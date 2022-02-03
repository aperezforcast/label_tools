import os
import json

# File extensions
njson = '.json'
xmljson = '.xml.json'

# CHANGE THESE VALUES TO FIT YOUR FORMAT
width = 1920 
height = 1080

# After reformulation, the code no longer replaces existing files, but the messages are pretty so i kept them
print('\033[91m **************D A N G E R********************\033[0m')
print(' \033[93mDO NOT RUN THIS SCRIPT MORE THAN ONCE IN THE SAME FOLDER')
print(' ARE YOU SURE YOU WANT TO NORMALIZE YOUR JSONS?\033[0m')
input('\033[5mPress enter to continue: \033[0m')
print ("\033[A                                     \033[A")

for i in range(100000):
    if (os.path.isfile(str(i) + njson)):
        path = str(i) + njson
    elif (os.path.isfile(str(i) + xmljson)):
        path = str(i) + xmljson
    else:
        continue
    data = json.loads(open(path,'r').read())

    ### Test code / Ignore
    """print(data[0]['annotations'][0]['coordinates']['x']/width)
    print(data[0]['annotations'][0]['coordinates']['y']/height)
    print(data[0]['annotations'][0]['coordinates']['width']/width)
    print(data[0]['annotations'][0]['coordinates']['height']/height)
    break"""
    ###

    data[0]['annotations'][0]['coordinates']['x'] /= width
    data[0]['annotations'][0]['coordinates']['y'] /= height
    data[0]['annotations'][0]['coordinates']['width'] /= width
    data[0]['annotations'][0]['coordinates']['height'] /= height

    path = str(i) + njson
    json.dump(data, open('normalized_' + path, 'w'))


print('Json normalized.')
print('\033[92mDone.\033[0m')