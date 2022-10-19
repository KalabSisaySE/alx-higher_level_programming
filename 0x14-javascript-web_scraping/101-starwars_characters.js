#!/usr/bin/node
const request = require('request');
const url = `ttps://swapi-api.hbtn.io/api/films/'${process.argv[2]}`;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        } else {
          console.log(`An error occured. Status code: ${response.statusCode}`);
        }
      });
    }
  } else {
    console.log(`An error occured. Status code: ${response.statusCode}`);
  }
});
