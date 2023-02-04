const allBooks = []

const book1 = {
title: "How to Get Away With Murder",
author: "J.K Antheny",
image: "https://picsum.photos/id/1/200/300",
alreadyRead: "true"
}

const book2 = {
    title: "Married my Type",
    author: "Martin.K",
    image: "https://picsum.photos/id/1/200/300",
    alreadyRead: "false"
    }  


    const book3 = {
        title: "Lets Get to the Good Part",
        author: "Kokky Whitney",
        image: "https://picsum.photos/id/1/200/300",
        alreadyRead: "false"
        }


        allBooks.push(book1);
        allBooks.push(book2);
        allBooks.push(book3);

        console.log("allBooks:", allBooks)

        const table = document.createElement("table")
        table.innerHTML =` 
        <thead>
            <tr>
                <th colspan="3"> My Book List</th>
            </tr>
        </thead>
        <tbody>
        <tr>
        <td>${book1.title} wriiten by ${book1.author}</td>
        <td> <img src="${book1.image}"</td>
        <td>Already read: ${book1.alreadyRead}</td>
        </tr>
        <tr>
        <td>${book2.title} wriiten by ${book2.author}</td>
        <td> <img src="${book2.image}"</td>
        <td>Already read: ${book2.alreadyRead}</td>
        </tr>
        <tr>
        <td>${book3.title} wriiten by ${book3.author}</td>
        <td> <img src="${book3.image}"</td>
        <td>Already read: ${book3.alreadyRead}</td>
        </tr>
        </tbody>
        `

        const booklistDiv = document.querySelector(".list_books")
        console.log('booklistDiv:', booklistDiv);
        booklistDiv?.appendChild(table)