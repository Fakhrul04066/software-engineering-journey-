// JavaScript Array Practice

let fruits = ["Apple", "Banana", "Mango"];

console.log("Original array:", fruits);

// Access elements
console.log("First:", fruits[0]);
console.log("Second:", fruits[1]);

// Array length
console.log("Length:", fruits.length);

// Add at the end
fruits.push("Orange");
console.log("After push:", fruits);

// Add at the beginning
fruits.unshift("Guava");
console.log("After unshift:", fruits);

// Remove from the end
fruits.pop();
console.log("After pop:", fruits);

// Remove from the beginning
fruits.shift();
console.log("After shift:", fruits);

// Change an element
fruits[1] = "Watermelon";
console.log("After update:", fruits);

// Loop through array
for (let i = 0; i < fruits.length; i++) {
    console.log(i, fruits[i]);
}

// forEach
fruits.forEach((fruit, index) => {
    console.log(index, fruit);
});

// Check if an element exists
console.log(fruits.includes("Apple"));

// Find index
console.log(fruits.indexOf("Mango"));

// Add/remove using splice
fruits.splice(1, 0, "Pineapple");
console.log("After splice:", fruits);

// Get part of array using slice
let selectedFruits = fruits.slice(0, 2);
console.log("Sliced array:", selectedFruits);

// Numbers array
let numbers = [10, 20, 30, 40, 50];

// map
let doubled = numbers.map((num) => num * 2);
console.log("Doubled:", doubled);

// filter
let greaterThan25 = numbers.filter((num) => num > 25);
console.log("Greater than 25:", greaterThan25);

// reduce
let sum = numbers.reduce((total, num) => total + num, 0);
console.log("Sum:", sum);