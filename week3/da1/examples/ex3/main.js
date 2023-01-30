const divElement = document.querySelector('div')

let className = divElement.getAttribute('class')
console.log(className)

className += 'fat';
divElement.setAttribute('class', className)
console.log(className)

// adding and deleting elementss

// ADD
const ulElemet = document.querySelector('ul')
ulElemet.innerHTML += '<li>Bob</li>'

// remove

ulElemet.innerHTML = ulElemet.innerHTML.replace('<li>Pete</li>', '')

// dont often us innerHTML

const ulElemet = document.querySelector('ul')
const newBobLi = document.createElement('li');
newBobLi.innerText = '<li>Bob</li>'

ulElemet.appendChild(newBobLi)


// replace

const newLiFirst = document.createElement('li')


// dailychallenge
// copy the html and css
// link rel "stylesheet" href etc
// create a div class planetx2
// another div class moonx2
// put the divs in section
// create array cont planetsArray = [ all the planets]
// console it 
// const planetElements = planetsArray.map( name => { const elements = Document.createElement('div') return elements
// }) console.log(planetElements)
//  you can use reduce 
// at css for diff background color, 
// array [ {name:'moon', moons:1}]

 //  for (const planet of planets){
    //  const div = document.createElement('div');
    // div.classList.add('planet');