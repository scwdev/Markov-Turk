# Markovical Turk API
#### A Marcov chain Monte Carlo text generation API.

## Project Links

- [frontend repo link](url)
- [deployment link](url)

## Project Description
An API that accepts strings as input and converts them into a {state: [...steps]} probability matrix. The user can then take this matrix and use it to generate semi-random strings based on their initial data.

### Tech:
Flask, SQLAlechemy, python-dotenv

### CRUD Routes

| Path | Route | Functionality | JSON | Queries |
| --- | :---: | :---: | :---: | :---: |
| /new/user      | POST | Create new user   | email |  |
| /:api-key/user | GET    | See existing user  | | |
| /:api-key/user | POST   | Edit existing user | email | |
| /:api-key/user | DELETE | See existing user  | | |
||||||
| /:api-key/generate-text						      | POST | Create text without saving data | training_data, n, gram, length | |
| /:api-key/generate-text/sample/:id/:n/:gram/:length | GET  | Create text from saved sample   | | |
| /:api-key/generate-text/matrix/:id/:length          | GET  | Create text from save matrix    | | "start: (first word) |
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

### Models:

login/auth:
 - email: String (required, unique)
 - api-key: String (required)

data_sample:
 - title: String (required, unique)
 - initial_data: Array of Strings (required)
 - added_data: Array of Strings

probability_matrix:
 - base_data_reference: String (required)
 - matrix_title: String (required)
 - seperator: String
 - n_gram: Number
 - matrix: dictionary (required)

saved_output: 
 - base_data_reference: String (required)
 - matrix_reference: String (required)
 - generated: Array of Strings (max length 10)

### Time/Component Table
#### MVP
| Component | Estimated Time |
| --- | :---: |
| Flask research | ?? |
| Models | 2 hrs |
| AuthZ | 3 hrs |
| Base_data routes | 2 hr |
| n-gram algo | 2 hr |
| Matrix routes | 1 hr |
| Generate algo | 2 hrs |
| Generate route | 1 hr |
| Output routes | 1 hr |
| Deployment | 2 hrs |
| --- | :---: |
| Total | 16 hrs |

#### Post-MVP
| Component | Estimated Time |
| --- | :---: |
| API landing | 6 hrs |
| Browser input page | 2 hrs |
