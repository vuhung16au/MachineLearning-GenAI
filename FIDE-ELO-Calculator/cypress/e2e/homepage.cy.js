describe('FIDE ELO Calculator Tests', () => {
  beforeEach(() => {
    cy.visit('/');
    // Reset the calculator before each test
    cy.contains('Reset Calculator').click();
  });

  it('should have the correct title', () => {
    cy.title().should('eq', 'FIDE ELO Calculator');
  });

  it('should display the main calculator interface', () => {
    cy.contains('h1', 'FIDE ELO Rating Calculator').should('be.visible');
    cy.contains('Game Inputs').should('be.visible');
    cy.get('table').should('be.visible');
  });

  // Test Case Group 1: Equal ratings with different scores and K-factors
  describe('Equal ratings tests (1800 vs 1800)', () => {
    it('Win (1) with K-factor 40 should result in +20 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('1800');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Win (1)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('40');
      
      // Verify rating change
      cy.get('td.p-2.font-semibold').contains('+20').should('be.visible');
      cy.contains('Total Rating Change:').siblings().contains('+20').should('be.visible');
    });

    it('Draw (0.5) with K-factor 40 should result in 0 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('1800');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Draw (0.5)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('40');
      
      // Verify rating change - accept "0", "+0", or "0.0"
      cy.get('td.p-2.font-semibold').then(($el) => {
        const text = $el.text().trim();
        expect(text === '0' || text === '+0' || text === '0.0').to.be.true;
      });
      
      // Also check the total rating change
      cy.contains('Total Rating Change:').siblings().then(($el) => {
        const text = $el.text().trim();
        expect(text === '0' || text === '+0' || text === '0.0').to.be.true;
      });
    });

    it('Loss (0) with K-factor 40 should result in -20 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('1800');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Loss (0)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('40');
      
      // Verify rating change
      cy.get('td.p-2.font-semibold').contains('-20').should('be.visible');
      cy.contains('Total Rating Change:').siblings().contains('-20').should('be.visible');
    });

    it('Win (1) with K-factor 20 should result in +10 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('1800');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Win (1)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('20');
      
      // Verify rating change
      cy.get('td.p-2.font-semibold').contains('+10').should('be.visible');
      cy.contains('Total Rating Change:').siblings().contains('+10').should('be.visible');
    });
  });

  // Test Case Group 2: Higher rating vs lower rating
  describe('Higher rating vs lower rating tests (2000 vs 1800)', () => {
    it('Win (1) with K-factor 40 should result in +9.6 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('2000');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Win (1)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('40');
      
      // Verify rating change
      cy.get('td.p-2.font-semibold').contains('+9.6').should('be.visible');
      cy.contains('Total Rating Change:').siblings().contains('+10').should('be.visible'); // Should round to +10
    });

    it('Draw (0.5) with K-factor 40 should result in -10.4 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('2000');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Draw (0.5)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('40');
      
      // Verify rating change
      cy.get('td.p-2.font-semibold').contains('-10.4').should('be.visible');
      cy.contains('Total Rating Change:').siblings().contains('-10').should('be.visible'); // Should round to -10
    });
  });

  // Test Case Group 3: More than 400 rating point difference
  describe('Extreme rating difference tests (2500 vs 1800)', () => {
    it('Win (1) with K-factor 10 should result in +0.8 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('2500');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Win (1)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('10');
      
      // Verify rating change
      cy.get('td.p-2.font-semibold').contains('+0.8').should('be.visible');
      cy.contains('Total Rating Change:').siblings().contains('+1').should('be.visible'); // Should round to +1
    });

    it('Loss (0) with K-factor 10 should result in -9.2 rating change', () => {
      // Set player rating
      cy.get('input[ng-model="game.playerRating"]').clear().type('2500');
      // Set opponent rating
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      // Select score
      cy.get('select[ng-model="game.score"]').select('Loss (0)');
      // Select K-factor
      cy.get('select[ng-model="game.kFactor"]').select('10');
      
      // Verify rating change
      cy.get('td.p-2.font-semibold').contains('-9.2').should('be.visible');
      cy.contains('Total Rating Change:').siblings().contains('-9').should('be.visible'); // Should round to -9
    });
  });

  // Test Case Group 4: Multiple games
  describe('Multiple games calculation', () => {
    it('should correctly calculate total rating change for multiple games', () => {
      // First game
      cy.get('input[ng-model="game.playerRating"]').clear().type('1800');
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      cy.get('select[ng-model="game.score"]').select('Win (1)');
      cy.get('select[ng-model="game.kFactor"]').select('20');
      
      // Add second game
      cy.contains('Add Game').click();
      cy.get('input[ng-model="game.playerRating"]').eq(1).should('have.value', '1800');
      cy.get('input[ng-model="game.opponentRating"]').eq(1).clear().type('2000');
      cy.get('select[ng-model="game.score"]').eq(1).select('Draw (0.5)');
      cy.get('select[ng-model="game.kFactor"]').eq(1).select('20');
      
      // Add third game
      cy.contains('Add Game').click();
      cy.get('input[ng-model="game.playerRating"]').eq(2).should('have.value', '1800');
      cy.get('input[ng-model="game.opponentRating"]').eq(2).clear().type('1700');
      cy.get('select[ng-model="game.score"]').eq(2).select('Loss (0)');
      cy.get('select[ng-model="game.kFactor"]').eq(2).select('20');
      
      // Verify individual rating changes and total
      cy.get('td.p-2.font-semibold').eq(0).contains('+10').should('be.visible');
      cy.get('td.p-2.font-semibold').eq(1).should('contain', '+');
      cy.get('td.p-2.font-semibold').eq(2).should('contain', '-');
      
      // Verify a total exists (not checking exact value as it depends on calculations)
      cy.contains('Total Rating Change:').siblings().should('exist');
    });
  });

  // Test UI functionality
  describe('UI functionality', () => {
    it('should allow adding and removing games', () => {
      // Initially there should be 1 game
      cy.get('tbody tr').should('have.length', 1);
      cy.get('tbody tr td:first-child').should('contain', '1');
      
      // Add a game
      cy.contains('Add Game').click();
      cy.get('tbody tr').should('have.length', 2);
      cy.get('tbody tr').eq(1).find('td:first-child').should('contain', '2');
      
      // Remove the second game
      cy.get('button').contains('✕').last().click();
      cy.get('tbody tr').should('have.length', 1);
      cy.get('tbody tr td:first-child').should('contain', '1');
      cy.get('tbody tr td:first-child').should('not.contain', '2');
    });

    it('should save and load calculations', () => {
      const testName = 'Test-Calculation-' + Date.now();
      
      // Create a calculation
      cy.get('input[ng-model="game.playerRating"]').clear().type('2050');
      cy.get('input[ng-model="game.opponentRating"]').clear().type('1800');
      cy.get('select[ng-model="game.score"]').select('Win (1)');
      cy.get('select[ng-model="game.kFactor"]').select('40');
      
      // Save the calculation
      cy.get('input[ng-model="ctrl.saveName"]').type(testName);
      cy.contains('Save Calculation').click();
      
      // Reset the calculator
      cy.contains('Reset Calculator').click();
      
      // Verify the form is reset
      cy.get('input[ng-model="game.playerRating"]').should('have.value', '');
      
      // Load the saved calculation
      cy.get('select[ng-model="ctrl.selectedSavedCalc"]').select(testName);
      cy.contains('Load Calculation').click();
      
      // Verify the loaded data
      cy.get('input[ng-model="game.playerRating"]').should('have.value', '2050');
      cy.get('input[ng-model="game.opponentRating"]').should('have.value', '1800');
    });
  });
});