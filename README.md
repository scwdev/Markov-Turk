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
| *USER ROUTES* |
| /new/user      | POST | Create new user   | email |  |
| /:api-key/user | GET    | See existing user  | | |
| /:api-key/user | PUT   | Edit existing user | email | |
| /:api-key/user | DELETE | See existing user  | | |
| *GENERATING TEXT* |
| /:api-key/generate-text						      | POST | Create text without saving data | training_data, n, gram, length | |
| /:api-key/generate-text/sample/:id/:n/:gram/:length | GET  | Create text from saved sample   | | |
| /:api-key/generate-text/matrix/:id/:length          | GET  | Create text from save matrix    | | start (first word) |
| *TRAINING DATA* |
| /:api-key/sample     | GET    | Index existing training data titles and ids | | |
| /:api-key/sample     | POST   | Create new training data entry              | sample_title, initial_data | |
| /:api-key/sample/:id | GET    | Show individual training data entry         | | |
| /:api-key/sample/:id | PUT    | Update entry                                | sample_title, added_data | |
| /:api-key/sample/:id | DELETE | Delete entry                                | | |
| *PROBABILITY MATRICES* |
| /:api-key/matrix                       | GET    | Index existing probability matrices titles and ids |                       | |
| /:api-key/sample/:sample-id/matrix     | POST   | Create new matrix entry                            | matrix_title, n, gram | |
| /:api-key/matrix/:id                   | GET    | Show individual matrix entry                       |                       | |
| /:api-key/matrix/:id                   | DELETE | Delete matrix                                      |                       | |


### Using the API:

#### Requesting a new API Key:
 - send a POST request to "/user/new" with an email address in the JSON body formatted as
    ```
    {
        "email": <string>
    }
    ```

#### Saving new data:
 - To add training data, send a POST request to "/:api-key/sample/" with the JSON body formatted as. As of last update linebreaks are not preserved and capitalized letters are changed to lower-case. 
    ```
    {
        "initial_data": <array of strings>,
        "sample_title": <string>
    }
    ```

 - To create a new probability matrix from saved training data send a POST request to "/:api-key/sample/:sample-id/matrix" with the JSON body formatted as:
    ```
    {
        "matrix_title": <string>,
        "n": <integer>,
        "gram": <string> // ("word" or "char")
    }
    ```

#### Generating text:
 - You can generated text without saving anything in the database, however you do still need an API key. You can do so by sending a POST request to "/:api-key/generate-text" with a JSON body of:
    ```
    {
        "training_data": <array of strings>,
        "n": <integer>,
        "gram": <string>, // "word" or "char"
        "length": <integer> // desired return length in characters
    }
    ```

However, if you have data saved in the API you can generated text with a simple GET request.
 - To generate text from a sample use "/:api-key/generate-text/sample/:id/:n/:gram/:length".
 - The fastest request is to generated text from an existing matrix at "/:api-key/generate-text/matrix/:id/:length", as this doesn't require the server to build a new matrix for each request. In addition, this route takes "start" as a query, allowing you to specify a starting "n-gram", as long as it exists in the matrix.

