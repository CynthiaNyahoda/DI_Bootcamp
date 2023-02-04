const form = document.querySelector("form")



function logFormInputs(e) {
    e.preventDefault();

    const firstName = document.querySelector("[ name=fname").value
    const lastName = document.querySelector("[name=lname").value

    console.log(firstName, lastName);

    if (firstName === "" || lastName === "") {
        alert("incomplete");
    } else {
        const ul = document.querySelector(".usersAnswer")
        ul.innerHTML="";
        
        const firstLi = document.createElement("li")
        const secondLi = document.createElement("li")
        firstLi.innerText= firstName
        secondLi.innerText= lastName

        ul.append(firstLi, secondLi)

    }


}

form.addEventListener("submit", logFormInputs)