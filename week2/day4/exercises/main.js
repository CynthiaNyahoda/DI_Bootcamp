// question 1
const username = prompt("introduce yourself"); //prompt
console.log(username)

// // question 2


function slitify(username){
return username.split(/\W/)

}
console.log(slitify(username))

// question 3
let usernames = ['Hello', 'my', 'name', 'is', 'Cynthia']
for (let i = 0; i < usernames.length; i++) {
   console.log(usernames[i])
    
}

let lengthoflongestword = 0;
const wordlength