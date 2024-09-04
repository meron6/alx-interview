#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error fetching data:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error('Failed to fetch data. Status code:', response.statusCode);
        process.exit(1);
    }

    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(characterUrl => {
        request(characterUrl, (err, res, charBody) => {
            if (err) {
                console.error('Error fetching character data:', err);
                return;
            }

            if (res.statusCode !== 200) {
                console.error('Failed to fetch character data. Status code:', res.statusCode);
                return;
            }

            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
        });
    });
});
