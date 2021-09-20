# Markovical Turk API
#### A Marcov chain Monte Carlo text generation API.

- [Deployed here](https://markov-turk.herokuapp.com/)

## Project Description
An API that accepts strings as input and converts them into a {state: [...steps]} probability matrix. The user can then take this matrix and use it to generate semi-random strings based on their initial data.

### Tech:
Flask, SQLAlechemy, flask-migrate

### Routes

| Path | Route | Functionality | JSON | Queries |
| --- | :---: | :---: | :---: | :---: |
| /new/user      | POST | Create new user   | email |  |
| /:api-key/user | GET    | See existing user  | | |
| /:api-key/user | POST   | Edit existing user | email | |
| /:api-key/user | DELETE | See existing user  | | |
||||||
| /:api-key/generate-text						      | POST | Create text without saving data | training_data, n, gram, length | |
| /:api-key/generate-text/sample/:id/:n/:gram/:length | GET  | Create text from saved sample   | | |
| /:api-key/generate-text/matrix/:id/:length          | GET  | Create text from save matrix    | | start (first word) |
||||||
| /:api-key/sample     | GET    | Index existing training data titles and ids | | |
| /:api-key/sample     | POST   | Create new training data entry              | sample_title, initial_data | |
| /:api-key/sample/:id | GET    | Show individual training data entry         | | |
| /:api-key/sample/:id | PUT    | Update entry                                | sample_title, added_data | |
| /:api-key/sample/:id | DELETE | Delete entry                                | | |
||||||
| /:api-key/matrix     | GET    | Index existing probability matrices titles and ids |                       | |
| /:api-key/matrix     | POST   | Create new matrix entry                            | matrix_title, n, gram | |
| /:api-key/matrix/:id | GET    | Show individual matrix entry                       |                       | |
| /:api-key/matrix/:id | DELETE | Delete matrix                                      |                       | |
||||||
| /:api-key/output            | GET    | Index title & id saved output | | |
| /:api-key/matrix/:id/output | POST   | Save new text | output_title, text | |
| /:api-key/output/:id        | SHOW   | read output object | | |
| /:api-key/output/:id        | PUT    | read output object | | |
| /:api-key/output/:id        | DELETE | delete output object | | |

### Using the API:

#### Requesting a new API Key:
send a POST request to "/user/new" with an email address in the JSON body formatted as {"email": <string>}

#### Saving new data:
To add training data, send a POST request to "/:api-key/sample/" with the JSON body formatted as {"initial_data": <array of strings>, "sample_title": <string>}