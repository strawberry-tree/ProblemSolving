let fs = require('fs');
let input = fs.readFileSync('dev/stdin').toString().split(' ');
let [a, b] = input.map(Number);
console.log(a + b);