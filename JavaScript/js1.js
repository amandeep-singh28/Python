console.log("Hello World")
console.log("Amandeep Singh")
let a = 5;
{
    let a = 10;
}
console.log(a);


let person = {
    name : "Amandeep",
    age : 21,
    isPassed : true
}
console.log(person);
console.log(typeof(person));

console.log("5"+2)
console.log("5"-2) // Type conversion automatically
console.log(typeof("5"-2)) 

console.log(5 == "5"); // true Data types get converted from string to number. It compares value and ignores data type
console.log(5 === "5"); // false ==== does not allow type conversion

let age = 18;
let hasId = true;
if (age >= 18 && hasId === true) {
    console.log("Adult");
} else {
    console.log("Minor");
}

// let number = Number(prompt("Enter a number:"));
let number = 10;
if (number > 0) {
    console.log(number + " is a positive number");
} else if (number < 0) {
    console.log(number + " is a negative number");
} else {
    console.log("Zero number");
}
console.log(typeof(number));

let username = prompt("Enter username:")
let password = Number(prompt("Enter password:"))
if (username === "admin" && password === 1234) {
    console.log("Login Successful");
} else {
    console.log("Invalid Credentials");
}

// for (let i = 10; i > 0; i--) {
//     console.log(i);
// }

let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}