console.log("All the even number from 1 to 100 using for loop");
for(let i = 1; i <=100; i++) {
    if (i%2==0)console.log(i);
}
console.log("All the odd number from 1 to 100  using while loop");
 let i=1;
 while(i<=100){
    if(i%2!=0)console.log(i);
    i++;
 }

 console.log("All the even number from 1 to 100 using do while loop");
 let j=1;
do{
    if(j%2==0)console.log(j);
    j++;
}while(j<=100);

console.log("All the odd character of a string using for of loop");
let b="Hello World";
for(let char of b){
    if(char!=" " && char.charCodeAt(0)%2!=0)console.log(char);
}

console.log("All the even character of a string using for in loop");
for(let index in b){
    if(b[index]!=" " && b[index].charCodeAt(0)%2==0)console.log(b[index]);
}