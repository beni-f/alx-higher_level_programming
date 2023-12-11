#!/usr/bin/node
const inputNumber = process.argv[2];
if (inputNumber)
{
    number = Math.floor(Number(inputNumber));
    if (isNaN(number))
        console.log('Not a number');
    else
        console.log(`My number: ${number}`);
}
else
    console.log('Not a number');