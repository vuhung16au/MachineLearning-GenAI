import AVFoundation
import Accelerate

class FFTAnalyzer: ObservableObject {
    @Published var bassEnergy: Float = 0.0
    @Published var midEnergy: Float = 0.0
    @Published var trebleEnergy: Float = 0.0

    private let audioEngine = AVAudioEngine()
    private let bufferSize: AVAudioFrameCount = 1024
    private var fftSetup: vDSP_DFT_Setup?

    init() {
        fftSetup = vDSP_DFT_zop_CreateSetup(nil, vDSP_Length(bufferSize), .FORWARD)
        setupAudioEngine()
    }

    private func setupAudioEngine() {
        let inputNode = audioEngine.inputNode
        let format = inputNode.outputFormat(forBus: 0)

        inputNode.installTap(onBus: 0, bufferSize: bufferSize, format: format) { [weak self] buffer, _ in
            self?.processAudio(buffer: buffer)
        }

        try? audioEngine.start()
    }

    private func processAudio(buffer: AVAudioPCMBuffer) {
        guard let floatData = buffer.floatChannelData?[0], let fftSetup = fftSetup else { return }

        var realInput = [Float](repeating: 0, count: Int(bufferSize))
        var imagInput = [Float](repeating: 0, count: Int(bufferSize))
        var realOutput = [Float](repeating: 0, count: Int(bufferSize))
        var imagOutput = [Float](repeating: 0, count: Int(bufferSize))

        // Windowing function (Hanning)
        var window = [Float](repeating: 0, count: Int(bufferSize))
        vDSP_hann_window(&window, vDSP_Length(bufferSize), Int32(vDSP_Hanning_Normalized))
        vDSP_vmul(floatData, 1, window, 1, &realInput, 1, vDSP_Length(bufferSize))

        // Execute Discrete Fourier Transform via vDSP
        vDSP_DFT_Execute(fftSetup, &realInput, &imagInput, &realOutput, &imagOutput)

        // Compute Magnitudes
        var magnitudes = [Float](repeating: 0, count: Int(bufferSize / 2))
        for i in 0..<Int(bufferSize / 2) {
            magnitudes[i] = sqrt(realOutput[i] * realOutput[i] + imagOutput[i] * imagOutput[i])
        }

        // Split Frequency Bands (Bass: 20-250Hz, Mid: 250-2000Hz, Treble: 2000-8000Hz)
        let bassSum = magnitudes[1...10].reduce(0, +) / 10.0
        let midSum = magnitudes[11...80].reduce(0, +) / 70.0
        let trebleSum = magnitudes[81...300].reduce(0, +) / 220.0

        DispatchQueue.main.async {
            self.bassEnergy = min(bassSum * 2.0, 1.0)
            self.midEnergy = min(midSum * 3.0, 1.0)
            self.trebleEnergy = min(trebleSum * 5.0, 1.0)
        }
    }

    deinit {
        if let fftSetup = fftSetup {
            vDSP_DFT_DestroySetup(fftSetup)
        }
    }
}
