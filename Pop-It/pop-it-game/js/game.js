// This file contains the main game logic for the Pop-It game, including functions for handling player turns, popping buttons, checking win conditions, and managing the game state. It also includes basic AI for the computer opponent.

const gameBoard = document.getElementById('game-board');
const playerTurnDisplay = document.getElementById('player-turn');
const resetButton = document.getElementById('reset-button');
const audio = new Audio('assets/audio/background.mp3');
let gameState = [];
let currentPlayer = 'Player';
let gameActive = true;

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function initializeGame() {
    gameState = Array(9).fill('');
    gameActive = true;
    playerTurnDisplay.innerText = `${currentPlayer}'s Turn`;
    gameBoard.innerHTML = '';
    for (let i = 0; i < 9; i++) {
        const button = document.createElement('button');
        button.classList.add('game-button');
        button.setAttribute('data-index', i);
        button.addEventListener('click', handleButtonClick);
        gameBoard.appendChild(button);
    }
    audio.loop = true;
    audio.play();
}

function handleButtonClick(event) {
    const clickedButton = event.target;
    const clickedIndex = parseInt(clickedButton.getAttribute('data-index'));

    if (gameState[clickedIndex] !== '' || !gameActive) {
        return;
    }

    gameState[clickedIndex] = currentPlayer;
    clickedButton.innerText = currentPlayer === 'Player' ? '💖' : '🤖';
    checkResult();
}

function checkResult() {
    let roundWon = false;

    for (let i = 0; i < winningConditions.length; i++) {
        const [a, b, c] = winningConditions[i];
        if (gameState[a] === '' || gameState[b] === '' || gameState[c] === '') {
            continue;
        }
        if (gameState[a] === gameState[b] && gameState[a] === gameState[c]) {
            roundWon = true;
            break;
        }
    }

    if (roundWon) {
        playerTurnDisplay.innerText = `${currentPlayer} Wins!`;
        gameActive = false;
        playAudio('win');
        return;
    }

    if (!gameState.includes('')) {
        playerTurnDisplay.innerText = 'Draw!';
        gameActive = false;
        return;
    }

    currentPlayer = currentPlayer === 'Player' ? 'AI' : 'Player';
    playerTurnDisplay.innerText = `${currentPlayer}'s Turn`;

    if (currentPlayer === 'AI') {
        setTimeout(aiTurn, 1000);
    }
}

function aiTurn() {
    let availableIndices = gameState.map((val, index) => val === '' ? index : null).filter(val => val !== null);
    const randomIndex = availableIndices[Math.floor(Math.random() * availableIndices.length)];
    const button = document.querySelector(`button[data-index='${randomIndex}']`);
    handleButtonClick({ target: button });
}

function playAudio(type) {
    const sound = new Audio(`assets/audio/${type}.mp3`);
    sound.play();
}

resetButton.addEventListener('click', initializeGame);
initializeGame();