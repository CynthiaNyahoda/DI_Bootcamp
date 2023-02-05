setTimeout(alertHello, 2000)
setTimeout(addParagraph, 2000)
const interval = setInterval(addParagraph,2000)


function alertHello() {
    alert('hello world!') 
}

function addParagraph(){
const p = document.createElement('p')
p.textContent = 'Hello world'
const container = document.getElementById('container')
if(container?.children.length < 5) {
container?.appendChild(p)
} else {
    clearParagraphInterval()
}
}


const button = document.getElementById('clear')
button?.addEventListener("click", clearParagraph)

function clearParagraph() {
clearInterval(interval)
}

