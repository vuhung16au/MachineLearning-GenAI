


**Prompt for Claude: Build a FIDE ELO Calculator Supporting Multiple Games**

**Objective**:  
Develop a web-based FIDE ELO Calculator that supports calculating rating changes for multiple chess games simultaneously, with customizable K-factors, and includes features for saving and loading calculations.

**Reference**:  
The calculator should align with the FIDE ELO rating change formula as described on the FIDE website:  
- [FIDE Rating Change Calculator](https://ratings.fide.com/calc.phtml?page=change)  
- [FIDE Handbook](https://handbook.fide.com/chapter/B022024)

**Functional Requirements**:

1. **Input Interface**:  
   - Display a table with up to 11 rows, each representing a game. Each row should include:  
     - **Player Rating**: Integer input (e.g., 2050).  
     - **Opponent Rating**: Integer input (e.g., 2353).  
     - **Score**: Dropdown with options: Win (1), Draw (0.5), Loss (0).  
     - **K-factor**: Dropdown with values (10, 15, 20, 30, 40) or a custom integer input (10–40). Default: 40.  
   - Include a "Calculate Rating Change" button to compute and display results.

2. **Output**:  
   - For each game row, display the rating change (e.g., +34.4 or -12.3) immediately after input is complete or when the "Calculate" button is clicked.  
   - Display the cumulative rating change across all games (e.g., total ELO gained/lost after 11 games).  
   - Format rating changes to one decimal place.

3. **Storage Features**:  
   - Allow users to save up to 30 ELO calculation sets (each set contains up to 11 games) using browser cookies or local storage.  
   - Provide a "Save Calculation" button to store the current table’s data.  
   - Provide a "Load Calculation" dropdown or list to retrieve and display a previously saved calculation.

4. **Example Use Case**:  
   A player with an ELO rating of 2050 plays 11 games in a chess tournament. They want to:  
   - Input ratings, opponent ratings, scores, and K-factors for all 11 games at once.  
   - See the ELO change for each game and the total ELO change after the tournament.  
   - Save the calculation for future reference and load it later.

**Non-Functional Requirements**:  
- **Responsive Design**: Ensure the calculator is usable on web and mobile browsers.  
- **Performance**: Calculate and display ELO changes instantly as users enter data for each game.  
- **Simplicity**: Keep the interface lightweight and intuitive.  
- **Styling**: Use Tailwind CSS for a modern, clean, and professional look.

**Technical Requirements**:  
- **Frontend**: HTML, CSS (Tailwind), JavaScript.  
- **Framework**: Use AngularJS (or suggest an alternative like React or Vue.js if more suitable) to manage the dynamic table and calculations.  
- **Storage**: Use browser cookies or local storage for saving/loading calculations.  
- **Formula**: Implement the FIDE ELO rating change formula:  
  - Expected Score: \( E = 1 / (1 + 10^{(Rc - R)/400}) \)  
  - Rating Change: \( \Delta R = K \cdot (W - E) \)  
  - Where:  
    - \( R \): Player rating  
    - \( Rc \): Opponent rating  
    - \( W \): Score (1 for win, 0.5 for draw, 0 for loss)  
    - \( K \): K-factor (10, 15, 20, 30, 40, or custom 10–40)  
- **K-factor Legend**:  
  - \( K = 40 \): For new players (until 30 games) or players under 18 with rating < 2300.  
  - \( K = 20 \): For players with rating < 2400.  
  - \( K = 10 \): For players with rating ≥ 2400 (remains even if rating drops below 2400).

([FIDE Handbook, Chapter B.022024](https://handbook.fide.com/chapter/B022024)) 

K is the development coefficient.
- K = 40 for a player new to the rating list until they have completed events with at least 30 games.
- K = 20 as long as a player's rating remains under 2400.
- K = 10 once a player's published rating has reached 2400 and remains at that level subsequently, even if the rating drops below 2400.
- K = 40 for all players until the end of the year of their 18th birthday, as long as their rating remains under 2300.

If the number of games (n) for a player on any list for a rating period multiplied by K (as defined above) exceeds 700, then K shall be the largest whole number such that K x n does not exceed 700.


**Deliverables**:  
- A complete HTML/CSS/JS codebase for the calculator.  
- Instructions for running the application locally.  
- Optional: Suggestions for improving the UI/UX or technology stack (e.g., replacing AngularJS with a modern framework).

**Constraints**:  
- Avoid server-side logic; the application should run entirely in the browser.  
- Ensure compatibility with modern browsers (Chrome, Firefox, Safari).

**References**:  
- [FIDE Rating Change Calculator](https://ratings.fide.com/calc.phtml?page=change)  
- [FIDE Handbook](https://handbook.fide.com/chapter/B022024)
