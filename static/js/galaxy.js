const stars = 500; // Adjust the number of stars as needed

for (let i = 0; i < stars; i++) {
    let star = document.createElement("div");
    star.className = "stars";
    let x = Math.floor(Math.random() * window.innerWidth);
    let y = Math.floor(Math.random() * window.innerHeight);
    star.style.top = y + "px";
    star.style.left = x + "px";
    document.body.append(star);
}

function randomPosition() {
    let x = window.innerWidth;
    let y = window.innerHeight;
    let randomX = Math.floor(Math.random() * x);
    let randomY = Math.floor(Math.random() * y);
    return [randomY, randomX];
}