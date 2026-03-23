const LinearSearch = require('./LinearSearch');

console.log(LinearSearch([10, 20, 30, 40],30));  // Expected 2
console.log(LinearSearch([5, 15, 25, 35], 5));    // Expected 0
console.log(LinearSearch([1, 2, 3, 4], 10));      // Expected -1
console.log(LinearSearch([], 1)) ;                 // Expected -1
