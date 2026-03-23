function square(number) {
    let result = [];
    for (let index = 1; index <= number; index++) {
        result.push(index * index);
    }
    return result;
}


let n = 5;
let squares = square(n);
console.log(`First ${n} perfect squares:`, squares);


console.log(square(0)); 
console.log(square(1)); 
console.log(square(10)); 
