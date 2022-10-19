#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    const characthers = results.map(x => x.characters);
    const wedAnt = characthers.filter(x => x.includes('https://swapi-api.hbtn.io/api/people/18/'));
    console.log(wedAnt.length);
  } else {
    console.log(`An error occured. Status code: ${response.statusCode}`);
  }
});
