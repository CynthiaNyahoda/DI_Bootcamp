const tasks = [];
let taskId = 0;

function addTask() {
    
  const taskInput = document.getElementById("taskInput");
  const task = taskInput.value;

  if (!task) {
    return;
  }

  const taskObject = {
    task_id: taskId,
    text: task,
    done: false,
  };

  tasks.push(taskObject);
  taskId++;

  const listTasks = document.getElementById("listTasks");
  const taskDiv = document.createElement("div");
  
  taskDiv.innerHTML = `
    <input type="checkbox" id="task-${taskObject.task_id}" onclick="doneTask(${taskObject.task_id})">
    <label for="task-${taskObject.task_id}">${taskObject.text}</label>
    <button onclick="deleteTask(${taskObject.task_id})"><i class="fas fa-times"></i></button>
  `;

  taskDiv.setAttribute("data-task-id", taskObject.task_id);
  listTasks.appendChild(taskDiv);

  taskInput.value = "";
}

function doneTask(taskId) {
  const taskIndex = tasks.findIndex((task) => task.task_id === taskId);
  tasks[taskIndex].done = !tasks[taskIndex].done;
}

function deleteTask(taskId) {
  const taskIndex = tasks.findIndex((task) => task.task_id === taskId);
  tasks.splice(taskIndex, 1);
}
 

