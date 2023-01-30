const ulElement = document.querySelectorAll('ul')

document.querySelector(".list").children[1].textContent = 'Richard'

const lists = document.querySelectorAll(".list")
lists.forEach(list => list.firstElementChild.textContent = 'Cynthia')

lists[1].children[1].remove()

lists.forEach(list => list.classList.add("student_list"))

const firstUl = document.querySelector('ul.list.student_list')
firstUl.classList.add('university', 'attendance')

console.log(ulElement)



