const stars = 400

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

// function to choose a random position on the screen
function randomPosition() {
    let y =  window.innerWidth
    let x = window.innerHeight
    let randomX= Math.floor(Math.random() * x)
    let randomY= Math.floor(Math.random() * y)
    return [randomX, randomY]
}


window.onload = function() {
    var backgroundAudio=document.getElementById("audio-intro");
    backgroundAudio.volume=0.1;
}

// let link = document.querySelector("#startAdventure").addEventListener("click", function() {
//     let start = document.getElementById()
    
// })


document.addEventListener("DOMContentLoaded", function() {
    let start = document.getElementById("startAdventure")
    let reveal = document.getElementById("intro-container")
    start.addEventListener("click", function() {
        if (reveal.style.display === "none") {
            reveal.style.display = "block"
            start.style.display = "none"
        }
    })
})



