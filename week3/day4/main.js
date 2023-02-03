const addToDoButton = document.getElementById('addToDo');
const toDoContainer = document.getElementById('toDoContainer');
const inputField = document.getElementById('inputField')
const tasks = []


addToDoButton.addEventListener
('click', function(){
    let paragraph = document.createElement('p')
    paragraph.classList.add('paragraph-styling')
    paragraph.innerText = inputField.value;
    toDoContainer.appendChild(paragraph);
    inputField.value = ""

    paragraph.addEventListener('click', function(){
        paragraph.style.textDecoration = "line-through"
    })

const inputData = new InputData('inputField');
const task = inputData.get("task");
if (task === "") return;
tasks.push(task);
FormData.reset();
console.log("tasks", tasks);

})
