#!/usr/bin/python

import random

def generate_color():
    letters = '0123456789ABCDEF'
    color = '#'
    for i in range(6):
        color += random.choice(letters)
    return color

random_color = generate_color()

import openai

def generate_sentence(asset_name):
    openai.api_key = "OPEN AI API KEY GOES HERE"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Create an interesting sentence that describes the {asset_name} game asset."),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

game_asset = "Infinity Sword"
generated_sentence = generate_sentence(game_asset)
print(generated_sentence)

#write a csv reader in python

import csv

data = []

def read_csv_file(filepath, output_file):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        #header.append("generated_sentence") # Add new header column
        rows = [header] # Prepare the rows with the header
        for row in reader:
            #asset_name = row[1]
            #generated_sentence = generate_sentence(asset_name)
            #print(generated_sentence)
            #row[2] = generated_sentence
            row[17] = generate_color()
            print(row)
            #row.append(generated_sentence) # Append the generated sentence
            rows.append(row) # Append the modified row to the rows list
            #data.append(row)


    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)



if __name__ == "__main__":
    """ This is executed when run from the command line """

    filepath = "/Users/aviralchandra/Desktop/Sheets/Infinity_Potions _Final_1.csv"
    output_file = "/Users/aviralchandra/Desktop/Infinity_Potions _Final_1.csv"

    data = read_csv_file(filepath, output_file)
    #print(data)
