#!/usr/bin/node

const request = require('request');
const requset = require('request');

// const url = process.argv[2] + "/people/18"
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error && response.statusCode == 200) {
    const results = JSON.parse(body).results;
    const characthers = results.map(x => x.characters);
    const wed_ant = characthers.filter(x => x.includes('https://swapi-api.hbtn.io/api/people/18/'));
    console.log(wed_ant.length);
  }
});
