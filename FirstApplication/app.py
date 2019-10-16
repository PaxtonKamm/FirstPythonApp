import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def getDefinition(word):
    if word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word.lower(),data.keys())) > 0:

        print("Oops, could not find the word you are looking for. Did you mean %s or %s?" % (get_close_matches(word.lower(), data.keys())[0],get_close_matches(word.lower(), data.keys())[1]))
        w = input("Re-Enter your word: ")
        return getDefinition(w)
    else:
        return("Not a word, please type in something else.")

word = input("Enter a word: ")

output = getDefinition(word)

if type(output) == list:
    for item in output:
     print(item)
else:
    print(output)