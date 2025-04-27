import './css/tailwind.css'

// FIDE ELO Calculator - Main JavaScript entry point
// This file only adds the drag and drop functionality to the existing application

(function() {
    'use strict';
    
    // We need to wait for the Angular module to be available, which happens in index.html
    document.addEventListener('DOMContentLoaded', function() {
        // Add drag and drop functionality once the document is ready
        setTimeout(initDragAndDrop, 500); // Give Angular time to render everything
    });
    
    // Initialize drag and drop functionality
    function initDragAndDrop() {
        // Find all game rows
        var gameRows = document.querySelectorAll('tr.game-row');
        
        // Set up drag and drop for each row
        gameRows.forEach(function(row) {
            // Skip if already initialized
            if (row.getAttribute('data-draggable') === 'true') {
                return;
            }
            
            // Mark as initialized
            row.setAttribute('data-draggable', 'true');
            row.setAttribute('draggable', 'true');
            
            // Get the controller from Angular
            var scope = angular.element(row).scope();
            var ctrl = scope.ctrl;
            
            // Set up drag events
            row.addEventListener('dragstart', function(e) {
                // Store the source index in the dataTransfer object
                var sourceIndex = scope.$index;
                e.dataTransfer.setData('text/plain', sourceIndex);
                e.dataTransfer.effectAllowed = 'move';
                row.classList.add('dragging');
            });
            
            row.addEventListener('dragover', function(e) {
                e.preventDefault(); // Allow drop
                e.dataTransfer.dropEffect = 'move';
            });
            
            row.addEventListener('dragenter', function(e) {
                row.classList.add('drag-over');
            });
            
            row.addEventListener('dragleave', function(e) {
                row.classList.remove('drag-over');
            });
            
            row.addEventListener('drop', function(e) {
                e.preventDefault();
                e.stopPropagation();
                
                // Get the source index from the dataTransfer object
                var sourceIndex = parseInt(e.dataTransfer.getData('text/plain'));
                var targetIndex = scope.$index;
                
                // Only reorder if source and target are different
                if (sourceIndex !== targetIndex) {
                    scope.$apply(function() {
                        // Move the item in the array
                        var movedGame = ctrl.games.splice(sourceIndex, 1)[0];
                        ctrl.games.splice(targetIndex, 0, movedGame);
                        
                        // Recalculate all rating changes
                        ctrl.calculateAllRatingChanges();
                    });
                }
                
                row.classList.remove('drag-over');
            });
            
            row.addEventListener('dragend', function() {
                // Remove drag styles
                row.classList.remove('dragging');
                document.querySelectorAll('.drag-over').forEach(function(el) {
                    el.classList.remove('drag-over');
                });
            });
        });
    }
    
    // Set up a mutation observer to detect when new rows are added
    function observeDOMChanges() {
        // Create an observer instance
        var observer = new MutationObserver(function(mutations) {
            // Re-initialize drag and drop when DOM changes
            initDragAndDrop();
        });
        
        // Observe the table body for changes to its children
        var tableBody = document.querySelector('tbody');
        if (tableBody) {
            observer.observe(tableBody, { childList: true });
        }
    }
    
    // Set up the observer after DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(observeDOMChanges, 1000);
    });
})();