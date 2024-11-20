async function testPing() {
    try {
        const response = await fetch('/api/ping');
        const data = await response.json();

        const resultDiv = document.getElementById('result');
        if (data.ping !== null) {
            resultDiv.textContent = `Ping: ${data.ping} ms`;
        } else {
            resultDiv.textContent = 'Ping test failed.';
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error fetching ping.';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('go-btn');
    button.addEventListener('click', testPing);
});
