import json
# difflib -> for comparing directories and files. can produce difference information in various formats
# get_close_matches (word, possibilities(list in which to search for close matches of word), n(maximum number of close matches), cutoff)
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? enter Y if yes, or N if no : " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. please double check it"
        else:
            return "We didn't understand yoy query"
    else:
        return "The word doesn't exist. please double check it"

word = input("Enter word :")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
