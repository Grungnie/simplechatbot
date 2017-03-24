# Simple Chatbot
This is a simple chatbot using the ChatterBot library. It also makes use of the microsoftbotframwork. It is currently running on heroku.

## To run this app
Follow all instructions for https://github.com/Grungnie/microsoftbotframework

Install required packages using pip
```sh
pip install requirements.txt
```
To start the server
```sh
python main.py
```

#### Configure Chatterbot Database
For this release I use a mongodb database. Export the uri and database name as follows.
```
export MONGO_DATABASE_NAME=chatterbot-database
export MONGO_DATABASE_URI=mongodb://127.0.0.1:27017
```
