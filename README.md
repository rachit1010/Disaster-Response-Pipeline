# Disaster-Response-Pipeline
## Project Description
Disaster Response Pipeline is the part of Udacity Nanodegree. In this project, we are going to build a model to classify messages that are sent during disasters. There are few pre-defined categories, and examples of these categories include military, Medical help, Search And Rescue, flood, food etc. During any disaster we face problem to filter the message as there are millions of messages floating through social media or through disaster organizations.By classifying these messages, we can allow these messages to be sent to the appropriate disaster relief agency on priority basis. This project involves the building of a basic ETL and Machine Learning pipeline to facilitate the task. This is also a multi-label classification task, since a message can belong to one or more categories. We will be working with a data set provided by Figure Eight containing real messages that were sent during disaster events.

Finally, this project contains a web app where you can input a message and get classification results.

<img width="846" alt="web_app" src="https://user-images.githubusercontent.com/81413089/126498350-00ff3f43-2034-44b0-925b-e023e85c5ac0.PNG">

## Structure Of The Project

This project contains three folders mainly (app, models, data) and its working is shown in the figure mentioned below.
     
<img width="582" alt="Process_steps" src="https://user-images.githubusercontent.com/81413089/126501541-a538ce48-21ce-4942-bf4f-addd1cb8edd0.PNG">

## Installation Requirement
Must runing with Python 3 with libraries of numpy, pandas, matplotlib, sqlalchemy, regular expression, NLTK, pickle, Sklearn, plotly and flask libraries.

## File Descriptions
* App folder including the go.html and master.html and "run.py" files for the web application
* Data folder contains "disaster_response_db.db", "disaster_categories.csv", "disaster_messages.csv" and "process_data.py" for data cleaning and transfering.
* Models folder includes "classifier.pkl" and "train_classifier.py" for the Machine Learning model.
* README file
* Screenshot of web app and few graphs.

<img width="845" alt="direct_genre" src="https://user-images.githubusercontent.com/81413089/126501572-c5c9c5c9-a3f3-4e39-8a36-81acfaf8f38a.PNG">

<img width="848" alt="message categories" src="https://user-images.githubusercontent.com/81413089/126501617-1c3f3c89-165f-4118-b2ae-e00bb87fbf36.PNG">

## Running Instructions
* Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

* Run the following command in the app's directory to run your web app.
    `python run.py`

* Go to http://0.0.0.0:3001/

## Licensing, Authors, Acknowledgements
Many thanks to Figure-8 for making this available to Udacity for training purposes. Special thanks to udacity for the training. 
Feel free to utilize the contents of this while citing me, udacity, and/or figure-8 accordingly.

#### Notice : Some codes are picked from stackoverflow data.
#### Click [here](https://github.com/rachit1010/Disaster-Response-Pipeline) to check repository.


