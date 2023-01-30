
const planets = [ 
    {name: "earth", moon:1}, 
    {name:"jupiter", moon:3}, 
    {name:"mercury",moon: 0},
     {name:"mars",moon:2}, 
     {name:"venus", moon:0}
    ]

     for (const planet of planets) {
  const div = document.createElement("div")
  div.classList.add("planet")
  div.classList.add(planet.name)

for (let i = 0; i < planet.moons; i++) {
    const moonDiv = document.createElement("div");
    moonDiv.classList.add("moon")
    moonDiv.style.left = i * 10 + "px"
    div.appendChild(moonDiv)
    
}  
  
  const section = document.querySelector(".listPlanets")
  section?.appendChild(div)
     } console.log(planets)
     
  

 








    
