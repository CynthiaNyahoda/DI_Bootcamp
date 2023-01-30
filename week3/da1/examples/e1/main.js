// TARGET DIV ELEMENT and change elements

// const divElement = document.querySelector('. first-one');

// divElement.innerHTML = '<h2>Another value</h2'

// const div = document.querySelector('div')
// const firstH1= div1.querySelector('h1')

// console.log(firstH1)

const divs = document.querySelectorAll('div')
console.log(divs)

for (let i = 0; i < divs.length; i++) {
    const element = divs[i];
    console.log(element);

    const h1 = element.querySelector('h1')

    // or you could use

    // const h1 = element.getElementByTagName('h1')
    // const h1 = element.firstChild
    h1.innerHTML += `${i + 1}`
    
}


const way1UlElements = document.querySelectorAll('li');
const way1UlElements = way1UlElements[2]

console.log(way1UlElements)

const Way2ulelements = Way1UlElements.lastElementChild('li')
// const Ulelements = ulelements[2]

console.log(ulelements)