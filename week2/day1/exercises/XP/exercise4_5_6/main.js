let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:55
    // Actual:55

    a = 2;

    console.log(a+b) //second expression
    // Prediction:23
    // Actual:23

    c = undefined

    console.log(3 + 4 + '5')
    // prediction 7
    // Actual: 75



// EXERCISE 5



    typeof(15)
// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:string
// Actual:number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:boolean
// Actual:boolean

typeof(1 != 2)
// Prediction: true
// Actual:boolean

"hamburger" + "s"
// Prediction:string
// Actual: string

"hamburgers" - "s"
// Prediction:string
// Actual:NaN

"1" + "3"
// Prediction:number
// Actual:13

"1" - "3"
// Prediction:number
// Actual:-1

"johnny" + 5
// Prediction:string
// Actual:johnny5

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction:NaN
// Actual:NaN

1 != 1
// Prediction:boomlean
// Actual:False

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:False
// Actual:False


// EXERCISE 6



5 + "34"
// Prediction:534
// Actual:534

5 - "4"
// Prediction:1
// Actual:1

10 % 5
// Prediction:NaN
// Actual:0

5 % 10
// Prediction:5
// Actual:5

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript

" " + " "
// Prediction:0
// Actual:''

" " + 0
// Prediction:0
// Actual:0

true + true
// Prediction:true
// Actual:2

true + false
// Prediction:0
// Actual:1

false + true
// Prediction:1
// Actual:

false - true
// Prediction:NaN
// Actual:-1

!true
// Prediction:False
// Actual:False

3 - 4
// Prediction:-1
// Actual:-1

"Bob" - "bill"
// Prediction:NaN
// Actual:NaN