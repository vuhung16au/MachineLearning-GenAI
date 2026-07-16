// Simplify initialization to avoid potential timing issues
document.addEventListener('DOMContentLoaded', initAnimation);

// Track if the animation has already started
let animationStarted = false;
let calculationRunning = false;

function initAnimation() {
    // Prevent running the initialization twice
    if (animationStarted) return;
    animationStarted = true;
    
    console.log('Animation initialization started');
    
    const canvas = document.getElementById('integralCanvas');
    if (!canvas) {
        console.error('Canvas element not found');
        document.body.innerHTML += '<p style="color:red">Error: Canvas element not found</p>';
        return;
    }
    
    const ctx = canvas.getContext('2d');
    if (!ctx) {
        console.error('Could not get canvas context');
        document.body.innerHTML += '<p style="color:red">Error: Could not get canvas context</p>';
        return;
    }
    
    const infoDiv = document.getElementById('info');
    if (!infoDiv) {
        console.error('Info div not found');
        document.body.innerHTML += '<p style="color:red">Error: Info div not found</p>';
        return;
    }
    
    const startButton = document.getElementById('startButton');
    if (!startButton) {
        console.error('Start button not found');
        document.body.innerHTML += '<p style="color:red">Error: Start button not found</p>';
        return;
    }
    
    const stopButton = document.getElementById('stopButton');
    if (!stopButton) {
        console.error('Stop button not found');
        document.body.innerHTML += '<p style="color:red">Error: Stop button not found</p>';
        return;
    }
    
    const resetButton = document.getElementById('resetButton');
    if (!resetButton) {
        console.error('Reset button not found');
        document.body.innerHTML += '<p style="color:red">Error: Reset button not found</p>';
        return;
    }
    
    const errorThresholdInput = document.getElementById('errorThreshold');
    if (!errorThresholdInput) {
        console.error('Error threshold input not found');
        document.body.innerHTML += '<p style="color:red">Error: Error threshold input not found</p>';
        return;
    }
    
    const maxIterationsInput = document.getElementById('maxIterations');
    if (!maxIterationsInput) {
        console.error('Max iterations input not found');
        document.body.innerHTML += '<p style="color:red">Error: Max iterations input not found</p>';
        return;
    }

    // Constants for the calculation
    const a = 0;
    const b = 1;
    const defaultMaxIterations = 200;
    let currentFrame = 0;
    let exactValue; // Will be calculated based on current function when possible
    const defaultErrorThreshold = 0.01;
    
    // Variables for timing
    let startTime = 0;
    let elapsedTimeInterval;
    let isPaused = false;
    let animationTimeout = null;
    
    // Function definition (fixed to x^2 since we removed the input)
    let currentFunctionText = 'x^2';
    let currentFunction;
    
    function parseFunction(expression) {
        const trimmed = expression.trim();
        // Safe function lookup — no dynamic code execution
        const safeFuncs = {
            'x^2':  x => x * x,
            'x^3':  x => x * x * x,
            'x^4':  x => { const x2 = x * x; return x2 * x2; },
            'x':    x => x,
            'x^2 + 1': x => x * x + 1,
            'x^3 + 1': x => x * x * x + 1,
            '1':    () => 1,
            '2':    () => 2,
        };
        if (safeFuncs[trimmed]) return safeFuncs[trimmed];
        // For other simple polynomial patterns: x^n
        const powMatch = trimmed.match(/^x\^(\d+)$/);
        if (powMatch) {
            const n = parseInt(powMatch[1], 10);
            if (n >= 0 && n <= 10) return x => Math.pow(x, n);
        }
        console.warn('Unsupported expression, using x^2 as fallback:', trimmed);
        return function(x) { return x * x; };
    }
    
    // Try to calculate exact value for common functions
    function calculateExactValue(funcText) {
        // For x^2 from 0 to 1, the exact value is 1/3
        if (funcText.trim() === 'x^2') return 1/3;
        // For x^3 from 0 to 1, the exact value is 1/4
        if (funcText.trim() === 'x^3') return 1/4;
        // For x from 0 to 1, the exact value is 1/2
        if (funcText.trim() === 'x') return 1/2;
        // For constant 1 from 0 to 1, the exact value is 1
        if (funcText.trim() === '1') return 1;
        
        // For other functions, use numerical approximation
        // This is a simple approximation and might not be accurate for all functions
        return numericalIntegration(parseFunction(funcText), a, b, 1000);
    }
    
    // Simple numerical integration using trapezoidal rule
    function numericalIntegration(func, a, b, n) {
        const h = (b - a) / n;
        let sum = 0.5 * (func(a) + func(b));
        
        for (let i = 1; i < n; i++) {
            sum += func(a + i * h);
        }
        
        return sum * h;
    }
    
    // Initialize current function and exact value
    currentFunction = parseFunction(currentFunctionText);
    exactValue = calculateExactValue(currentFunctionText);
    
    // Function to use in calculation
    function f(x) {
        try {
            return currentFunction(x);
        } catch (error) {
            console.error('Error evaluating function:', error);
            return x * x; // Fallback to x^2
        }
    }
    
    // Remove the event listener for function input since it no longer exists
    
    // Set default values for inputs
    errorThresholdInput.value = defaultErrorThreshold;
    maxIterationsInput.value = defaultMaxIterations;

    // Initial canvas setup - draw the function right away
    clearAndDrawAxesFunction();
    
    function clearAndDrawAxesFunction() {
        // Clear the canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw axes
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(canvas.width - 50, canvas.height - 50);  // X-axis
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(50, 50);  // Y-axis
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Label the axes
        ctx.fillStyle = 'black';
        ctx.font = '14px Arial';
        ctx.fillText('x', canvas.width - 40, canvas.height - 30);
        ctx.fillText('y', 30, 60);
        
        // Draw the current function
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        for (let i = 0; i <= 100; i++) {
            const x = a + (b - a) * i / 100;
            const y = f(x);
            const canvasX = 50 + x * (canvas.width - 100);
            const canvasY = canvas.height - 50 - y * (canvas.height - 100);
            if (i === 0) {
                ctx.moveTo(canvasX, canvasY);
            } else {
                ctx.lineTo(canvasX, canvasY);
            }
        }
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Label the function
        ctx.fillStyle = 'red';
        ctx.fillText(`f(x) = ${currentFunctionText}`, canvas.width - 150, 70);
    }

    function updateElapsedTime() {
        if (!calculationRunning || isPaused) return;
        
        const currentTime = new Date().getTime();
        const elapsedMs = currentTime - startTime;
        const seconds = Math.floor(elapsedMs / 1000);
        const milliseconds = elapsedMs % 1000;
        
        document.getElementById('elapsedTime').textContent = 
            `${seconds}.${milliseconds.toString().padStart(3, '0')}s`;
    }

    function startTimer() {
        startTime = new Date().getTime();
        // Update the timer every 50ms for smoother display
        elapsedTimeInterval = setInterval(updateElapsedTime, 50);
    }

    function stopTimer() {
        if (elapsedTimeInterval) {
            clearInterval(elapsedTimeInterval);
            elapsedTimeInterval = null;
        }
    }

    // Function to format the exact value display
    function formatExactValue(value) {
        if (currentFunctionText.trim() === 'x^2') {
            return "1/3 = " + value.toFixed(6);
        }
        if (currentFunctionText.trim() === 'x^3') {
            return "1/4 = " + value.toFixed(6);
        }
        if (currentFunctionText.trim() === 'x') {
            return "1/2 = " + value.toFixed(6);
        }
        if (currentFunctionText.trim() === '1') {
            return "1 = " + value.toFixed(6);
        }
        // For other functions, just show the numerical value
        return value.toFixed(6);
    }

    function drawFrame() {
        if (!calculationRunning || isPaused) return;
        
        const n = currentFrame + 1;
        const deltaX = (b - a) / n;
        let sumArea = 0;

        // Clear and redraw axes and function
        clearAndDrawAxesFunction();

        // Draw Riemann rectangles
        ctx.fillStyle = 'rgba(0, 0, 255, 0.3)';
        ctx.strokeStyle = 'blue';
        ctx.lineWidth = 0.5;

        for (let i = 1; i <= n; i++) {
            const xRight = a + i * deltaX;
            const yRight = f(xRight);
            const x1Canvas = 50 + (xRight - deltaX) * (canvas.width - 100);
            const y1Canvas = canvas.height - 50;
            const x2Canvas = 50 + xRight * (canvas.width - 100);
            const y2Canvas = canvas.height - 50 - yRight * (canvas.height - 100);

            ctx.fillRect(x1Canvas, y2Canvas, (x2Canvas - x1Canvas), (y1Canvas - y2Canvas));
            ctx.strokeRect(x1Canvas, y2Canvas, (x2Canvas - x1Canvas), (y1Canvas - y2Canvas));
            sumArea += yRight * deltaX;
        }

        // Calculate error
        const error = Math.abs(sumArea - exactValue);
        
        // Display results in a table
        infoDiv.innerHTML = `
            <table border="1" style="border-collapse: collapse; margin-top: 10px; width: 100%;">
                <tr>
                    <th style="padding: 5px;">Rectangles (n)</th>
                    <th style="padding: 5px; background-color: #FFFF99;">Riemann Sum</th>
                    <th style="padding: 5px; color: red;">Error</th>
                    <th style="padding: 5px;">Exact/Approx. Value</th>
                    <th style="padding: 5px;">Elapsed Time</th>
                </tr>
                <tr>
                    <td style="padding: 5px; text-align: center;">${n}</td>
                    <td style="padding: 5px; text-align: center; background-color: #FFFF99;">${sumArea.toFixed(6)}</td>
                    <td style="padding: 5px; text-align: center; color: red;">${error.toFixed(6)}</td>
                    <td style="padding: 5px; text-align: center;">${formatExactValue(exactValue)}</td>
                    <td style="padding: 5px; text-align: center;" id="elapsedTime">0.000s</td>
                </tr>
            </table>
        `;
        
        // Update the elapsed time immediately after creating the table
        updateElapsedTime();
        
        console.log(`Frame ${currentFrame}: n=${n}, area=${sumArea.toFixed(4)}, error=${error.toFixed(4)}`);

        currentFrame++;
        
        // Get the current error threshold and max iterations from inputs
        const errorThreshold = parseFloat(errorThresholdInput.value) || defaultErrorThreshold;
        const maxIterations = parseInt(maxIterationsInput.value) || defaultMaxIterations;
        
        // Check both stopping conditions: error threshold and max iterations
        if (currentFrame < maxIterations && error >= errorThreshold) {
            animationTimeout = setTimeout(drawFrame, 50);
        } else {
            // We reached either error threshold or max iterations
            let stopReason = "";
            if (error < errorThreshold) {
                stopReason = "Error threshold reached";
            } else {
                stopReason = "Maximum iterations reached";
            }
            console.log(`Calculation completed: ${stopReason}`);
            
            updateElapsedTime(); // One final update
            stopTimer();
            
            calculationRunning = false;
            startButton.textContent = "Start calculation";
            startButton.disabled = false;
            stopButton.disabled = true;
            resetButton.disabled = false;
        }
    }

    // Button click event handlers
    startButton.addEventListener('click', function() {
        console.log("Button clicked");
        if (calculationRunning) {
            console.log("Calculation already running, ignoring click");
            return;
        }
        
        // Validate inputs
        const errorThreshold = parseFloat(errorThresholdInput.value);
        if (isNaN(errorThreshold) || errorThreshold <= 0 || errorThreshold >= 1) {
            alert("Please enter a valid error threshold between 0 and 1");
            errorThresholdInput.value = defaultErrorThreshold;
            return;
        }
        
        const maxIterations = parseInt(maxIterationsInput.value);
        if (isNaN(maxIterations) || maxIterations < 1 || maxIterations > 1000) {
            alert("Please enter a valid max iterations value between 1 and 1000");
            maxIterationsInput.value = defaultMaxIterations;
            return;
        }
        
        console.log(`Starting new calculation with error threshold: ${errorThreshold}, max iterations: ${maxIterations}`);
        calculationRunning = true;
        isPaused = false;
        currentFrame = 0;
        startButton.textContent = "Calculating...";
        startButton.disabled = true;
        stopButton.disabled = false;
        resetButton.disabled = true;
        
        // Initialize the info div with an empty table
        infoDiv.innerHTML = `
            <table border="1" style="border-collapse: collapse; margin-top: 10px; width: 100%;">
                <tr>
                    <th style="padding: 5px;">Rectangles (n)</th>
                    <th style="padding: 5px; background-color: #FFFF99;">Riemann Sum</th>
                    <th style="padding: 5px; color: red;">Error</th>
                    <th style="padding: 5px;">Exact/Approx. Value</th>
                    <th style="padding: 5px;">Elapsed Time</th>
                </tr>
                <tr>
                    <td style="padding: 5px; text-align: center;" colspan="5">Calculation in progress...</td>
                </tr>
            </table>
        `;
        
        // Start the timer
        startTimer();
        
        // Start the animation immediately
        drawFrame();
    });
    
    // Stop button click event handler
    stopButton.addEventListener('click', function() {
        if (!calculationRunning || isPaused) return;
        
        console.log("Stopping calculation");
        isPaused = true;
        
        // Clear the animation timeout
        if (animationTimeout) {
            clearTimeout(animationTimeout);
            animationTimeout = null;
        }
        
        // Stop the timer
        stopTimer();
        
        // Update button states
        startButton.textContent = "Resume";
        startButton.disabled = false;
        stopButton.disabled = true;
        resetButton.disabled = false;
    });
    
    // Reset button click event handler
    resetButton.addEventListener('click', function() {
        console.log("Resetting calculation");
        
        // Clear any existing timeout
        if (animationTimeout) {
            clearTimeout(animationTimeout);
            animationTimeout = null;
        }
        
        // Stop the timer
        stopTimer();
        
        // Reset all variables
        calculationRunning = false;
        isPaused = false;
        currentFrame = 0;
        
        // Reset UI
        clearAndDrawAxesFunction();
        startButton.textContent = "Start calculation";
        startButton.disabled = false;
        stopButton.disabled = true;
        resetButton.disabled = true;
        
        // Initialize the info div with an empty table
        infoDiv.innerHTML = `
            <table border="1" style="border-collapse: collapse; margin-top: 10px; width: 100%;">
                <tr>
                    <th style="padding: 5px;">Rectangles (n)</th>
                    <th style="padding: 5px; background-color: #FFFF99;">Riemann Sum</th>
                    <th style="padding: 5px; color: red;">Error</th>
                    <th style="padding: 5px;">Exact/Approx. Value</th>
                    <th style="padding: 5px;">Elapsed Time</th>
                </tr>
                <tr>
                    <td style="padding: 5px; text-align: center;">${0}</td>
                    <td style="padding: 5px; text-align: center; background-color: #FFFF99;">0.0000</td>
                    <td style="padding: 5px; text-align: center; color: red;">${exactValue.toFixed(6)}</td>
                    <td style="padding: 5px; text-align: center;">${formatExactValue(exactValue)}</td>
                    <td style="padding: 5px; text-align: center;" id="elapsedTime">0.000s</td>
                </tr>
            </table>
        `;
    });
    
    // Auto-start the calculation when the page loads
    console.log("Auto-starting calculation");
    calculationRunning = true;
    isPaused = false;
    currentFrame = 0;
    startButton.textContent = "Calculating...";
    startButton.disabled = true;
    stopButton.disabled = false;
    resetButton.disabled = true;
    
    // Initialize the info div with an empty table
    infoDiv.innerHTML = `
        <table border="1" style="border-collapse: collapse; margin-top: 10px; width: 100%;">
            <tr>
                <th style="padding: 5px;">Rectangles (n)</th>
                <th style="padding: 5px; background-color: #FFFF99;">Riemann Sum</th>
                <th style="padding: 5px; color: red;">Error</th>
                <th style="padding: 5px;">Exact/Approx. Value</th>
                <th style="padding: 5px;">Elapsed Time</th>
            </tr>
            <tr>
                <td style="padding: 5px; text-align: center;" colspan="5">Calculation in progress...</td>
            </tr>
        </table>
    `;

    startTimer();    // Start the timer for auto-start        
    drawFrame();
    
    console.log("Initialization complete - ready for calculation");
}