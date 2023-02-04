let allBoldItems;

function getBoldItems() {
    allBoldItems = document.getElementsByTagName("strong")
}

function highlight(){
    getBoldItems();
    for (const boldItem of allBoldItems) {
        boldItem.style.color ='blue'
    }
}

function returnNormal() {
    getBoldItems();
    for (const item of allBoldItems) {
        item.style.color = 'black'
    }
}

const paragraph = document.querySelector("p")
paragraph.addEventListener("mouseover", highlight)
paragraph.addEventListener("mouseout", returnNormal)