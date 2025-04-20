document.addEventListener('DOMContentLoaded', () => {
    // Game elements
    const bubbles = document.querySelectorAll('.bubble');
    const restartButton = document.getElementById('restart-btn');
    const soundToggle = document.getElementById('sound-toggle');
    const currentPlayerElement = document.getElementById('current-player');
    const remainingCountElement = document.getElementById('remaining-count');
    const gameMessage = document.getElementById('game-message');
    const pvpButton = document.getElementById('pvp-btn');
    const pveButton = document.getElementById('pve-btn');
    const startPopButton = document.getElementById('start-pop-btn');
    const endPopButton = document.getElementById('end-pop-btn');
    const strategyTip = document.querySelector('.strategy-tip');
    
    // Add click event listener to strategy tip
    if (strategyTip) {
        strategyTip.addEventListener('click', () => {
            strategyTip.classList.toggle('visible');
        });
    }
    
    // Audio elements
    const popSound = document.getElementById('pop-sound');
    const winSound = document.getElementById('win-sound');
    const backgroundMusic = document.getElementById('background-music');
    
    // Game state
    let gameState = {
        currentPlayer: 1, // 1 for Player 1, 2 for Player 2 or Computer
        remainingBubbles: 28, // Updated from 30 to 28
        poppedThisTurn: 0,
        gameOver: false,
        vsComputer: true,
        soundEnabled: true,
        poppingEnabled: false
    };
    
    // Add these variables to your existing game state variables
    let gameDifficulty = 'easy'; // Default difficulty
    let firstPlayer = 'human';   // Default first player
    let isPvEMode = true;        // Default game mode

    // Initialize the game
    initGame();
    
    function initGame() {
        // Reset game state
        gameState.currentPlayer = 1;
        gameState.remainingBubbles = 28; // Updated from 30 to 28
        gameState.poppedThisTurn = 0;
        gameState.gameOver = false;
        gameState.poppingEnabled = false;
        
        // Reset UI
        updateUI();
        
        // Reset bubbles
        bubbles.forEach(bubble => {
            bubble.classList.remove('popped');
            bubble.classList.remove('popping');
        });
        
        gameMessage.textContent = '';
        
        // Reset buttons
        startPopButton.disabled = false;
        endPopButton.disabled = true;
        
        // Start background music
        if (gameState.soundEnabled) {
            backgroundMusic.play().catch(error => {
                console.log("Audio autoplay was prevented:", error);
            });
        }

        // If computer goes first in PvE mode
        if (isPvEMode && firstPlayer === 'computer') {
            // Set current player to computer
            gameState.currentPlayer = 2;
            // Then make computer move
            setTimeout(computerTurn, 1000);
        }
    }
    
    // Update the game UI
    function updateUI() {
        if (gameState.vsComputer && gameState.currentPlayer === 2) {
            currentPlayerElement.textContent = 'Computer';
        } else {
            currentPlayerElement.textContent = `Player ${gameState.currentPlayer}`;
        }
        remainingCountElement.textContent = gameState.remainingBubbles;
        
        // Update button states based on whose turn it is
        if ((gameState.currentPlayer === 2 && gameState.vsComputer) || gameState.gameOver) {
            startPopButton.disabled = true;
            endPopButton.disabled = true;
        } else {
            startPopButton.disabled = gameState.poppingEnabled;
            endPopButton.disabled = !gameState.poppingEnabled || gameState.poppedThisTurn === 0;
        }
    }
    
    // Handle bubble click
    function handleBubbleClick(bubble) {
        if (gameState.gameOver || bubble.classList.contains('popped') || 
            (gameState.currentPlayer === 2 && gameState.vsComputer) || 
            !gameState.poppingEnabled) {
            return;
        }
        
        if (gameState.poppedThisTurn >= 3) {
            gameMessage.textContent = "You can only pop up to 3 bubbles per turn!";
            return;
        }
        
        // Pop the bubble
        popBubble(bubble);
        
        // Update end pop button state
        endPopButton.disabled = false;
    }
    
    // Pop a bubble
    function popBubble(bubble) {
        // Play pop sound
        if (gameState.soundEnabled) {
            popSound.currentTime = 0;
            popSound.play().catch(error => console.log("Audio play was prevented:", error));
        }
        
        // Visual effect
        bubble.classList.add('popping');
        
        setTimeout(() => {
            bubble.classList.remove('popping');
            bubble.classList.add('popped');
            
            // Update game state
            gameState.remainingBubbles--;
            gameState.poppedThisTurn++;
            
            // Update UI
            updateUI();
            
            // Check for game over
            if (gameState.remainingBubbles === 0) {
                const winner = gameState.currentPlayer === 1 ? 2 : 1;
                endGame(winner);
                return;
            }
            
            // Automatically end turn if 3 bubbles are popped
            if (gameState.poppedThisTurn === 3) {
                gameMessage.textContent = "Maximum 3 bubbles popped, ending turn automatically!";
                setTimeout(() => {
                    gameState.poppingEnabled = false;
                    endTurn();
                }, 500); // Short delay before switching turns
            }
        }, 300);
    }
    
    // End the current turn
    function endTurn() {
        if (gameState.gameOver) return;
        
        // Switch player
        gameState.currentPlayer = gameState.currentPlayer === 1 ? 2 : 1;
        gameState.poppedThisTurn = 0;
        gameState.poppingEnabled = false;
        
        // Update UI
        updateUI();
        
        // Clear any messages
        gameMessage.textContent = '';
        
        // Computer's turn
        if (gameState.currentPlayer === 2 && gameState.vsComputer && !gameState.gameOver) {
            setTimeout(computerTurn, 1000);
        } 
        // Player's turn after computer - auto enable popping
        else if (gameState.currentPlayer === 1 && gameState.vsComputer && !gameState.gameOver) {
            // Automatically enable popping for the player
            gameState.poppingEnabled = true;
            startPopButton.disabled = true;
            endPopButton.disabled = false;
            gameMessage.textContent = `${currentPlayerElement.textContent}, pop 1-3 bubbles!`;
            
            // Update UI again after enabling popping
            updateUI();
        }
    }
    
    // Computer AI logic
    function computerTurn() {
        if (gameState.gameOver) return;
        
        gameMessage.textContent = "Computer is thinking...";
        
        const unpoppedBubbles = Array.from(bubbles).filter(bubble => 
            !bubble.classList.contains('popped'));
            
        // Simple AI strategy: try to leave the opponent with 1, 5, 9, 13, 17... bubbles
        // These are the "bad positions" in Nim game theory
        let optimalMove;
        const targetRemainders = [1, 5, 9, 13, 17];
        
        for (let toBePop = 1; toBePop <= 3; toBePop++) {
            const newRemaining = gameState.remainingBubbles - toBePop;
            if (targetRemainders.includes(newRemaining)) {
                optimalMove = toBePop;
                break;
            }
        }
        
        // If no optimal move found or only one bubble left, just pop one
        if (!optimalMove || unpoppedBubbles.length <= 1) {
            optimalMove = Math.min(gameState.remainingBubbles, 1);
        } else if (unpoppedBubbles.length <= 3) {
            // If few bubbles left, don't pop all unless it's advantageous
            optimalMove = Math.min(optimalMove, unpoppedBubbles.length - 1);
            if (optimalMove <= 0) optimalMove = 1;
        }
        
        // Perform the computer's moves
        setTimeout(() => {
            gameMessage.textContent = "Computer is popping...";
            
            // Simulate "Start Pop" for computer
            gameState.poppingEnabled = true;
            
            for (let i = 0; i < optimalMove; i++) {
                if (unpoppedBubbles[i]) {
                    setTimeout(() => {
                        popBubble(unpoppedBubbles[i]);
                        
                        // Check if this was the last move in the turn
                        if (i === optimalMove - 1 || gameState.remainingBubbles === 0) {
                            setTimeout(() => {
                                gameMessage.textContent = "Computer finished its turn";
                                gameState.poppingEnabled = false;
                                endTurn();
                            }, 500);
                        }
                    }, i * 500);
                }
            }
        }, 1000);
    }
    
    // End the game
    function endGame(winner) {
        gameState.gameOver = true;
        
        const winnerText = winner === 1 ? "Player 1" : 
                          (gameState.vsComputer ? "Computer" : "Player 2");
        
        gameMessage.textContent = `${winnerText} wins the game!`;
        
        // Disable popping buttons
        startPopButton.disabled = true;
        endPopButton.disabled = true;
        
        // Play win sound
        if (gameState.soundEnabled) {
            backgroundMusic.pause();
            winSound.play().catch(error => console.log("Audio play was prevented:", error));
        }
    }
    
    // Event listeners
    bubbles.forEach(bubble => {
        bubble.addEventListener('click', () => handleBubbleClick(bubble));
    });
    
    restartButton.addEventListener('click', initGame);
    
    soundToggle.addEventListener('click', () => {
        gameState.soundEnabled = !gameState.soundEnabled;
        soundToggle.textContent = gameState.soundEnabled ? '🔊' : '🔇';
        
        if (gameState.soundEnabled) {
            backgroundMusic.play().catch(error => console.log("Audio play was prevented:", error));
        } else {
            backgroundMusic.pause();
        }
    });
    
    pvpButton.addEventListener('click', () => {
        if (!gameState.gameOver || confirm("Start a new game?")) {
            gameState.vsComputer = false;
            pvpButton.classList.add('active');
            pveButton.classList.remove('active');
            initGame();
        }
    });
    
    pveButton.addEventListener('click', () => {
        if (!gameState.gameOver || confirm("Start a new game?")) {
            gameState.vsComputer = true;
            pveButton.classList.add('active');
            pvpButton.classList.remove('active');
            initGame();
        }
    });
    
    // Start Pop button
    startPopButton.addEventListener('click', () => {
        if (!gameState.gameOver) {
            gameState.poppingEnabled = true;
            startPopButton.disabled = true;
            endPopButton.disabled = false;
            gameMessage.textContent = `${currentPlayerElement.textContent}, pop 1-3 bubbles!`;
        }
    });
    
    // End Pop button
    endPopButton.addEventListener('click', () => {
        if (!gameState.gameOver && gameState.poppingEnabled && gameState.poppedThisTurn > 0) {
            // Explicitly disable End Pop and enable Start Pop
            endPopButton.disabled = true;
            startPopButton.disabled = false;
            endTurn();
        }
    });
    
    // Enable sound on first user interaction with the page
    document.addEventListener('click', () => {
        if (gameState.soundEnabled && backgroundMusic.paused) {
            backgroundMusic.play().catch(error => console.log("Audio play was prevented:", error));
        }
    }, { once: true });

    // Event listeners for the new settings
    document.querySelectorAll('input[name="difficulty"]').forEach(radio => {
        radio.addEventListener('change', function() {
            gameDifficulty = this.value;
            console.log(`Difficulty set to: ${gameDifficulty}`);
        });
    });

    document.querySelectorAll('input[name="firstPlayer"]').forEach(radio => {
        radio.addEventListener('change', function() {
            firstPlayer = this.value;
            console.log(`First player set to: ${firstPlayer}`);
        });
    });

    // Modify your existing mode selection buttons
    document.getElementById('pve-btn').addEventListener('click', function() {
        isPvEMode = true;
        document.getElementById('game-settings').style.display = 'block';
        // Any other existing code for mode selection
    });

    document.getElementById('pvp-btn').addEventListener('click', function() {
        isPvEMode = false;
        document.getElementById('game-settings').style.display = 'none';
        // Any other existing code for mode selection
    });

    // Modify your computer move function to implement different difficulty levels
    function computerMove() {
        if (gameState.gameOver) return;
        
        gameMessage.textContent = "Computer is thinking...";
        
        const unpoppedBubbles = Array.from(bubbles).filter(bubble => 
            !bubble.classList.contains('popped'));
            
        let bubblesToPop;
        
        switch(gameDifficulty) {
            case 'easy':
                // Random number between 1-3
                bubblesToPop = Math.floor(Math.random() * 3) + 1;
                break;
                
            case 'medium':
                // Smarter random strategy
                // Sometimes makes optimal moves, sometimes random
                if (Math.random() > 0.6) {
                    bubblesToPop = getOptimalMove(gameState.remainingBubbles);
                } else {
                    bubblesToPop = Math.floor(Math.random() * 3) + 1;
                }
                break;
                
            case 'hard':
                // Always make optimal move
                bubblesToPop = getOptimalMove(gameState.remainingBubbles);
                break;
        }
        
        // Make sure we don't pop more bubbles than available
        bubblesToPop = Math.min(bubblesToPop, gameState.remainingBubbles);
        
        // Perform the computer's moves
        setTimeout(() => {
            gameMessage.textContent = "Computer is popping...";
            
            // Simulate "Start Pop" for computer
            gameState.poppingEnabled = true;
            
            for (let i = 0; i < bubblesToPop; i++) {
                if (unpoppedBubbles[i]) {
                    setTimeout(() => {
                        popBubble(unpoppedBubbles[i]);
                        
                        // Check if this was the last move in the turn
                        if (i === bubblesToPop - 1 || gameState.remainingBubbles === 0) {
                            setTimeout(() => {
                                gameMessage.textContent = "Computer finished its turn";
                                gameState.poppingEnabled = false;
                                endTurn();
                            }, 500);
                        }
                    }, i * 500);
                }
            }
        }, 1000);
    }

    // New function to calculate optimal move
    function getOptimalMove(remainingBubbles) {
        // Nim game optimal strategy:
        // Try to leave opponent with a multiple of 4 bubbles
        const remainder = remainingBubbles % 4;
        
        if (remainder === 0) {
            // Not in winning position, pop 1 randomly
            return 1;
        } else {
            // Pop enough to leave a multiple of 4
            return remainder;
        }
    }
});
