#!/usr/bin/node

const request = require('request');

// check correct number and type of arguments is used
if (process.argv.length !== 3 || !Number.isInteger(Number(process.argv[2]))) {
  console.log('Usage: ./0-starwars_characters.js <id: int>');
  process.exit(1);
}

// create filmUrl
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  // parse json to js object
  const filmData = JSON.parse(body);

  // get name of each actor
  for (const character of filmData.characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
