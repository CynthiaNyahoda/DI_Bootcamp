const form = document.getElementById("my-form");
const radius = document.getElementById("radius");
const volume = document.getElementById("volume");

addEventListener("submit", handleSubmit)

function handleSubmit(e) {
    e.preventDefault();

    // Volume of sphere = (v=4/3 PI r3)
    const r = Number(radius.value);
    if(Number.isNaN(r)) return;
    const vol = (4/3) * Math.PI * r ** 3;
    volume.value = vol;
}



// EXERCISE 5

document.addEventListener('keyup', (event) => console.log(event.keycode));

form?.addEventListener("pointerenter", () => console.log ("pointer inside form"))
form?.addEventListener("pointerleave", () => console.log ("pointer left form"))

window.addEventListener("blur", ()=>{
    const body = document.querySelector("body");
    body.style.backgroundColor = "grey";
});

window.addEventListener("focus", () => {
    const body = document.querySelector("body")
    body.style.backgroundColor = "white";
})

document.addEventListener("resize", () => alert("window resized"))