import os

png = '.png'
json = '.json'
xmljson = '.xml.json'

for i in range(100000):
    if(i < 10):
        if  (os.path.isfile('00' + str(i) + json)):
            os.remove('00' + str(i) + json)
        if  (os.path.isfile('00' + str(i) + xmljson)):
            os.remove('00' + str(i) + xmljson)
    elif(i < 100 and i >= 10):
        if  (os.path.isfile('0' + str(i) + json)):
            os.remove('0' + str(i) + json)
        if  (os.path.isfile('0' + str(i) + xmljson)):
            os.remove('0' + str(i) + xmljson)
    else:
        if (os.path.isfile(str(i) + json)):
            os.remove(str(i) + json)
        if (os.path.isfile(str(i) + xmljson)):
            os.remove(str(i) + xmljson)