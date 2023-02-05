let distance = 0 

function myMove() {
    setInterval(moveRedSquare,1)
}

function moveRedSquare() {
    if (distance === 350) {
        clearInterval(interval)
        return
    }
    distance = distance + 1
    const redSquare = document.getElementById('animate')
    redSquare.style.left = distance + "px"
}