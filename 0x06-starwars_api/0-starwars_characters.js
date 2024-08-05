#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, data) {
  if (err) throw err;
  const characterUrls = JSON.parse(data).characters;
  printCharactersInOrder(characterUrls, 0);
});

const printCharactersInOrder = (characterUrls, index) => {
  if (index === characterUrls.length) return;
  request(characterUrls[index], function (err, res, data) {
    if (err) throw err;
    console.log(JSON.parse(data).name);
    printCharactersInOrder(characterUrls, index + 1);
  });
};
