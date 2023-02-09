#!/usr/bin/node

const request = require('request');

const url = 'https://swapi.dev/api/films/' + process.argv[2] + "/";
let listChars = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  characters = JSON.parse(body).characters;
  getCharacters(0);
});

const getCharacters = (count) => {
  if (count === listChars.length) {
    return;
  }

  request(listChars[count], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(JSON.parse(body).name);
    getCharacters(count + 1);
  });
};

