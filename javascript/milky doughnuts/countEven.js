function countEvens(numbers) {
    let count = 0;
    for (let index = 0; index < numbers.length; index++) {
        if (numbers[index] % 2 === 0) {
            count++;
        }
    }
    return count;
}


console.log(countEvens([1, 2, 3, 4, 5, 6],3)); // 3
console.log(countEvens([0, 2, 4, 6, 8],5));    // 5
console.log(countEvens([1, 3, 5, 7],0));       // 0
console.log(countEvens([],0));                 // 0
