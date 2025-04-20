# Pop-It Game Requirements

## Overview
Create a fun, web-based Pop-It game for kids using HTML, CSS, and JavaScript.

## Game Board Design
- Heart-shaped board with approximately 30 bubble buttons
- Colorful design, primarily using pink and red tones
- Include animations for button presses (visual "pop" effect)
- Page background: Light purple heart shape
- Bubble container background: Light pink heart shape

## Gameplay Mechanics
- Two-player game (Player vs. Player or Player vs. Computer)
- Players take turns pressing unpopped buttons using a mouse or touch screen
- On their turn, a player must pop 1, 2, or 3 buttons (cannot skip a turn or pop 0 or 4+ buttons)
- Once popped, a button is marked as "popped," visually pressed, and cannot be popped again
- The player who pops the last button loses the game
- Display the number of unpopped buttons remaining on the board

## Game Modes & Difficulty
- **Player Options:**
    - Choose who plays first: Human or Computer
    - Toggle between Player vs. Player or Player vs. Computer modes
- **Difficulty Levels (Computer AI):**
    - Level 1: Easy - Computer pops random numbers of bubbles
    - Level 2: Medium - Computer pops random numbers of bubbles but stronger
    - Level 3: Try Hard - Computer plays optimal moves to win the game

## User Interface
- **Layout:**
    - Game board positioned on the left side of screen
    - Settings panel on the right side of screen
    - "Restart Game" button to reset the game at any time
- **Settings Panel:**
    - Game mode selection (Player vs Computer/Player vs Player)
    - Computer difficulty settings
    - First player selection
- **Game Controls:**
    - Toggle functionality between "Start Pop" and "End Pop" buttons
    - When "Start Pop" is pressed, disable it and enable "End Pop"
    - When "End Pop" is pressed, disable it and enable "Start Pop"
- **Help Section:**
    - Include "How to play" section at the bottom of the page
    - Add a "Strategy tip" section that's initially hidden
    - Strategy tip only visible when users hover or click on it
    - Content: "Strategy tip: Try to leave your opponent with 5, 9, 13, or 17 bubbles!"

## Audio Features
- Background music that loops during gameplay
- "Pop" sound effect when a button is pressed
- Distinct sound when the game ends (win/lose)

## Technical Requirements
- Web-based, playable in modern browsers
- Responsive and visually appealing for kids
- **Technologies:**
    - HTML, CSS, and JavaScript
- **File/Folder Structure:**
    - `index.html`: Main game file
    - `./css/`: Store all CSS files (e.g., `styles.css`)
    - `./js/`: Store all JavaScript files (e.g., `game.js`)
- Follow clear naming conventions (camelCase for variables/functions, descriptive names)
- Well-commented, modular code that follows best practices for maintainability

## Deliverables
- Complete HTML structure with the heart-shaped board and UI elements
- CSS for styling, animations, and responsive design
- JavaScript for game logic, sound integration, and computer AI
- Instructions for adding audio files (where to place MP3 files)
