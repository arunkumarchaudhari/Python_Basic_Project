import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y"  or decide =='Y':
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n" or decide =='N':
            return("No data found with the given word, Please try with some other input...")
        else:
            return("Enter either y or n")
    else:
        print("No data found with the given word, Please try with some other input...")


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
