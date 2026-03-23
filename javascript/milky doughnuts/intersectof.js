function intersectOf(a, b) {
    let result = [];

    for (let index = 0; index < a.length; index++) {
        
        if (b.includes(a[index]) && !result.includes(a[index])) {
            result.push(a[index]);
        }
    }

    return result;
}


console.log(intersectOf([1, 2, 3], [2, 3, 4])); 

console.log(intersectOf([45, 60, 3, 0], [3, 45, 100])); 

console.log(intersectOf([1, 1, 2, 2], [2, 2, 3])); 

console.log(intersectOf([], [1, 2, 3])); 
