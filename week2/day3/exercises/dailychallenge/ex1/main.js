//QUESTION 1
const endNumber = 6
let stars = ""
for (let i = 0; i < endNumber; i ++) {
    stars = stars + "*"
    console.log(stars);
} ;
    

// QUESTION 2

for (let i = 0; i < endNumber; i ++) {
    stars = stars + ""
    const nStars = i + 1;
    

    let nestedStars = ""
    for (let j = 0; j < nStars; j++) {
        nestedStars = nestedStars + "*";
        console.log(nestedStars)
} };

