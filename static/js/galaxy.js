const stars = 400
const planets = ["bespin", "dagobah", "deathstar", "endor","hoth","tatouine","yavin"] 

// loop to create our background "stars" creates an empty div, with the 
// classname stars, gives them a random position, 1 px in style and then appends
// we will remove these when start button is pressed 
for (let i=0; i < stars; i ++) {
    let star = document.createElement("div")
    star.className="stars"
    let xy = randomPosition()
    star.style.top = xy[0] + "px"
    star.style.left = xy[1] + "px"
    document.body.append(star)
}

// create each planet
planets.forEach((planet) => {

    // planet for creating planet
    planet = `

    <div> 
        <a href="#" id="name-planet" class="planet">${planet}</a>
        <img class="image-planet" src="{% static 'img/${planet}.png' %}">

    </div>

    `

    planet.className ="planets"
    // loop and position planets randomly
    let xy=randomPosition()

    planet.style.top = xy[100] + "px"
    planet.style.left = xy[101] + "px"
    document.body.append(planet)

})

// function to choose a random position on the screen
function randomPosition() {
    let y =  window.innerWidth
    let x = window.innerHeight
    let randomX= Math.floor(Math.random() * x)
    let randomY= Math.floor(Math.random() * y)
    return [randomX, randomY]
}


    