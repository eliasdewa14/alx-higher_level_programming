#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing the size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      console.log('X');
    }
  }
}