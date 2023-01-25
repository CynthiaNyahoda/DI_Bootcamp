// short circuiting / a way to write code in a straightline

// let value
// let raining = false or true 
// value = raining && 'it is raining' || "it isn't raining"

// if (raining) {
//     value= 'it is raining today'
// }

// else {
//     value = "it isn't raining today"
// }

// console.log(value); 

//condition

// let raining = false, value;
// value = raining && 'it is raining today'

// console.log(value); 


// or 
// let raining = false, really = false, value;
// value = raining && really &&'it is raining today'; 

// console.log(value); 


// let raining = true, really= false,value;
// let str = 'raining today';
// value = ( raining || really) && str;
// console.log(value);

// or just
// let raining = true, really= false,value;
// let str = 'raining today';
// console.log(value); xyz

// value = ( raining || really) ? str : 'xyz'


// console.log(3 || 'Orange');
// console.log('' || 'Orange');
// console.log(true || 0);
// console.log(undefined || null);


// let person = {
//     name: 'Jack',
//     age: 34
//     job:true
//   };
//   console.log(person.job ? || 'unemployed');
//   // 'unemployed'


// to add an element
//  let person = {
//     firstname: 'John'
//     lastname:'doe'
//     eyecolor:'blue'
//  };

//  person.age = 48;

//  console.log (person) { firstname:'john', lastname: 'doe'..etc}
//  console.log ( person.firstname) John
