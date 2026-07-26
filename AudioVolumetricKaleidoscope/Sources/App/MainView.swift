import SwiftUI

struct MainView: View {
    @StateObject private var audioAnalyzer = FFTAnalyzer()
    @State private var foldIntensity: Float = 1.0

    var body: some View {
        ZStack {
            VolumetricMetalView(
                bassEnergy: audioAnalyzer.bassEnergy,
                midEnergy: audioAnalyzer.midEnergy,
                trebleEnergy: audioAnalyzer.trebleEnergy,
                foldIntensity: foldIntensity
            )
            .edgesIgnoringSafeArea(.all)

            // Audio Visualizer Overlay
            VStack {
                HStack(spacing: 12) {
                    AudioBar(label: "BASS", value: audioAnalyzer.bassEnergy, color: .red)
                    AudioBar(label: "MID", value: audioAnalyzer.midEnergy, color: .green)
                    AudioBar(label: "TREBLE", value: audioAnalyzer.trebleEnergy, color: .blue)
                }
                .padding()
                .background(.ultraThinMaterial)
                .cornerRadius(12)
                .padding(.top, 50)

                Spacer()

                VStack {
                    Text("Fold Complexity")
                        .foregroundColor(.white)
                    Slider(value: $foldIntensity, in: 0.5...3.0)
                }
                .padding()
                .background(.ultraThinMaterial)
                .cornerRadius(16)
                .padding()
            }
        }
    }
}

struct AudioBar: View {
    let label: String
    let value: Float
    let color: Color

    var body: some View {
        VStack {
            Text(label).font(.caption2).bold().foregroundColor(.white)
            GeometryReader { geo in
                VStack {
                    Spacer()
                    Rectangle()
                        .fill(color)
                        .frame(height: geo.size.height * CGFloat(value))
                }
            }
            .frame(width: 20, height: 60)
            .background(Color.white.opacity(0.2))
            .cornerRadius(4)
        }
    }
}
