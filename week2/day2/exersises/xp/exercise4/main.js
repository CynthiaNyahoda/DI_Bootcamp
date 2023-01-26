//QUESTION 1
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
console.log(users)

if (users.length === 0) { 
    console.log('noone is online')
}

// QUESTION 2

if (users.length === 1){
    console.log(users[0] + 'is online')
}

// QUESTION 3
if (users.length === 2) {
    console.log(users[0] + 'and' + users[1] + 'are online')
}

// QUESTION 4
if (users.length >= 2) {
    console.log(`${users[0]}, ${users[1]} and ${users.length-2} more are online`)
}