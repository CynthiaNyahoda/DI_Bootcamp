const navbar = document.getElementById("navBar")
console.log("navbar",navbar)

navbar.setAttribute("id", "socialNetworkNavigation")



const li = document.createElement("li")

const logout = document.createTextNode("Logout")
console.log("logout:", logout)

li.appendChild(logout)
console.log(li)

const ul = navbar?.firstElementChild
ul.appendChild(li)

const firstLi = ul.firstElementChild
console.log("firstLi", firstLi)

const lastLi = ul.lastElementChild
console.log("lastLi", lastLi)

console.log("first li content")
console.log(firstLi?.textContent)
console.log(lastLi?.textContent)