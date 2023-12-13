# Market value of a footballer
ML project about the market value of a football player. This is a Project for mlzoomcamp course by Datatalks ( https://datatalks.club/ )

![](images.jpg)

---

## 1 - Problem description

The football player market is an auction market in which teams buy and sell players of another team or as a free agent. 
There are two market session each year, that may change between each league. More or less, in Europe, those periods are: 
- Summer session, from 01 July to 01 September
- Winter session, from 01 january to 31 January
  
Players have training sessions and matches each week during the season.
Football players value depends on various parameters, like: player skill, potential, recent performance, residual contract duration, position and others. Everything matters to estimate an accurate transfer fee.

---
## 2 - The Goal

The target of this project is to predict the current value of a player.

--- 

## 3 - Data

This dataset has gathered information on players competing in several top-tier global football leagues:
- 11 European leagues, including the Premier League and Championship in England, Bundesliga in Germany, La Liga in Spain, Serie A in Italy, Ligue 1 in France, Eredivisie in the Netherlands, Liga NOS in Portugal, Premier Liga in Russia, Super Lig in Turkey, and Bundesliga in Austria.
- 4 American leagues, including Brasileiro in Brazil, Major League Soccer in the United States, Primera División in Argentina, and Liga MX in Mexico.
- 1 African league, namely the DStv Premiership in South Africa.
- 4 Asian leagues, comprising J-League in Japan, Saudi Pro League in Saudi Arabia, K-League 1 in South Korea, and A-League in Australia.

The data was obtained from this repository which processed the data from transfermarkt: https://www.kaggle.com/datasets/khanghunhnguyntrng/football-players-transfer-fee-prediction-dataset

Important details about the data:
- player: the link to the Transfermarkt page contains player data (you should add a prefix "www.transfermarkt.com/" to further navigating).
- team: name of the team that player played for, at the time data was collected.
- name: name of the player.
- position: position where the player played most.
- height: height of player, in cm unit.
- age: age of the player.
- appearance: the number of times a player appear on field.
- goals: goals scored.
- assists: assits to goals.
- yellow cards: number of yellow card.
- second yellow cards: number of time the player got 2 yellow card in 1 match.
- red cards: number of red card.
- goals conceded: gol took (only for a Goalkeeper, zero for the others).
- clean sheets: number of match where the goalkeeper took 0 goals.
- minutes played: number of minutes played during the monitor time.
- days_injured: days he stayed injured.
- games_injured: missed game for injuries.
- award: total awarđ in whole career.
- current_value: valuated price, Euro unit.
- highest_value: highest valuated price in the past, Euro unit.
- position_encoded: 0: galkeeper – 1: Defender – 2: midfield – 3: Attack
- winger: 1: winger, 0: not a winger.

I uploaded the entire dataset to the repository. File: *player_data.csv* in the data directory.
This data is processed using the ``train.py`` file archive in the main folder.

After EDA, i decided to delete some columns based on the redundant value already present in the dataset. I cut:
- winger: info already present in the position
- position_encoded: info already present in the position
- player: Link to transfermarket. 

---

## 4 - Structure of the repository

### DATASET
- **player_data.csv**: contains the full dataset, it is in folder named 'data'

### Files
- **Proj1.ipynb**: contains the notebook to explore the data and choose the model with the best results
- **Pipfile and Pipfile.lock**: contains the dependencies to run the repo
- **predict.py**: contains the prediction using flask
- **test.py**: contains some values to test the model
- **player_model.bin**: this is the model got from the train.py using Pickle
- **train.py**: contains the model with the best performance in the testing set, obtained using the notebook
- **Dockerfile**: contains the image for the docker

### Folder '**Proof of working**'
- **docker running.png**: screenshot of the docker built running
- **docker_running.mp4**: video of the docker built running and the prediction
- **flask running.png**: screenshot of the flask app running in local
- **flask_running.mp4**: video of the flask built running and the prediction
- **gunicorn running.mp4**: video of the gunicorn built running and the prediction

---
## 5 - Loading final model in web service:

#### pipenv 

The script *train.py* load the model : *player_model.bin* and it can run in a separate virtual environment across its dependency files *Pipenv* and *Pipenv.lock*.
*flask* was used for the local web deployment in *train.py* script.

- Install pipenv :
```
pip install pipenv
```
- Get a copy of project and dependencies, or clone the repository :
```
git clone https://github.com/bergimax/footballer-value/
```
- From the project's folder, run :
``` 
pipenv install
```
- All the dependencies should be automatically soddisfied, just verify.
- Run the web service using gunicorn inside the virtual environment:
```
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```

#### Docker
There is also the file: *Dockerfile* in the repository, through this you can run the service in a completely separate container. To run the Docker, be sure your docker service is running. If you are using wsl2 on Windows, to run the build command you need to make sure your docker dekstop is running, otherwise you will get an error. 
For the docker, you have to:

- From the project directory, create the docker image :
```
docker build -t player_prediction .
```
- Run the docker image created:
```
docker run -it --rm -p 9696:9696 player_prediction:latest
```

#### Test the local web service:

- To test the local web service, you can run the test script in another terminal:
```
python test.py
```
- If you edit the market values to analize some data, you should modify the parameters in the file test.py, maybe you cane take them from the smaller dataset present in this repo of each market:
```
vi test.py
```
P.S: The current values in test.py are taken from the dataset, raw number 2075.

---

#### Video of the service running :
I loaded a small video where you can see how the service works, everything it's in the 'Proof of working' folder.

The video show the local service starting in Docker and how it respond to the test.py
I also attached the screenshot of the service running with flask and gunicorn.
