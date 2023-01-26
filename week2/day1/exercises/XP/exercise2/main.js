// QUESTION 1
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
console.log(myWatchedSeries)

let myWatchedSeriesLength = myWatchedSeries.length;
console.log(myWatchedSeriesLength)

// QUESTION 2
const myWatchedSeriesSentence = (`${myWatchedSeries[0]}, ${myWatchedSeries[1]} and ${myWatchedSeries[2]}`);

console.log(myWatchedSeriesSentence);

//QUESTION 3
const sentence = ( `i watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}`)
console.log(sentence)


// PART II
// QUESTION 1
myWatchedSeries[2]= ('Friends')
console.log(myWatchedSeries)

// QUESTION 2
myWatchedSeries.push('Dynasty')
console.log(myWatchedSeries)

// QUESTION 3
myWatchedSeries.unshift('All American')
console.log (myWatchedSeries)

// QUESTION 4
delete myWatchedSeries [1]
console.log(myWatchedSeries)

// QUESTION 5
const moneyheist = myWatchedSeries[2]
console.log(moneyheist[2])

// QUESTION 6
console.log(myWatchedSeries)