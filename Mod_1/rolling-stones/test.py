import json
import csv

with open('data.csv') as f:
    # we are using DictReader because we want our information to be in
    # dictionary format.
    reader = csv.DictReader(f)
    my_music = list(reader)

# open the text file in read
#text_file = open('top-500-songs.txt', 'r')
# read each line of the text file
# here is where you can print out the lines to your terminal and get an idea
# for how you might think about re-formatting the data
# lines = text_file.readlines()


file = open('track_data.json', 'r')
json_data = json.load(file)

json_data[0].keys()

for i in range(len(lines)):
    new_list = []
    final_list = []
    dic_list = []
    key = ['number', 'name', 'artist', 'year']
    # this is to split and to remove the \n caracter at the end of each sting
    #
    s1 = (lines[i].replace('\n', '\t'))
    new_list.append(s1.split('\t'))
    # eliminates the last empty object generated after spliting
    del new_list[i][-1]

    # make a dictionary with the new list and the keys
    #
    dic = {key[v]: new_list[i][v] for v in range(len(new_list[i]))}
    dic_list.append(dic)
