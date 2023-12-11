#!/usr/bin/node
if (process.argv[2] == null) { console.log(0); } else {
  let max = 0; let secondMax = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] >= max) {
      secondMax = max;
      max = process.argv[i];
    }
  }
  console.log(secondMax);
}
