import argparse
import json
import pandas as pd
import dive_tools as dt


def import_json(path):
    try:
        f = open(path, 'r')
        data = json.load(f)
        return data
    except Exception as e:
        print(e)
        print('There was an issue importing your json file')
        return 

# vars
json_path = '/home/jennaehnot/Desktop/dive_tools/redball_150cmH/annotations.dive.json'
img_path = '/home/jennaehnot/Desktop/dive_tools/redball_150cmH/frames/rb150_1.png'
path2labels= '/home/jennaehnot/Desktop/dive_tools/redball_150cmH/labels/'
name_conv ='rb150_'


json_data = import_json(json_path)

data = dt.JSONData(json_data)

data.make_labelfiles(img_path, path2labels, name_conv)
print("Done ! :) ")