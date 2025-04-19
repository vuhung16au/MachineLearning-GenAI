// Fibonacci spiral visualization

document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('spiral-canvas');
    const ctx = canvas.getContext('2d');
    const animateButton = document.getElementById('animate-spiral');
    const resetButton = document.getElementById('reset-spiral');
    
    let animationId = null;
    let isAnimating = false;
    
    // Fibonacci function (optimized)
    function fibonacci(n) {
        if (n <= 0) return 0;
        if (n === 1) return 1;
        
        let a = 0, b = 1;
        for (let i = 2; i <= n; i++) {
            const temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
    
    // Function to draw the Fibonacci spiral
    function drawFibonacciSpiral(iterations = 7, animate = false, step = 0) {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set drawing styles
        ctx.lineWidth = 2;
        ctx.strokeStyle = '#2c3e50';
        ctx.fillStyle = 'rgba(52, 152, 219, 0.1)';
        
        // Calculate scale factor to fit the canvas
        const maxFib = fibonacci(iterations);
        const scale = Math.min(canvas.width, canvas.height) / (maxFib * 2.5);
        
        // Start at the center of the canvas
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        
        // Draw sequence
        let x = centerX;
        let y = centerY;
        let angle = 0;
        
        // Draw the visual representation of the first few Fibonacci numbers
        ctx.font = '14px Arial';
        ctx.fillStyle = '#333';
        ctx.textAlign = 'center';
        
        // Limit animation to the current step
        const maxIterationsToDraw = animate ? Math.min(step, iterations) : iterations;
        
        // Draw spiral
        for (let i = 1; i <= maxIterationsToDraw; i++) {
            const prevFib = fibonacci(i - 1);
            const currentFib = fibonacci(i);
            const squareSize = currentFib * scale;
            
            // Determine position based on the current angle
            let squareX, squareY;
            
            // Position squares based on the spiral's angle
            switch ((i - 1) % 4) {
                case 0: // Right and up
                    squareX = x;
                    squareY = y - squareSize;
                    x = squareX;
                    y = squareY;
                    break;
                case 1: // Right and down
                    squareX = x;
                    squareY = y;
                    x = squareX + squareSize;
                    y = squareY;
                    break;
                case 2: // Left and down
                    squareX = x - squareSize;
                    squareY = y;
                    x = squareX;
                    y = squareY + squareSize;
                    break;
                case 3: // Left and up
                    squareX = x - squareSize;
                    squareY = y - squareSize;
                    x = squareX;
                    y = squareY;
                    break;
            }
            
            // Draw square
            ctx.beginPath();
            ctx.rect(squareX, squareY, squareSize, squareSize);
            ctx.strokeStyle = `hsl(${i * 20 % 360}, 70%, 50%)`;
            ctx.stroke();
            
            // Label with Fibonacci number
            if (currentFib < 1000) {
                ctx.fillText(currentFib.toString(), 
                    squareX + squareSize / 2, 
                    squareY + squareSize / 2);
            }
            
            // Draw arc (quarter circle) within each square to form the spiral
            ctx.beginPath();
            let arcX, arcY, startAngle, endAngle;
            
            switch ((i - 1) % 4) {
                case 0: // Top-right corner
                    arcX = squareX + squareSize;
                    arcY = squareY + squareSize;
                    startAngle = Math.PI;
                    endAngle = 3 * Math.PI / 2;
                    break;
                case 1: // Bottom-right corner
                    arcX = squareX;
                    arcY = squareY + squareSize;
                    startAngle = 3 * Math.PI / 2;
                    endAngle = 0;
                    break;
                case 2: // Bottom-left corner
                    arcX = squareX;
                    arcY = squareY;
                    startAngle = 0;
                    endAngle = Math.PI / 2;
                    break;
                case 3: // Top-left corner
                    arcX = squareX + squareSize;
                    arcY = squareY;
                    startAngle = Math.PI / 2;
                    endAngle = Math.PI;
                    break;
            }
            
            ctx.arc(arcX, arcY, squareSize, startAngle, endAngle, false);
            ctx.strokeStyle = '#e74c3c';
            ctx.lineWidth = 3;
            ctx.stroke();
            ctx.lineWidth = 2;
        }
        
        // Add description text
        ctx.fillStyle = '#333';
        ctx.font = '16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Fibonacci Spiral Visualization', canvas.width/2, 30);
        ctx.font = '14px Arial';
        ctx.fillText('Each square has a side length equal to a Fibonacci number', canvas.width/2, canvas.height - 20);
    }
    
    // Function to reset the animation
    function resetSpiral() {
        if (animationId) {
            cancelAnimationFrame(animationId);
            animationId = null;
        }
        isAnimating = false;
        drawFibonacciSpiral(6, false); // Match with maxSteps value
    }
    
    // Function to animate the spiral
    function animateSpiral() {
        if (isAnimating) return;
        
        isAnimating = true;
        let step = 1;
        const maxSteps = 15; // Increase maximum steps for a fuller spiral
        
        function animate() {
            drawFibonacciSpiral(maxSteps, true, step);
            
            if (step < maxSteps) {
                step++;
                // Add delay for smoother animation
                setTimeout(() => {
                    animationId = requestAnimationFrame(animate);
                }, 200); // 200ms delay between frames
            } else {
                isAnimating = false;
            }
        }
        
        animationId = requestAnimationFrame(animate);
    }
    
    // Initial drawing
    resetSpiral();
    
    // Event listeners
    animateButton.addEventListener('click', animateSpiral);
    resetButton.addEventListener('click', resetSpiral);
});
