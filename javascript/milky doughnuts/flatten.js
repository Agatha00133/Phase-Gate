function flatten(matrix) {
    let result = [];

    for (let index = 0; index < matrix.length; index++) {
        for (let value = 0; value < matrix[index].length; value++) {
            result.push(matrix[index][value]);
        }
    }

    return result;
}



console.log(flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));

console.log(flatten([[1], [2], [3]]));

console.log(flatten([[1, 2], [], [3, 4]]));

console.log(flatten([]));
