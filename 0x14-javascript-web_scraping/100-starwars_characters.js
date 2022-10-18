#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode == 200) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (!error && response.statusCode == 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
