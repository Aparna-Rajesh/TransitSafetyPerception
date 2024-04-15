// script.js
window.addEventListener('scroll', function() {
    const scrollPosition = window.pageYOffset;

    document.querySelectorAll('.parallax').forEach(function(el, index) {
        const direction = index % 2 === 0 ? 1 : -1; // Alternate direction for each parallax
        const speed = 0.5; // Adjust speed if necessary
        el.style.backgroundPositionY = (direction * scrollPosition * speed) + 'px';
    });
});
