FIDE ELO Calculator (support multiple games)

# Objectvies:
Create a FIDE ELO calculator that support multiple input and custom K-factor 

# FIDE ELO Calculator 
https://ratings.fide.com/calc.phtml?page=change

This page can calculate ELO based on player and opponent's FIDE ELO rating, with K factor fixed to 10, 15, 20, 30, 40 -> 

# The inputs include 

The input is design as a table, have up to 11 rows, each row contains the following inputs: 
- Integer input: Player rating
- Integer input: Opponent rating
- Dropdown list: Score (win (1), draw (1/2), lost (0))
- K-factor dropdown list: 10, 15, 20, 30, 40 or users can input any integer between 10 and 40. The default value is 40.
- Button: "Calculate Rating Change", when clicked, show the "Rating changes"


Example:

Rating: 2050
Opponent Rating: 2353
Score: 1 / K factor: 40
Rating Change is: +34.4

# Case/Example:

A players with ELO rating 2050 plays 11 games in a chess tournaments.
After each game, he wants to how many ELO he gains or loses.
Also, he also wants to know, after the 11 games of the tournament, how many ELO he gains or loses. 

Until now, he has been using "FIDE ELO Calculator" to calculate ELO changes for each game one by one.

And he'll want to enter 11 games at a time! 

# Use stories:
- Users can input player/opponent ratings, score, k-factor from multiple games to calculate ratings change after each games or after the tournamens (has multiple games)
- Users can save up to 30 ELO calculations to local storage using cookies
- Users can load calculated ELO from cookies and display 

# Technologies:
- HTML, CSS, JS, cookies
- AngularJS to display the tables of possible (pls suggest me)

# NFR

- Responsive to web/mobile browsers 
- Simple, light-weight
- Instantly calculate ELO changes as users finishes entering info for each game (in a line)
- Tailwind for fancy looks and feel 

# Put the reference links at the footer of this page

- (FIDE) Calculators for Chess Rating https://ratings.fide.com/calc.phtml?page=change

- FIDE Handbook: https://handbook.fide.com/chapter/B022024

Legends:
```
Rating - Rating of a player.
Rc - Opponent rating.
W - Score.
K val - K is the development coefficient.
K is the development coefficient.
K = 40 for a player new to the rating list until he has completed events with at least 30 games
K = 20 as long as a player's rating remains under 2400.
K = 10 once a player's published rating has reached 2400 and remains at that level subsequently, even if the rating drops below 2400.
K = 40 for all players until their 18th birthday, as long as their rating remains under 2300.
```

# Additional features:

Add to 'index.html' a section named "ELO Changes Calculation Example" just below the section "Important FIDE Rating Rules"

This sections explain FIDE rules 8.3.1, 8.3.2, 8.3.3 and 8.3.4

Using example

Pls note the elo diff is greater than 400
```
Difference of more than 400 is counted as 400.
Rating: 1300
Opponent Rating: 1800
Score: 1 / K factor: 30
Rating Change is: +27.6
```

```
Rating: 2050
Opponent Rating: 1800
Score: 0.5 / K factor: 40
Rating Change is: -12.4
```

When a players plays N = 21 games, and his K factor = 40, 
explain how K factor is adjusted (it is 21)

Use maths formula (mathjax?) to write beautiful formula.

Add a section to explain "FIDE Handbook chapter 8.3.4"

Use example below

A player plays 2 games:

Rating: 2000
Opponent Rating: 1800
Score: 0.5 / K factor: 40

Rating: 2000
Opponent Rating: 1600
Score: 0 / K factor: 40

How his rating change? Explain the calculation as example.

# Verification

Verify that all the sections 8.3.1, 8.3.2, 8.3.3 and 8.3.4 are correctly implemented
- Check that the K factor is set to 40 for new players until they have completed 30 games.

# Cypress test

Pls use cypress to test the following:
- input data in the file 'fide-test-data.txt'


# Responsive design

make sure that index.html is responsive to smartphone, display correctly under different size of browser size

