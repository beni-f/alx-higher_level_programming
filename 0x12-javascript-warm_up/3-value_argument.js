#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === null) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
