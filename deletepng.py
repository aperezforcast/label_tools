import os

png = '.png'
json = '.json'
xmljson = '.xml.json'

for i in range(100000):
    if(i < 10):
        if not (os.path.isfile('00' + str(i) + json) or os.path.isfile('00' + str(i) + xmljson)):
            if (os.path.isfile('00' + str(i) + png)):
                os.remove('00' + str(i) + png)
    elif(i < 100 and i >= 10):
        if not (os.path.isfile('0' + str(i) + json) or os.path.isfile('0' + str(i) + xmljson)):
            if (os.path.isfile('0' + str(i) + png)):
                os.remove('0' + str(i) + png)
    else:
        if not (os.path.isfile(str(i) + json) or os.path.isfile(str(i) + xmljson)):
            if (os.path.isfile(str(i) + png)):
                os.remove(str(i) + png)