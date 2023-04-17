# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import sys
import json

openai.api_key = "yyyyyyyyysxxxxxxxxxxxxxxxxxxxxxx"

'''
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
'''

'''

content = result["choices"][0]["message"]["content"]

#take content and split it into a list
#content = content.split("\n")

#remove the first 3 characters of each element in the list
#content = [x[3:] for x in content]

print(content)

#print(result["choices"][0]["message"]["content"])
print("Prompt Tokens Used: " + str(result["usage"]["prompt_tokens"]))
print("Completion Tokens Used: " + str(result["usage"]["completion_tokens"]))
print("Total Tokens Used: " + str(result["usage"]["total_tokens"]))

'''

def prompt_gpt(prompt, chat):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=chat
    )
    return response

#read the chat history from the file
#chat = open("chat.txt", 'r').read()
#convert the chat to the correct format. Example: [{'role': 'system', 'content': 'You are a helpful assistant.'}, 
# {'role': 'user', 'content': '"Suggest 3 names of a Minecraft rank"'}, 
# {'role': 'assistant', 'content': '1. Diamond Knight\n2. Emerald Champion \n3. Obsidian Master'}, 
# {'role': 'user', 'content': '"Write a 30 word description of the second rank"'}, 
# {'role': 'assistant', 'content': 'The Emerald Champion rank in Minecraft signifies
# a level of expertise that only a few players possess. With its 
# distinguished green emerald title, players at this rank embody 
# a well-rounded understanding of Minecraft gameplay and demonstrate 
# exceptional gameplay abilities.'}]



#chat = json.loads(chat)
#print(chat)

#chat = [{chat}]

#chat = [{"role": "system", "content": "You are a helpful assistant."}]
while True:
    #read the chat history from the csv file and convert it to the correct format
    chat = open("chat.csv", 'r').read()
    chat = chat.split("\n")
    chat = [x.split(";") for x in chat]
    chat = [{"role": x[0], "content": x[1]} for x in chat]


    question = input("Let's keep going? (y/n): ")
    if question == "n":
        break

    else:
        prompt = input("Enter prompt: ")
        print("First Prompt: " + prompt)
        chat.append({"role": "user", "content": prompt})

        result = prompt_gpt(prompt, chat)

        content = result["choices"][0]["message"]["content"]
        role = result["choices"][0]["message"]["role"]
        print("Content: " + content)
        print("Role: " + role)
        chat.append({"role": role, "content": content})

        print("Chat: " + str(chat))
        print("Total Tokens Used: " + str(result["usage"]["total_tokens"]))

        #write chat to a csv file where role is the first column and content is the second column
        with open("chat.csv", 'a') as f:
            f.write("\n" + role + ";" + content)
            f.close()

    if result["usage"]["total_tokens"] > 1000:
        break


