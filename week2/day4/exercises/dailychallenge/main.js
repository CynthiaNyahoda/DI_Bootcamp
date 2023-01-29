// question 1
let username = prompt("introduce yourself"); //prompt
console.log(username)

// // question 2
function slitify(username){
return username.split(/\W/)

}
console.log(slitify(username))


// question 3

function lengthofLongestWord(){ 
   
   let longestwordlength = 0;
   
      let usernames =  ['Hello', 'my', 'name', 'is', 'wendy']
      for (let i = 0; i < usernames.length; i++) {
      console.log(usernames[i])
   
   
      const wordlength = usernames.length
      if(wordlength > longestwordlength){
         longestwordlength = wordlength
      }
   
      }return longestwordlength }

const longestwordlength = lengthofLongestWord()
const firstRow = createFirstRow();
console.log(firstRow);

function createFirstRow() {
   const numberfirstRowStars = longestwordlength + 5;
   let row = "";
   for (let i = 0; i< numberfirstRowStars; i++) {
    row = row + "*";
    
   }
   return row
}



function displayRows() {
   const numberofsideStars = 4
   const numberfirstRowStars = longestwordlength + 
numberofsideStars;

return "*".repeat(numberfirstRowStars)
   let row = "";
   for (let i = 0; i< numberfirstRowStars; i++) {
    row = row + "*";
   
} }



const delimiterRow = createDelimterRow();
   console.log(delimiterRow);
      for(const word of words) 
      displayWord(word);
   
 

function displayWord(word) {
  
   const numberOfSpacesToAdd = longestwordlength - word.length + 1
   const emptySpaces = "".repeat(numberOfSpacesToAdd);
   console.log("*" + word + emptySpaces + "*");
}










