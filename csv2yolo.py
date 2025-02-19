import csv
import dive_tools as dt

csv_path = '/home/jennaehnot/Desktop/dive_tools/redball_150cmH/annotations.viame.csv'
img_path = '/home/jennaehnot/Desktop/dive_tools/redball_150cmH/frames/rb150_1.png'
path2labels= '/home/jennaehnot/Desktop/dive_tools/redball_150cmH/labels/'
name_conv ='rb150_'

try:
    with open(csv_path, 'r') as csv_file:
        for line in csv_file:
            if line[0] != '#':
                data = dt.CSVData(line)
                data.make_labelfiles(img_path, path2labels, name_conv)
except Exception as e:
    print(e)





