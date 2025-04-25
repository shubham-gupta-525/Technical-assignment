window.onload = () => {
    const ctxCPU = document.getElementById('cpuChart').getContext('2d');
    new Chart(ctxCPU, {
        type: 'doughnut',
        data: {
            labels: ['Used', 'Free'],
            datasets: [{
                data: [50, 50],
                backgroundColor: ['red', 'gray']
            }]
        }
    });

    const ctxRAM = document.getElementById('ramChart').getContext('2d');
    new Chart(ctxRAM, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar'],
            datasets: [{
                label: 'RAM Usage',
                data: [70, 80, 60],
                fill: true,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'blue'
            }]
        }
    });

    const ctxTraffic = document.getElementById('trafficChart').getContext('2d');
    new Chart(ctxTraffic, {
        type: 'line',
        data: {
            labels: ['Day 1', 'Day 2', 'Day 3'],
            datasets: [{
                label: 'Incoming Traffic',
                data: [100, 200, 150],
                borderColor: 'green',
                fill: false
            }]
        }
    });
};
