#################################################################
Backend application which lets developers list and browse games.

API includes - CRUD operations and Search API

To test the application
Super user created-

name - sreenidhin
password - cgi

Authorixation token has to be passed with requests inorder to access api.

To receive a token for a user- `localhost:port/api-token-auth/`  api is provided.
For CRUD operations the api is -`localhost:port/game/<int:pk>/`.
For searching the DB - `localhost:port/gamesearch/?search=<search key>`. is used. 

 


