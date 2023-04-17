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

def generator(prompt):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"{prompt}"),
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.9,
    )
    return response["choices"][0]["text"]

game_asset = "dog"
prompt_part_1 = f"find the correct name for the {game_asset} and write a minecraft command block code to summon a "
prompt_part_2 = " that can pick up loots "
connector = "and "
prompt_part_4 = "give instant health for 100 seconds "

prompt = prompt_part_1 + game_asset + prompt_part_2 + connector + prompt_part_4
print(prompt)

#workflow part 1: genrate a command block code
generated_command = generator(prompt)
print(generated_command)

#workflow part 2: explain the code in simple english
explanation = "Please explain the code in simple english " + str(generated_command)
generated_explanation = generator(explanation)

explain_in_simple_english = f" Here's the explanation in english {generated_explanation}"
print(explain_in_simple_english)