let NumeralValue = prompt("Please enter a number")
NumeralValue = Number(NumeralValue)

function EvenOdd(NumeralValue) {
    if (NumeralValue % 2 == 0){
        console.log("This number is Even")
    } else {
        console.log("This number is Odd")
    }
}
EvenOdd(NumeralValue)