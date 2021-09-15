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

| Path | Route | Functionality |
| --- | :---: | :---: |
| /key | get | read existing key |
| /key/new | post | create new key |
| /key/delete | delete | delete existing key and all associated data |
| --- | :---: | :---: |
| /data/:key | get | read existing base_data titles and ids |
| /data/:key | post | add new base_data entry |
| /data/:key/:id | show | read individual base_data entry |
| /data/:key/:id | put | update entry |
| /data/:key/:id | delete | delete entry |
| --- | :---: | :---: |
| /matrix/:key | get | read all matrices (title & id) associated with reference |
| /matrix/:key | post | generate new reference |
| /matrix/:key/:id | show | read individual probability matrix entry |
| /matrix/:key/:id | delete | delete matrix |
| --- | :---: | :---: |
| /generate/:length | get | read MCMC output with charcount = :length |
| --- | :---: | :---: |
| /output/:key | get | read title & id for all output /generate objects |
| /output/:key | put | save new object |
| /output/:key/:id | show | read output object |
| /output/:key/:id | delete | delete output object |

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
