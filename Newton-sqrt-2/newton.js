// Constants
const SQRT2 = Math.sqrt(2);
const TOLERANCE = 1e-10;
const MAX_ITERATIONS = 10;

// DOM Elements
const canvas = document.getElementById('graph');
const ctx = canvas.getContext('2d');
const initialGuessInput = document.getElementById('initialGuess');
const resetButton = document.getElementById('reset');
const nextIterationButton = document.getElementById('nextIteration');
const runAllButton = document.getElementById('runAll');
const tableBody = document.getElementById('tableBody');
const currentApproximation = document.getElementById('currentApproximation');

// State variables
let iterations = [];
let currentIteration = 0;
let animationId = null;

// Newton's method function for calculating sqrt(2)
function newtonSqrt2(x) {
    return x - (x * x - 2) / (2 * x);
}

// Initialize the visualization
function initialize() {
    // Clear any previous state
    iterations = [];
    currentIteration = 0;
    
    // Clear the table
    tableBody.innerHTML = '';
    currentApproximation.textContent = '-';
    
    // Get initial guess
    const x0 = parseFloat(initialGuessInput.value);
    iterations.push({
        n: 0,
        x: x0,
        fx: x0 * x0 - 2,
        error: Math.abs(x0 - SQRT2)
    });
    
    // Add initial row to table
    addIterationToTable(iterations[0]);
    
    // Draw the graph
    drawGraph();
    
    // Update current approximation
    updateCurrentApproximation();
}

// Perform the next iteration
function nextIteration() {
    if (currentIteration >= MAX_ITERATIONS) return;
    
    const prev = iterations[currentIteration];
    const nextX = newtonSqrt2(prev.x);
    
    currentIteration++;
    
    const next = {
        n: currentIteration,
        x: nextX,
        fx: nextX * nextX - 2,
        error: Math.abs(nextX - SQRT2)
    };
    
    iterations.push(next);
    addIterationToTable(next);
    drawGraph();
    updateCurrentApproximation();
    
    // Check if we've converged
    if (next.error < TOLERANCE) {
        nextIterationButton.disabled = true;
        runAllButton.disabled = true;
    }
}

// Run all iterations until convergence
function runAllIterations() {
    if (animationId) {
        cancelAnimationFrame(animationId);
    }
    
    function step() {
        if (currentIteration < MAX_ITERATIONS && iterations[currentIteration].error >= TOLERANCE) {
            nextIteration();
            animationId = requestAnimationFrame(step);
        } else {
            animationId = null;
        }
    }
    
    animationId = requestAnimationFrame(step);
}

// Add an iteration to the results table
function addIterationToTable(iteration) {
    const row = document.createElement('tr');
    
    const iterationCell = document.createElement('td');
    iterationCell.textContent = iteration.n;
    row.appendChild(iterationCell);
    
    const xCell = document.createElement('td');
    xCell.textContent = iteration.x.toFixed(10);
    row.appendChild(xCell);
    
    const fxCell = document.createElement('td');
    fxCell.textContent = iteration.fx.toFixed(10);
    row.appendChild(fxCell);
    
    const errorCell = document.createElement('td');
    errorCell.textContent = iteration.error.toFixed(10);
    row.appendChild(errorCell);
    
    tableBody.appendChild(row);
}

// Update the current approximation display
function updateCurrentApproximation() {
    if (iterations.length > 0) {
        const current = iterations[currentIteration];
        currentApproximation.textContent = current.x.toFixed(10);
    }
}

// Draw the graph visualization
function drawGraph() {
    const width = canvas.width;
    const height = canvas.height;
    
    // Clear canvas
    ctx.clearRect(0, 0, width, height);
    
    // Draw coordinate system
    ctx.strokeStyle = '#ccc';
    ctx.lineWidth = 1;
    
    // Draw x-axis
    ctx.beginPath();
    ctx.moveTo(0, height / 2);
    ctx.lineTo(width, height / 2);
    ctx.stroke();
    
    // Draw y-axis
    ctx.beginPath();
    ctx.moveTo(width / 4, 0);
    ctx.lineTo(width / 4, height);
    ctx.stroke();
    
    // Scale factors
    const scaleX = 100;
    const scaleY = 100;
    const offsetX = width / 4;
    const offsetY = height / 2;
    
    // Plot f(x) = x^2 - 2
    ctx.strokeStyle = '#3498db';
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    for (let px = 0; px < width; px++) {
        const x = (px - offsetX) / scaleX;
        const y = x * x - 2;
        const py = offsetY - y * scaleY;
        
        if (px === 0) {
            ctx.moveTo(px, py);
        } else {
            ctx.lineTo(px, py);
        }
    }
    ctx.stroke();
    
    // Plot the line x = sqrt(2)
    ctx.strokeStyle = '#2ecc71';
    ctx.lineWidth = 1;
    ctx.beginPath();
    const sqrtX = offsetX + SQRT2 * scaleX;
    ctx.moveTo(sqrtX, 0);
    ctx.lineTo(sqrtX, height);
    ctx.stroke();
    
    // Plot iterations
    for (let i = 0; i <= currentIteration; i++) {
        const iter = iterations[i];
        const px = offsetX + iter.x * scaleX;
        const py = offsetY - iter.fx * scaleY;
        
        // Draw point
        ctx.fillStyle = i === currentIteration ? '#e74c3c' : '#3498db';
        ctx.beginPath();
        ctx.arc(px, py, 5, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw tangent line if not last iteration
        if (i < currentIteration) {
            const nextIter = iterations[i + 1];
            const nextPx = offsetX + nextIter.x * scaleX;
            
            // Derive and plot tangent line
            const derivative = 2 * iter.x;
            ctx.strokeStyle = '#f39c12';
            ctx.lineWidth = 1;
            ctx.beginPath();
            
            // Extend tangent line
            const extensionX = 50;
            ctx.moveTo(px - extensionX, py - derivative * (-extensionX));
            ctx.lineTo(px + extensionX, py - derivative * extensionX);
            ctx.stroke();
            
            // Draw line to x-axis
            ctx.strokeStyle = '#e74c3c';
            ctx.beginPath();
            ctx.moveTo(px, py);
            ctx.lineTo(nextPx, offsetY);
            ctx.stroke();
        }
    }
    
    // Add labels
    ctx.fillStyle = '#333';
    ctx.font = '12px Arial';
    ctx.fillText('0', offsetX - 15, offsetY + 15);
    ctx.fillText('f(x) = x² - 2', width - 100, 20);
    ctx.fillText('x = √2', sqrtX + 5, 20);
    
    // Label axes
    ctx.fillText('x', width - 10, offsetY + 15);
    ctx.fillText('y', offsetX - 15, 10);
}

// Event listeners
resetButton.addEventListener('click', initialize);
nextIterationButton.addEventListener('click', nextIteration);
runAllButton.addEventListener('click', runAllIterations);

// Initialize on load
window.addEventListener('load', initialize);
