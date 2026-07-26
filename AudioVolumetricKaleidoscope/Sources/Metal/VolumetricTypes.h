#ifndef VolumetricTypes_h
#define VolumetricTypes_h

#ifdef __METAL_VERSION__
#include <metal_stdlib>
using namespace metal;
#else
#import <simd/simd.h>
#endif

typedef struct {
#ifdef __METAL_VERSION__
    float2 resolution;
    float time;
    float3 cameraPos;
    float bassEnergy;
    float midEnergy;
    float trebleEnergy;
    float foldIntensity;
#else
    simd_float2 resolution;
    float time;
    simd_float3 cameraPos;
    float bassEnergy;
    float midEnergy;
    float trebleEnergy;
    float foldIntensity;
#endif
} VolumetricUniforms;

#endif
