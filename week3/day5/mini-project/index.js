const colors = document.querySelectorAll("#colors .color");

for (const color of colors) {
  color.addEventListener("click", function() {
    selectedColor = this.style.backgroundColor;
  });
}

const grid = document.querySelector("#grid");

let isDrawing = false;

grid.addEventListener("mousedown", function(event) {
  isDrawing = true;
  event.target.style.backgroundColor = selectedColor;
});

grid.addEventListener("mouseover", function(event) {
  if (isDrawing) {
    event.target.style.backgroundColor = selectedColor;
  }
});

grid.addEventListener("mouseup", function() {
  isDrawing = false;
});

const clearBtn = document.querySelector("#clear")

clearBtn.addEventListener("click", () => {
  squares.forEach((square) => {
    square.style.backgroundColor = "";
  });
});






