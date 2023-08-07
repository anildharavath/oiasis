function addTask() {
    const taskInput = document.getElementById("taskInput");
    const taskText = taskInput.value.trim();

    if (taskText === "") {
        return;
    }

    const taskItem = document.createElement("li");
    taskItem.innerHTML = `
        <span>${taskText}</span>
        <span class="actions">
            <button onclick="completeTask(this)">Complete</button>
            <button onclick="editTask(this)">Edit</button>
            <button onclick="deleteTask(this)">Delete</button>
        </span>
    `;

    const pendingTasksList = document.getElementById("pendingTasks");
    pendingTasksList.appendChild(taskItem);

    taskInput.value = "";
}

function completeTask(button) {
    const taskItem = button.parentNode.parentNode;
    const completedTasksList = document.getElementById("completedTasks");
    completedTasksList.appendChild(taskItem);
    taskItem.classList.add("completed");
    button.remove();
}

function editTask(button) {
    const taskItem = button.parentNode.parentNode;
    const taskText = taskItem.firstChild.innerText;
    const taskInput = document.getElementById("taskInput");
    taskInput.value = taskText;
    taskItem.remove();
}

function deleteTask(button) {
    const taskItem = button.parentNode.parentNode;
    taskItem.remove();
}
