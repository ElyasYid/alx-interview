The script uses the request module to make HTTP requests to the SWAPI. It takes a film ID as a command-line argument, retrieves the list of characters in that film, and then prints each character's name in the order they appear in the API response.

Example Usage
To use the script, simply run it with Node.js and pass a film ID as a command-line argument:

bash
Copy code
./script_name.js 1
This will fetch and print the names of all characters from the first Star Wars film (Episode IV: A New Hope).

Code Overview
Request the Film Data:
The script starts by making a request to the SWAPI to get the details of the film with the specified ID:

javascript
Copy code
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, data) {
Parse the Response:
The response is parsed to extract the list of character URLs:

javascript
Copy code
const characterUrls = JSON.parse(data).characters;
Fetch and Print Character Names:
The script then recursively requests each character's data and prints their name:

javascript
Copy code
printCharactersInOrder(characterUrls, 0);
Dependencies
Node.js: Ensure you have Node.js installed on your system.
request module: This module is used to make HTTP requests. Install it by running:
bash
Copy code
npm install request
Installation
Clone the repository or download the script.
Ensure you have Node.js installed.
Install the request module:
bash
Copy code
npm install request
Running the Script
To run the script, use the following command:

bash
Copy code
node script_name.js <film_id>
Replace <film_id> with the ID of the Star Wars film you want to query. For example, use 1 for Episode IV: A New Hope.

Example
To fetch the characters from Episode IV: A New Hope (film ID 1), run:

bash
Copy code
node script_name.js 1
The output will be the names of all characters in that film, printed in order.0x06-starwars_api
