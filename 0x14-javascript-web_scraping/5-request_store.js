#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    fs.writeFile(process.argv[3], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  } else {
    console.log(error);
  }
});
