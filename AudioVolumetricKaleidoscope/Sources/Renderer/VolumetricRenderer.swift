import Metal
import MetalKit
import simd

class VolumetricRenderer: NSObject, MTKViewDelegate {
    public var device: MTLDevice!
    private var commandQueue: MTLCommandQueue!
    private var pipelineState: MTLRenderPipelineState!

    public var bassEnergy: Float = 0.0
    public var midEnergy: Float = 0.0
    public var trebleEnergy: Float = 0.0
    public var foldIntensity: Float = 1.0

    private var startTime = CACurrentMediaTime()

    init?(metalKitView: MTKView) {
        super.init()
        guard let defaultDevice = MTLCreateSystemDefaultDevice() else { return nil }
        self.device = defaultDevice
        metalKitView.device = defaultDevice

        self.commandQueue = device.makeCommandQueue()
        metalKitView.delegate = self

        setupPipeline(view: metalKitView)
    }

    private func setupPipeline(view: MTKView) {
        guard let library = device.makeDefaultLibrary() else { return }
        let descriptor = MTLRenderPipelineDescriptor()
        descriptor.vertexFunction = library.makeFunction(name: "volumetricVertexShader")
        descriptor.fragmentFunction = library.makeFunction(name: "volumetricFragmentShader")
        descriptor.colorAttachments[0].pixelFormat = view.colorPixelFormat

        pipelineState = try? device.makeRenderPipelineState(descriptor: descriptor)
    }

    func draw(in view: MTKView) {
        guard let drawable = view.currentDrawable,
              let renderPassDescriptor = view.currentRenderPassDescriptor,
              let pipelineState = pipelineState else { return }

        let elapsedTime = Float(CACurrentMediaTime() - startTime)
        let commandBuffer = commandQueue.makeCommandBuffer()
        let encoder = commandBuffer?.makeRenderCommandEncoder(descriptor: renderPassDescriptor)

        // Slowly orbit camera in 3D around kaleidoscope origin
        let cameraRadius: Float = 3.0
        let camX = sin(elapsedTime * 0.3) * cameraRadius
        let camZ = -cos(elapsedTime * 0.3) * cameraRadius

        var uniforms = VolumetricUniforms(
            resolution: simd_make_float2(Float(view.drawableSize.width), Float(view.drawableSize.height)),
            time: elapsedTime,
            cameraPos: simd_make_float3(camX, 0.0, camZ),
            bassEnergy: bassEnergy,
            midEnergy: midEnergy,
            trebleEnergy: trebleEnergy,
            foldIntensity: foldIntensity
        )

        encoder?.setRenderPipelineState(pipelineState)
        encoder?.setFragmentBytes(&uniforms, length: MemoryLayout<VolumetricUniforms>.stride, index: 0)

        encoder?.drawPrimitives(type: .triangleStrip, vertexStart: 0, vertexCount: 4)
        encoder?.endEncoding()

        commandBuffer?.present(drawable)
        commandBuffer?.commit()
    }

    func mtkView(_ view: MTKView, drawableSizeWillChange size: CGSize) {}
}
