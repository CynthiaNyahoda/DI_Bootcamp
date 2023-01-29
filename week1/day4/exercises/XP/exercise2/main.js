
function calculatorTip() {
    const amount = prompt("How much is the bill")
    let tipPercent
    if (amount < 50) tipPercent = 0.2;
    if (amount > 50 && amount < 200) tipPercent = 0.15
    if(amount > 200) tipPercent = 0.1
        
    const total = amount * (1 + tipPercent)

    console.log("bill:", amount)
    console.log("tipPercent", tipPercent)
    console.log( "total:", total)
} calculatorTip()