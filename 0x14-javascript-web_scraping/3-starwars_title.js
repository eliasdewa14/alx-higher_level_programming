#!/usr/bin/node

const request = require('request');

const url = `http://swapi.co/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
