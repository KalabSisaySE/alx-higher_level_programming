#!/usr/bin/node

const request = require('request');
url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  // console.log(body);
  console.log(JSON.parse(body).title);
});
