   
    document.addEventListener("DOMContentLoaded", function() {
        var container = document.querySelector('.galaxy-container');
        var planets = document.querySelectorAll('.planet-item');
        var containerWidth = container.clientWidth;
        var containerHeight = container.clientHeight;
    
        planets.forEach(function(planet) {
            var randomX = Math.random() * (containerWidth - 200);
            var randomY = Math.random() * (containerHeight - 200);
            planet.style.left = randomX + 'px';
            planet.style.top = randomY + 'px';
        });
    });
    