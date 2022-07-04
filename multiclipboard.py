from click import command
import clipboard
import sys
import json

data = clipboard.paste()
#print(data)

clipboard.copy('abc')

print(sys.argv)

#to save the data object(key-value pairs) to a filepath using json.dump 

def save_data(filepath, data):
    with open(filepath, 'w') as f: #arg 'w' so the data overwrites the filepaths contents 
        json.dump(data, f)

#save_data('test.json', {'key':'value'})

#read json file
def load_json(filepath):
    try:               #exception hadling so we can create an empty json file incase we dont have input
     with open(filepath, 'r') as f:
        data = json.load(f)
        return data
    except:
        return {}

SAVED_DATA = 'clipboard.json'


if len(sys.argv) == 2:  #argv gives all argument with the python cmd
    command = sys.argv[1]
    data = load_json(SAVED_DATA)
    print('Data Saved!')

    if command == 'save': #to save a data to the clipboard or overwrite whtever is in the clipboard with data[key]
        key = input('Enter a Key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)

    elif command == 'load':   #this is to check if the key entered is in the data and return thr key
        key = input('Enter a Key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data Copied to clipboard.')
        else: 
            print('Key does not exist.')
    elif command == 'list':
        print(data)
    else:
         print('Unknown Command.')
else:
    print('Please enter exactly one command.')


