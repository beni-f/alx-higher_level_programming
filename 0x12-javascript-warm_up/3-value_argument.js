#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
