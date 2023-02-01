
    
   const form = document.getElementById("libform")
    console.log(form)

    
const button = getbutton()
const shuffleButton = document.getElementById("shuffle")
    button?.addEventListener('click', handleclick)
     console.log("button", button)
     
    
    
    

function handleclick(e) {
            e.preventDefault()
            const noun = document.getElementById("noun").Value
            
            const adjective = document.getElementById("adjective").Value
            
            const person = document. getElementById("person").Value
            
            const verb = document.getElementById("verb").Value
            
            const place = document.getElementById("place").Value


if (noun == ""|| adjective==""|| person==""|| verb ==""|| place=="") return

const story = generateStory(noun, adjective, person, verb, place)
    console.log("story", story)

    appendStoryTopage(story)
}

function appendStoryTopage(story) {
    const paragraph = document.getElementById("story")
    const span = document.createElement("span")
    span.innerText= story
    paragraph?.appendChild(span)
}


function generateStory(noun, adjective, person, verb, place) {
    return `Early this morning the ${noun} was found to be ${adjective} and ${person} had just ${verb} at ${place} the very same day.`
    
}


function getbutton() {
    return document.getElementById("lib-button")
}


           

    
    
    

















