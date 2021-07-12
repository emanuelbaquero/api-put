import requests
import json
import pandas as pd
import os



post_data = {"username":"ema@gmail.com","password":"123"}
respuesta = requests.post("https://flask-api-requests-post-tgpcxkofza-ue.a.run.app/requests",json=post_data)
respuesta.json()['token']

