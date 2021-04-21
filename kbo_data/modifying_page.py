""" 가져온 KBO 자료를 DB에 저장하기 위한 모듈

"""

import json
import pandas as pd

def get_date(record_dict):
    date = record_dict.keys()[0]
    full_date = date[0:4]+"-"+date[4:6]+"-"+date[6:8]
    return full_date

def get_away_team(record_dict):
    return record_dict.keys()[0][9:11]

def get_home_team(record_dict):
    return record_dict.keys()[0][11:13]

def get_doubleheader(record_dict):
    return record_dict.keys()[0][13:]

def make_df(record_dict):
    df = pd.DataFrame({"date":get_date(record_dict),"away":get_away_team(record_dict),
              "home":get_home_team(record_dict),"doubleheader":get_doubleheader(record_dict)},index =[0])
    return df
