// QUESTION 1
function hotelCost() {
let response

while (!responseInNumbers (response)) {

     response = prompt("How many nights would you like to stay at our Hotel?")
    
}
    const duration = Number(response)
    const costPerNight = 140
    const totalPrice = duration * costPerNight
console.log("hotelCost:", totalPrice)
    return totalPrice
    
} 




function responseInNumbers(str) {
    const regex = new RegExp(/^[0-9]*$/)
    return regex.test(str)
} 



// QUESTION 2

function planeRideCost() {
    let destination = ""

    while (destination == null || destination == "") {
        destination = prompt("what is your destination?") 
    }
     console.log("destination:", destination)
     if (destination === "London") return 183
     if (destination === "Paris") return 220
     return 300
}
planeRideCost()


function onlyString(str) {
    const regex = new RegExp(/\d/)
    return regex.test(str)
}


// QUESTION 3

function rentalCarCost() {
    let response 

    while (!responseInNumbers (response)) {
        response = prompt ("How many days would you like to rent a car?")
    }
    const dailyPrice = 40
    const numberOfDays = Number(response)


    let discount = 0
    if (numberOfDays >= 10) discount = 0.05

    const totalPrice = dailyPrice * numberOfDays *(1-discount)
    console.log("rentalCarCost:", totalPrice)
    return totalPrice 
}



// QUESTION 4

function totalVacationCost() {
    const carPrice= rentalCarCost()
    const hotelPrice= hotelCost()
    const planePrice = planeRideCost()

console.log("hotelPrice:", hotelPrice)
console.log("planePrice:", planePrice)
console.log("carPrice:", carPrice)

const totalVacationCost = hotelPrice + planePrice + carPrice
console.log("totalVacationCost:", totalVacationCost)
}
totalVacationCost()