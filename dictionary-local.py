import json
# import difflib
from difflib import get_close_matches
# from difflib import SequenceMatcher

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0 :
        yn = input("Did you mean \"%s\" instead? Yes / No: " % get_close_matches(w, data.keys())[0])
        if yn in ("YES", "Yes", "yes", "yES", "Y", "y"):
            return data[get_close_matches(w, data.keys())[0]]
        elif yn in ("NO", "No", "no", "nO", "N", "n"):
            return "The word \"%s\" doesn't exist in the dictionary" % w
        else:
            return "Entry is not understood :("
    else:
        return "The word \"%s\" doesn't exist in the dictionary" % w

word = input("Enter a word: ")
output = translate(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)