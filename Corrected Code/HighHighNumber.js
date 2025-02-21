let numbers = [1,2,3,4,5,6,7,8]

function maxvalue(array){
    let maxvalue = array[0]
    for(let i = 0; i < array.length; i++) {
        if (array[i] > maxvalue){
            maxvalue = array[i]
        }
    }
    console.log(maxvalue)
}

maxvalue(numbers)