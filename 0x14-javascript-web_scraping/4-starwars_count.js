#!/usr/bin/node

const request = require('request');
let count = 0;

request.get(process.argv[2], (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes('18')) {
          count += 1;
        }
      });
    });
    console.log(count);
  } else {
    console.log(error);
  }
});