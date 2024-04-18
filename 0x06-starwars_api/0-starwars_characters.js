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

// get character name from person url
const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
};

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
  const promises = filmData.characters.map(getCharacterName);

  Promise.all(promises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
