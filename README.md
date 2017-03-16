# Microsoft Bot Framework
Microsoft Bot Framework is a wrapper for the Microsoft Bot API by Microsoft. It uses Flask to recieve the post messages from microsoft and Celery to complete Async tasks.

## To run this app
Create a Microsoft Chatbot | https://dev.botframework.com/bots. Generate <Microsoft App ID> and <Microsoft App Secret> then add them to the evironment vars.
```
export APP_CLIENT_ID=<Microsoft App ID>
export APP_CLIENT_SECRET=<Microsoft App Secret>
```
Also set the environment (PROD or DEV)
```
export ENVIRONMENT=PROD
```
Install required packages using pip
```sh
pip install requirements.txt
```
To start the server run python main.py
#### Configure Async Tasks
Add the broker-url and result-backend uri to the environment vars
```
export CELERY_BROKER_URL=redis://localhost:6379
export CELERY_RESULT_BACKEND=redis://localhost:6379
```
To use celery install and configure celery and its backend and run
```sh
celery -A microsoftbotframework.runcelery.celery worker --loglevel=info
```
#### Configure Chatterbot Database
For this release I use a mongodb database. Export the uri and database name as follows.
```
export MONGO_DATABASE_NAME=chatterbot-database
export MONGO_DATABASE_URI=mongodb://127.0.0.1:27017
```