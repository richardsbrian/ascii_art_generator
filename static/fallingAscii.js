// Get the canvas and its drawing context
const canvas = document.getElementById('fallingAscii');
const ctx = canvas.getContext('2d');

// Set canvas size to the window dimensions
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Define ASCII characters and font settings
const asciiChars = " .:-=+*%@#";
const fontSize = 12;
const columns = Math.floor(canvas.width / fontSize); // Calculate number of columns

// Initialize drop positions for each column
const drops = Array(columns).fill(0);

function draw() {
    // Create a trailing effect with a semi-transparent background
    ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.font = `${fontSize}px monospace`; // Set font style

    // Draw characters and update drop positions
    for (let i = 0; i < drops.length; i++) {
        // Pick a random character
        const char = asciiChars[Math.floor(Math.random() * asciiChars.length)];

        // Generate random color
        const randomColor = `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 0.8)`;
        ctx.fillStyle = randomColor;

        // Draw the character
        ctx.fillText(char, i * fontSize, drops[i] * fontSize);

        // Reset drop to the top randomly or move it down
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.95) {
            drops[i] = 0;
        }
        drops[i]++;
    }

    requestAnimationFrame(draw); // Loop the animation
}

// Update canvas size on window resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

draw(); // Start the animation
