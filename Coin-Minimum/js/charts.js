// Chart creation functions
function createRuntimeChart(canvasId, title, amounts, data) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    // Define colors for different algorithms
    const colors = {
        'Memoized DP (Recursive)': 'rgb(255, 99, 132)',
        'Memoized DP (Iterative)': 'rgb(54, 162, 235)',
        'Bottom-Up DP': 'rgb(255, 206, 86)',
        'Greedy': 'rgb(75, 192, 192)'
    };
    
    // Prepare datasets
    const datasets = [];
    for (const [algorithm, runtimes] of Object.entries(data)) {
        datasets.push({
            label: algorithm,
            data: runtimes,
            borderColor: colors[algorithm],
            backgroundColor: colors[algorithm] + '20',
            borderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 7,
            fill: false
        });
    }
    
    // Create chart
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: amounts,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: title,
                    font: {
                        size: 16
                    }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                },
                legend: {
                    position: 'bottom'
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Amount'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Runtime (seconds)'
                    },
                    type: 'logarithmic',
                    min: 0.000001
                }
            },
            interaction: {
                mode: 'nearest',
                intersect: false,
                axis: 'x'
            }
        }
    });
}
