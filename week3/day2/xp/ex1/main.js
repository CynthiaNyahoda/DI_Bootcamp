const h1 = getFirstElement("h1")
const h2 = getFirstElement("h2")
const h3 = getFirstElement("h3")
const secondParagraph = getSecondParagraph()
removeLastLine()
addButton()

function removeLastLine() {
    const article = document.querySelector("article")
    article?.lastElementChild.remove()
}

function getFirstElement(selector) {
    return document.querySelector(selector)
}



h2?.addEventListener("click", changeBackground)
h3?.addEventListener("click", hideH3)
secondParagraph.addEventListener("mouseover", makeSecondParagraphFadeout)



function changeBackground() {
    h2?.classList.add("red")
}



function hideH3() {
    h3?.classList.add("hide")
}

function makeSecondParagraphFadeout() {
    secondParagraph.classList.add("fadeout")
}

function getSecondParagraph() {
    return document.querySelectorAll("p")[1]
}
function boldParagraphs() {
    const paragraphs = document.querySelectorAll("p")
    for (const paragraph of paragraphs) {
        paragraph.classList.add("bold")
    }
}

function addButton() {
    const button = document.createElement("button")
    button.textContent ="BOLD"
    button.addEventListener("click", boldParagraphs)
    const article = getFirstElement("article")
    article.appendChild(button)
    
}