// QUESTION 1

const sentence =  'the movie is not that bad, i like it';
console.log(sentence);

// QUESTION 2

const wordNot = sentence.search('not'); 
console.log (wordNot); 13


// //QUESTION 3

const wordBad = sentence.search ('bad');
console.log (wordBad); 22

//QUESTION 4

const another = 'good'

if (wordBad>wordNot) {
    const substr = sentence.substring (wordNot, wordBad + (wordBad + 'bad'.length))

    console.log (another)
}

else{
    console.log (sentence)
}


//QUESTION 5

if 
(wordNot < wordBad) { 
    
    const substr = sentence.substring (wordNot, wordBad + (wordBad + 'bad'.length))
    console.log (sentence)

}

else {
    console.log(another)
}