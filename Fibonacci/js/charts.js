// Chart.js implementation for Fibonacci algorithm performance visualization

document.addEventListener('DOMContentLoaded', function() {
    // Performance data from experiments
    const perfData = [
        {n: 10, fib_iterative: 2.86102294921875e-06, fib_iterative_optimized: 9.5367431640625e-07, fib_memo: 3.0994415283203125e-06, fib_matrix: 1.0013580322265625e-05},
        {n: 100, fib_iterative: 7.152557373046875e-06, fib_iterative_optimized: 3.0994415283203125e-06, fib_memo: 1.0013580322265625e-05, fib_matrix: 1.2874603271484375e-05},
        {n: 200, fib_iterative: 9.298324584960938e-06, fib_iterative_optimized: 6.198883056640625e-06, fib_memo: 1.7881393432617188e-05, fib_matrix: 1.5974044799804688e-05},
        {n: 500, fib_iterative: 3.719329833984375e-05, fib_iterative_optimized: 1.6927719116210938e-05, fib_memo: 6.198883056640625e-05, fib_matrix: 2.002716064453125e-05},
        {n: 1000, fib_iterative: 6.67572021484375e-05, fib_iterative_optimized: 3.814697265625e-05, fib_memo: 0.00011801719665527344, fib_matrix: 2.5033950805664062e-05},
        {n: 5000, fib_iterative: 0.0005660057067871094, fib_iterative_optimized: 0.00040340423583984375, fib_memo: 0.0008132457733154297, fib_matrix: 0.00013709068298339844},
        {n: 10000, fib_iterative: 0.0023758411407470703, fib_iterative_optimized: 0.0016300678253173828, fib_memo: 0.0027680397033691406, fib_matrix: 0.0004010200500488281},
        {n: 20000, fib_iterative: 0.008448123931884766, fib_iterative_optimized: 0.005677938461303711, fib_memo: 0.009376049041748047, fib_matrix: 0.001138925552368164},
        {n: 30000, fib_iterative: 0.017866134643554688, fib_iterative_optimized: 0.012006044387817383, fib_memo: 0.019356966018676758, fib_matrix: 0.0016720294952392578},
        {n: 40000, fib_iterative: 0.03313422203063965, fib_iterative_optimized: 0.02028799057006836, fib_memo: 0.03336310386657715, fib_matrix: 0.003522157669067383},
        {n: 50000, fib_iterative: 0.04944109916687012, fib_iterative_optimized: 0.03174018859863281, fib_memo: 0.053086042404174805, fib_matrix: 0.004241943359375},
        {n: 60000, fib_iterative: 0.07253313064575195, fib_iterative_optimized: 0.04559898376464844, fib_memo: 0.07424211502075195, fib_matrix: 0.005203962326049805},
        {n: 70000, fib_iterative: 0.09551477432250977, fib_iterative_optimized: 0.06156802177429199, fib_memo: 0.10172724723815918, fib_matrix: 0.009676933288574219},
        {n: 80000, fib_iterative: 0.12384605407714844, fib_iterative_optimized: 0.07849907875061035, fib_memo: 0.12499594688415527, fib_matrix: 0.010717153549194336},
        {n: 90000, fib_iterative: 0.15742015838623047, fib_iterative_optimized: 0.10072088241577148, fib_memo: 0.16397833824157715, fib_matrix: 0.013051271438598633},
        {n: 100000, fib_iterative: 0.19235467910766602, fib_iterative_optimized: 0.12029099464416504, fib_memo: 0.20043182373046875, fib_matrix: 0.013135194778442383}
    ];

    // Extract data for charts
    const nValues = perfData.map(item => item.n);
    const iterativeData = perfData.map(item => item.fib_iterative);
    const optimizedData = perfData.map(item => item.fib_iterative_optimized);
    const memoData = perfData.map(item => item.fib_memo);
    const matrixData = perfData.map(item => item.fib_matrix);

    // Populate data table
    populateDataTable(perfData);

    // Define chart colors
    const colors = {
        iterative: 'rgba(255, 99, 132, 0.8)',
        optimized: 'rgba(54, 162, 235, 0.8)',
        memo: 'rgba(255, 206, 86, 0.8)',
        matrix: 'rgba(75, 192, 192, 0.8)'
    };

    // Create Linear Scale Chart
    const linearCtx = document.getElementById('linearChart').getContext('2d');
    new Chart(linearCtx, {
        type: 'line',
        data: {
            labels: nValues,
            datasets: [
                {
                    label: 'Iterative (DP)',
                    data: iterativeData,
                    borderColor: colors.iterative,
                    backgroundColor: colors.iterative.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                },
                {
                    label: 'Iterative (Optimized)',
                    data: optimizedData,
                    borderColor: colors.optimized,
                    backgroundColor: colors.optimized.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                },
                {
                    label: 'Memoization',
                    data: memoData,
                    borderColor: colors.memo,
                    backgroundColor: colors.memo.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                },
                {
                    label: 'Matrix Exponentiation',
                    data: matrixData,
                    borderColor: colors.matrix,
                    backgroundColor: colors.matrix.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Fibonacci Algorithm Performance (Linear Scale)',
                    font: {
                        size: 16
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.raw.toExponential(6)} seconds`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Input Size (n)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Time (seconds)'
                    },
                    ticks: {
                        callback: function(value) {
                            return value.toExponential(2);
                        }
                    }
                }
            }
        }
    });

    // Create Logarithmic Scale Chart
    const logCtx = document.getElementById('logChart').getContext('2d');
    new Chart(logCtx, {
        type: 'line',
        data: {
            labels: nValues,
            datasets: [
                {
                    label: 'Iterative (DP)',
                    data: iterativeData,
                    borderColor: colors.iterative,
                    backgroundColor: colors.iterative.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                },
                {
                    label: 'Iterative (Optimized)',
                    data: optimizedData,
                    borderColor: colors.optimized,
                    backgroundColor: colors.optimized.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                },
                {
                    label: 'Memoization',
                    data: memoData,
                    borderColor: colors.memo,
                    backgroundColor: colors.memo.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                },
                {
                    label: 'Matrix Exponentiation',
                    data: matrixData,
                    borderColor: colors.matrix,
                    backgroundColor: colors.matrix.replace('0.8', '0.1'),
                    borderWidth: 2,
                    pointRadius: 3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Fibonacci Algorithm Performance (Log Scale)',
                    font: {
                        size: 16
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.raw.toExponential(6)} seconds`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Input Size (n)'
                    }
                },
                y: {
                    type: 'logarithmic',
                    title: {
                        display: true,
                        text: 'Time (seconds) - Log Scale'
                    },
                    ticks: {
                        callback: function(value) {
                            return value.toExponential(2);
                        }
                    }
                }
            }
        }
    });

    // Function to populate the data table
    function populateDataTable(data) {
        const tableBody = document.querySelector('#performance-data tbody');
        
        data.forEach(row => {
            const tr = document.createElement('tr');
            
            // Add table cells
            tr.innerHTML = `
                <td>${row.n}</td>
                <td>${row.fib_iterative.toExponential(6)}</td>
                <td>${row.fib_iterative_optimized.toExponential(6)}</td>
                <td>${row.fib_memo.toExponential(6)}</td>
                <td>${row.fib_matrix.toExponential(6)}</td>
            `;
            
            tableBody.appendChild(tr);
        });
    }
});
