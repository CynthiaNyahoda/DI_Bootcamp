
    
   const form = document.getElementById("libform")
    console.log(form)

    
const button = getbutton()
    button?.addEventListener('click', handleclick)
     console.log("button", button)
     
     function getbutton() {
        return document.getElementById("lib-button")
}
     


const noun = document.getElementById("noun")
console.log("noun", noun)
const adjective = document.getElementById("adjective")
console.log("adjective", adjective)
const person = document. getElementById("person")
console.log("person", person)
const verb = document.getElementById("verb")
console.log("verb", verb)
const place = document.getElementById("place")
console.log("place", place)





function handleclick(e) {
            e.preventDefault()
            const noun = document.getElementById("noun").Value
            
            const adjective = document.getElementById("adjective").Value
            
            const person = document. getElementById("person").Value
            
            const verb = document.getElementById("verb").Value
            
            const place = document.getElementById("place").Value


if (( noun == ""|| adjective==""|| person==""|| verb ==""|| place=="")){
    console.log("complete, well done!!")
} else {
    console.log("incomplete")
}
const story = generateStory(noun, adjective,person,verb,place)
console.log("story", story)
}  
           

function generateStory(noun, adjective, person, verb, place) {
        return `Early this morning the ${noun} was found to be ${adjective} and ${person} had just ${verb} at ${place} the very same day.`
        
    }
    
    
    
// appendStoryTopage()
// }

// // function appendStoryTopage() {
// //     const paragraph = document.getElementById
// // }













// // // // const getvalue = () => {
// // // //     // get form first
// // // //     const form = document.forms
// // // //     // use const form = document.getElementById('forms')

// // // //     // target element
// // // //     const fname = form.elements.fname.value
// // // //     const lname = form.elements.lname.value
// // // //     alert (`${fname}-${lname}`)
// // // // }


