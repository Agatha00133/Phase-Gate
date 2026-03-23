function arraysEqual(a, b) {
    if (a.length !== b.length) {
        return false;
    }

    for (let value = 0; value < a.length; value++) {
        if (a[value] !== b[value]) {
            return false;
        }
    }

    return true;
}


console.log(arraysEqual([1, 2, 3], [1, 2, 3],true)); 
console.log(arraysEqual([1, 2, 3], [1, 2, 4],false)); 
