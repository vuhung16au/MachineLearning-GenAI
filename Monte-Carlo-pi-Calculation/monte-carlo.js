document.addEventListener('DOMContentLoaded', function() {
    // Get canvas and context
    const canvas = document.getElementById('simulationCanvas');
    const ctx = canvas.getContext('2d');
    
    // Set up constants
    const canvasSize = canvas.width;
    const centerX = canvasSize / 2;
    const centerY = canvasSize / 2;
    
    // Variables for tracking simulation
    let pointsInside = 0;
    let totalPoints = 0;
    let piEstimate = 0;
    let error = 1.0;
    let errorThreshold = 0.0001; // Default, will be adjustable
    const actualPi = Math.PI;
    let startTime;
    let endTime;
    let isRunning = false;
    
    // DOM elements for stats and point information
    const pointsInsideElement = document.getElementById('pointsInside');
    const totalPointsElement = document.getElementById('totalPoints');
    const piEstimateElement = document.getElementById('piEstimate');
    const piErrorElement = document.getElementById('piError');
    const iterationsElement = document.getElementById('iterations');
    const actualPiElement = document.getElementById('actualPi');
    const elapsedTimeElement = document.getElementById('elapsedTime');
    
    // DOM elements for current point information
    const pointXElement = document.getElementById('pointX');
    const pointYElement = document.getElementById('pointY');
    const pointDistanceElement = document.getElementById('pointDistance');
    const pointStatusElement = document.getElementById('pointStatus');
    
    // DOM elements for controls
    const errorThresholdInput = document.getElementById('errorThreshold');
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    
    // Update actual Pi value with blue color
    actualPiElement.innerHTML = `<span style="color: #0066cc; font-weight: bold;">${actualPi.toFixed(8)}</span>`;
    
    // Set default error threshold
    errorThreshold = 0.001;
    errorThresholdInput.value = '0.001';
    
    // Initialize canvas
    initCanvas();
    
    // Auto-start the simulation when page loads
    setTimeout(() => {
        startSimulation();
    }, 500); // Small delay to ensure everything is rendered
    
    // Add event listener for start button
    startButton.addEventListener('click', function() {
        // Get user-defined error threshold
        const userThreshold = parseFloat(errorThresholdInput.value);
        
        // Validate threshold
        if (isNaN(userThreshold) || userThreshold <= 0 || userThreshold > 1) {
            alert('Please enter a valid threshold between 0 and 1');
            errorThresholdInput.value = '0.0001';
            return;
        }
        
        // Stop any running simulation
        isRunning = false;
        
        // Reset simulation
        resetSimulation();
        
        // Set the new threshold
        errorThreshold = userThreshold;
        
        // Start simulation
        startSimulation();
    });
    
    // Add event listener for stop button
    stopButton.addEventListener('click', function() {
        stopSimulation();
    });
    
    function stopSimulation() {
        if (isRunning) {
            isRunning = false;
            
            // Calculate elapsed time
            endTime = performance.now();
            const elapsedSeconds = ((endTime - startTime) / 1000).toFixed(2);
            
            console.log("Simulation stopped by user.");
            // Update elapsed time display
            elapsedTimeElement.textContent = elapsedSeconds + " seconds";
            
            // Mark that the simulation was stopped
            ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
            ctx.fillRect(centerX - 150, centerY - 15, 300, 30);
            ctx.fillStyle = 'white';
            ctx.font = '16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`Simulation stopped! Elapsed time: ${elapsedSeconds}s`, centerX, centerY);
        }
    }
    
    function resetSimulation() {
        // Reset counters
        pointsInside = 0;
        totalPoints = 0;
        piEstimate = 0;
        error = 1.0;
        
        // Clear canvas
        initCanvas();
        
        // Reset displays
        updateStats();
        updatePointInfo(0, 0, 0, false);
        elapsedTimeElement.textContent = "calculating...";
    }
    
    function startSimulation() {
        if (!isRunning) {
            isRunning = true;
            startTime = performance.now();
            animate();
        }
    }
    
    function initCanvas() {
        // Clear canvas
        ctx.clearRect(0, 0, canvasSize, canvasSize);
        
        // Draw square
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.strokeRect(0, 0, canvasSize, canvasSize);
        
        // Draw circle with radius exactly half of canvas size
        ctx.beginPath();
        ctx.arc(centerX, centerY, centerX, 0, 2 * Math.PI);
        ctx.strokeStyle = '#0066cc';
        ctx.stroke();
        
        // Draw radius line
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(centerX + centerX, centerY); // Draw to right edge of circle
        ctx.strokeStyle = '#0066cc';
        ctx.setLineDash([5, 3]); // Dashed line
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.setLineDash([]); // Reset dash
        
        // Add radius label
        ctx.fillStyle = '#0066cc';
        ctx.font = '14px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(`r = ${centerX}`, centerX + centerX/2, centerY - 10);
        
        // Add coordinate system indicators
        drawCoordinateSystem();
    }
    
    function drawCoordinateSystem() {
        // Draw faint coordinate axes
        ctx.beginPath();
        ctx.moveTo(centerX, 0);
        ctx.lineTo(centerX, canvasSize);
        ctx.moveTo(0, centerY);
        ctx.lineTo(canvasSize, centerY);
        ctx.strokeStyle = 'rgba(0, 0, 0, 0.1)';
        ctx.stroke();
    }
    
    // Generate and process a single point
    function processPoint() {
        // Generate random coordinates
        const x = Math.random() * canvasSize;
        const y = Math.random() * canvasSize;
        
        // Calculate distance from center
        const dx = x - centerX;
        const dy = y - centerY;
        const distanceSquared = dx * dx + dy * dy;
        const distance = Math.sqrt(distanceSquared);
        
        // Check if point is inside circle
        const isInside = distanceSquared <= centerX * centerX;
        
        // Update point information display
        updatePointInfo(x, y, distance, isInside);
        
        // Draw the point
        drawPoint(x, y, isInside);
        
        // Update counters
        totalPoints++;
        if (isInside) {
            pointsInside++;
        }
        
        // Calculate pi estimate: (points inside / total points) * 4
        piEstimate = (pointsInside / totalPoints) * 4;
        error = Math.abs(piEstimate - actualPi);
        
        // Update stats display
        updateStats();
        
        return error < errorThreshold;
    }
    
    // Update the point information display
    function updatePointInfo(x, y, distance, isInside) {
        pointXElement.textContent = x.toFixed(2);
        pointYElement.textContent = y.toFixed(2);
        pointDistanceElement.textContent = distance.toFixed(2);
        
        if (isInside) {
            pointStatusElement.innerHTML = '<span style="color: #00cc66; font-weight: bold;">🟢</span>';
        } else {
            pointStatusElement.innerHTML = '<span style="color: #ff3366; font-weight: bold;">🔴</span>';
        }
    }
    
    // Draw a single point on the canvas
    function drawPoint(x, y, isInside) {
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, 2 * Math.PI);
        ctx.fillStyle = isInside ? '#00cc66' : '#ff3366';
        ctx.fill();
    }
    
    // Update statistics display with colored values
    function updateStats() {
        pointsInsideElement.textContent = pointsInside.toLocaleString();
        totalPointsElement.textContent = totalPoints.toLocaleString();
        
        // Show estimated pi in green
        piEstimateElement.innerHTML = `<span style="color: #008800; font-weight: bold;">${piEstimate.toFixed(8)}</span>`;
        
        // Show error in red
        piErrorElement.innerHTML = `<span style="color: #cc0000; font-weight: bold;">${error.toFixed(8)}</span>`;
        
        // Update iterations (same as total points)
        iterationsElement.textContent = totalPoints.toLocaleString();
    }
    
    // Animation loop
    function animate() {
        // Process a single point
        let shouldStop = processPoint();
        
        if (!shouldStop && isRunning) {
            requestAnimationFrame(animate);
        } else {
            isRunning = false;
            
            // Calculate elapsed time
            endTime = performance.now();
            const elapsedSeconds = ((endTime - startTime) / 1000).toFixed(2);
            
            console.log("Simulation complete. Error threshold reached.");
            // Update elapsed time display
            elapsedTimeElement.textContent = elapsedSeconds + " seconds";
            
            // Mark that the simulation is complete
            ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
            ctx.fillRect(centerX - 150, centerY - 15, 300, 30);
            ctx.fillStyle = 'white';
            ctx.font = '16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`Complete! Error < ${errorThreshold} in ${elapsedSeconds}s`, centerX, centerY);
        }
    }
    
    // Start with initial canvas setup but don't start animation yet
    // User must click Start button to begin
});
