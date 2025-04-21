// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************

// -- This is a parent command --
Cypress.Commands.add('fillCalculatorForm', (playerRating, opponentRating, score, kFactor) => {
  if (playerRating) {
    cy.get('input[ng-model="game.playerRating"]').clear().type(playerRating);
  }
  if (opponentRating) {
    cy.get('input[ng-model="game.opponentRating"]').clear().type(opponentRating);
  }
  if (score) {
    cy.get('select[ng-model="game.score"]').select(score);
  }
  if (kFactor) {
    cy.get('select[ng-model="game.kFactor"]').select(kFactor.toString());
  }
});

// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add('login', (username, password) => {
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(password);
    cy.get('button[type="submit"]').click();
});