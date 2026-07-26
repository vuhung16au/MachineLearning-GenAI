import SwiftUI
import MetalKit

#if os(macOS)
struct VolumetricMetalView: NSViewRepresentable {
    var bassEnergy: Float
    var midEnergy: Float
    var trebleEnergy: Float
    var foldIntensity: Float

    func makeNSView(context: Context) -> MTKView {
        let view = MTKView()
        if let renderer = VolumetricRenderer(metalKitView: view) {
            context.coordinator.renderer = renderer
            view.delegate = renderer
        }
        return view
    }

    func updateNSView(_ nsView: MTKView, context: Context) {
        if let renderer = context.coordinator.renderer {
            renderer.bassEnergy = bassEnergy
            renderer.midEnergy = midEnergy
            renderer.trebleEnergy = trebleEnergy
            renderer.foldIntensity = foldIntensity
        }
    }

    func makeCoordinator() -> Coordinator {
        Coordinator()
    }

    class Coordinator {
        var renderer: VolumetricRenderer?
    }
}
#else
struct VolumetricMetalView: UIViewRepresentable {
    var bassEnergy: Float
    var midEnergy: Float
    var trebleEnergy: Float
    var foldIntensity: Float

    func makeUIView(context: Context) -> MTKView {
        let view = MTKView()
        if let renderer = VolumetricRenderer(metalKitView: view) {
            context.coordinator.renderer = renderer
            view.delegate = renderer
        }
        return view
    }

    func updateUIView(_ uiView: MTKView, context: Context) {
        if let renderer = context.coordinator.renderer {
            renderer.bassEnergy = bassEnergy
            renderer.midEnergy = midEnergy
            renderer.trebleEnergy = trebleEnergy
            renderer.foldIntensity = foldIntensity
        }
    }

    func makeCoordinator() -> Coordinator {
        Coordinator()
    }

    class Coordinator {
        var renderer: VolumetricRenderer?
    }
}
#endif
