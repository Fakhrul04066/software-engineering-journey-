// 1. Normal Function - Count Vowels
function countV(str) {
    let count = 0;

    for (const char of str.toLowerCase()) {
        if ("aeiou".includes(char)) {
            console.log(char);
            count++;
        }
    }

    console.log(count);
}

countV("javascript");


// 2. Arrow Function - Count Vowels
const contV = (str) => {
    let count = 0;

    for (const char of str.toLowerCase()) {
        if ("aeiou".includes(char)) {
            console.log(char);
            count++;
        }
    }

    console.log(count);
};

contV("javascript");


// 3. map() - Square Every Number
const nums = [1, 2, 3, 4, 5, 6];

const square = nums.map((num) => {
    return num * num;
});

console.log(square);


// 4. reduce() - Calculate Sum
const sum = nums.reduce((total, num) => {
    return total + num;
}, 0);

console.log(sum);


// 5. filter() - Find Even Numbers
const even = nums.filter((num) => {
    return num % 2 === 0;
});

console.log(even);


// 6. forEach() - Print Every Element
const fruits = ["Apple", "Banana", "Mango"];

fruits.forEach((fruit) => {
    console.log(fruit);
});


// 7. find() - Find First Matching Number
const result = nums.find((num) => {
    return num > 3;
});

console.log(result);


// 8. some() - Check If Any Number Is Even
const hasEven = nums.some((num) => {
    return num % 2 === 0;
});

console.log(hasEven);


// 9. every() - Check If All Numbers Are Even
const allEven = nums.every((num) => {
    return num % 2 === 0;
});

console.log(allEven);


// 10. sort() - Sort Numbers in Ascending Order
const numbers = [50, 10, 40, 20, 30];

const sorted = numbers.sort((a, b) => {
    return a - b;
});

console.log(sorted);


// 11. map() with Objects - Get Student Names
const students = [
    { name: "Rahim", marks: 85 },
    { name: "Karim", marks: 30 },
    { name: "Hasan", marks: 90 }
];

const names = students.map((student) => {
    return student.name;
});

console.log(names);


// 12. filter() + map() - Get Passed Students
const passed = students
    .filter((student) => {
        return student.marks >= 40;
    })
    .map((student) => {
        return student.name;
    });

console.log(passed);