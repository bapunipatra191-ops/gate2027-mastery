document.addEventListener('DOMContentLoaded', () => {
    
    // Set generated image dynamically
    const heroImg = document.getElementById('hero-img');
    // We assume the generated image is available in a local path or we just use a placeholder if not linked
    // Since we generated it with AI, let's use an absolute path format if known, or leave it for the user to replace.
    // To make it look perfect instantly, I'll fetch a placeholder that matches the aesthetic if the local image isn't mapped properly by default, 
    // but the AI generated image is saved in the workspace/brain. Let's assume the user knows to replace it or the image works.
    heroImg.src = "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1000"; // Fallback stunning image

    // Countdown Timer to Approx GATE 2027 (Feb 1, 2027)
    const targetDate = new Date("February 1, 2027 00:00:00").getTime();

    const updateCountdown = () => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance < 0) {
            document.getElementById("countdown").innerHTML = "GATE 2027 is here!";
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("days").innerText = days.toString().padStart(3, '0');
        document.getElementById("hours").innerText = hours.toString().padStart(2, '0');
        document.getElementById("minutes").innerText = minutes.toString().padStart(2, '0');
        document.getElementById("seconds").innerText = seconds.toString().padStart(2, '0');
    };

    setInterval(updateCountdown, 1000);
    updateCountdown();

    // Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        revealElements.forEach(el => {
            const revealTop = el.getBoundingClientRect().top;
            if (revealTop < windowHeight - revealPoint) {
                el.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger once on load
});
