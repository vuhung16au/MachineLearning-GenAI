#include <metal_stdlib>
#include "VolumetricTypes.h"

using namespace metal;

struct VertexOut {
    float4 position [[position]];
    float2 uv;
};

vertex VertexOut volumetricVertexShader(uint vertexID [[vertex_id]]) {
    float2 positions[4] = {
        float2(-1.0, -1.0),
        float2( 1.0, -1.0),
        float2(-1.0,  1.0),
        float2( 1.0,  1.0)
    };

    VertexOut out;
    out.position = float4(positions[vertexID], 0.0, 1.0);
    out.uv = positions[vertexID] * 0.5 + 0.5;
    return out;
}

// 3D Kaleidoscope Space Folding
float3 fold3DSpace(float3 p, float intensity) {
    for (int i = 0; i < 5; ++i) {
        p = abs(p) - float3(0.4 * intensity);
        // Rotate in 3D around Y and Z axes
        float s = sin(0.5 + intensity * 0.2);
        float c = cos(0.5 + intensity * 0.2);
        p.xy = float2(c * p.x - s * p.y, s * p.x + c * p.y);
        if (p.x < p.y) p.xy = p.yx;
        if (p.x < p.z) p.xz = p.zx;
        if (p.y < p.z) p.yz = p.zy;
    }
    return p;
}

// Distance Estimator
float sceneSDF(float3 p, constant VolumetricUniforms &uniforms) {
    float3 foldedP = fold3DSpace(p, uniforms.foldIntensity + uniforms.bassEnergy * 0.5);
    float box = length(max(abs(foldedP) - float3(0.3 + uniforms.trebleEnergy * 0.2), 0.0)) - 0.05;
    return box;
}

// Normal calculation via finite differences
float3 calcNormal(float3 p, constant VolumetricUniforms &uniforms) {
    float e = 0.001;
    return normalize(float3(
        sceneSDF(p + float3(e, 0, 0), uniforms) - sceneSDF(p - float3(e, 0, 0), uniforms),
        sceneSDF(p + float3(0, e, 0), uniforms) - sceneSDF(p - float3(0, e, 0), uniforms),
        sceneSDF(p + float3(0, 0, e), uniforms) - sceneSDF(p - float3(0, 0, e), uniforms)
    ));
}

fragment float4 volumetricFragmentShader(VertexOut in [[stage_in]],
                                          constant VolumetricUniforms &uniforms [[buffer(0)]]) {
    // Setup camera ray
    float2 st = (in.uv - 0.5) * 2.0;
    st.x *= (uniforms.resolution.x / uniforms.resolution.y);

    float3 ro = uniforms.cameraPos;
    float3 rd = normalize(float3(st, 1.5)); // Ray direction with FOV scaling

    // Raymarching loop
    float t = 0.0;
    float maxDist = 20.0;
    int maxSteps = 64;
    float hitDist = -1.0;

    for (int i = 0; i < maxSteps; ++i) {
        float3 p = ro + rd * t;
        float d = sceneSDF(p, uniforms);

        if (d < 0.001) {
            hitDist = t;
            break;
        }
        t += d;
        if (t >= maxDist) break;
    }

    // Color generation
    if (hitDist > 0.0) {
        float3 p = ro + rd * hitDist;
        float3 normal = calcNormal(p, uniforms);

        // Dynamic lighting based on Audio Spectrum (Bass = Red/Gold, Mid = Cyan, Treble = Magenta)
        float light = max(0.0, dot(normal, normalize(float3(1.0, 2.0, -1.0))));
        float3 baseColor = float3(
            0.5 + 0.5 * sin(uniforms.time + p.x * 2.0 + uniforms.bassEnergy * 3.0),
            0.5 + 0.5 * sin(uniforms.time + p.y * 2.0 + uniforms.midEnergy * 3.0),
            0.5 + 0.5 * sin(uniforms.time + p.z * 2.0 + uniforms.trebleEnergy * 3.0)
        );

        float3 finalColor = baseColor * (light + 0.2) + pow(light, 16.0); // Diffuse + Specular

        // Depth fog attenuation
        finalColor = mix(finalColor, float3(0.02, 0.02, 0.05), 1.0 - exp(-0.1 * hitDist));
        return float4(finalColor, 1.0);
    }

    // Background cosmic gradient
    return float4(0.02, 0.02, 0.05, 1.0);
}
