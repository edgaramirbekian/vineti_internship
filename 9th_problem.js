// Determine if a number is power of two
// Realization in JavaScript
// There are many ways but let's use recursion


// I'm going to use node.js to run this
// let's create a user input interface in node.js and put our algorithm
// functio into it

let rl = require('readline');
let prompts = rl.createInterface(process.stdin, process.stdout);
prompts.question("Write a number to check ", function is_power (given_number) {
    if (given_number%2==0) {
        if (given_number/2 == 1) {

            console.log(true);

        }
        else {

            is_power (given_number/2, 2);

        }
    }
    else {

        console.log(false);

    }

    process.exit();
});