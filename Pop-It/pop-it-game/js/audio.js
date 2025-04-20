// This file handles audio integration, including functions to play background music, sound effects for button presses, and sounds for game end scenarios (win/lose).

const audio = {
    backgroundMusic: new Audio('assets/audio/background.mp3'),
    popSound: new Audio('assets/audio/pop.mp3'),
    winSound: new Audio('assets/audio/win.mp3'),

    playBackgroundMusic: function() {
        this.backgroundMusic.loop = true;
        this.backgroundMusic.volume = 0.5; // Set volume to 50%
        this.backgroundMusic.play();
    },

    stopBackgroundMusic: function() {
        this.backgroundMusic.pause();
        this.backgroundMusic.currentTime = 0; // Reset to start
    },

    playPopSound: function() {
        this.popSound.currentTime = 0; // Reset to start
        this.popSound.play();
    },

    playWinSound: function() {
        this.winSound.currentTime = 0; // Reset to start
        this.winSound.play();
    }
};

// Export the audio object for use in other modules
export default audio;