document.addEventListener("DOMContentLoaded", function() {
    var container = document.querySelector('.galaxy-container');
    var planets = document.querySelectorAll('.planet-item');
    var containerWidth = container.clientWidth;
    var containerHeight = container.clientHeight;
    var numPlanets = planets.length;
    var radius = Math.min(containerWidth, containerHeight) * 0.3;
    var angleIncrement = (2 * Math.PI) / numPlanets;

    planets.forEach(function(planet, index) {
        var angle = index * angleIncrement;
        var x = containerWidth / 2 + radius * Math.cos(angle) - planet.offsetWidth / 2;
        var y = containerHeight / 2 + radius * Math.sin(angle) - planet.offsetHeight / 2;
        planet.style.left = x + 'px';
        planet.style.top = y + 'px';
    });
});