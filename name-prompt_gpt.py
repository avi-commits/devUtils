# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import sys

openai.api_key = "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"

def prompt_gpt(prompt):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},

        {"role": "user", "content": prompt}
     ]
    )
    return response

prompt = str(sys.argv[1])
result = prompt_gpt(prompt)

content = result["choices"][0]["message"]["content"]

#take content and split it into a list
content = content.split("\n")

#remove the first 3 characters of each element in the list
content = [x[3:] for x in content]

print(content)

#print(result["choices"][0]["message"]["content"])
print("Prompt Tokens Used: " + str(result["usage"]["prompt_tokens"]))
print("Completion Tokens Used: " + str(result["usage"]["completion_tokens"]))
print("Total Tokens Used: " + str(result["usage"]["total_tokens"]))