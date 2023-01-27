// QUESTION 1
let numberofBeers = prompt("How many beers?")


while (numberofBeers > 0) {
    const lyrics = compilelyrics(numberofBeers);
    console.log(lyrics);
    numberofBeers = numberofBeers -1 
}


function compilelyrics(value) {

    const bottleOrBottles = BottleorBottles(value);
    const lyrics = `${value} ${bottleOrBottles} of beer on the wall
${value} ${bottleOrBottles} of beer
Take 1 down, pass it around
${value - 1}${BottleorBottles(value - 1)} of beer on the wall`;
    

return lyrics;
}


function isPlural(value){
    if (value > 1) {
        return true
        
    } else {
        return false
    }
}

function BottleorBottles(value) {
    if (isPlural(value)) {
        return "bottles;"
    } else {
        return "bottle"
    }
}

