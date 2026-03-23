function removeDuplicates(arrays) {
    let result = [];

    for (let index = 0; index < arrays.length; index++) {
        
        if (!result.includes(arrays[index])) {
            result.push(arrays[index]);
        }
    }

    return result;
}


console.log(removeDuplicates([1, 2, 2, 3, 4, 3])); 

console.log(removeDuplicates([45, 60, 3, 0, 67, 2, 45, 3, 22, 0])); 

console.log(removeDuplicates([])); 

console.log(removeDuplicates([5, 5, 5, 5])); 

