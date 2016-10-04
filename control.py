import key_mapping
import os
import time
from key_mapping import keys
from key_mapping import getRemoteName
#from Pillow import Image

#image = Image.open('arrisremote_labelled.jpg')
#image.show()

print('Input a sequence to be transmitted; numbers are according to the printout')


print('Command numbers are labelled according to the image')

loop = '1'
while(loop == '1'):
    print('Please enter the command numbers separated by a space')
    command = raw_input()
    print(command + ' entered')
    command = command.split(' ')

    arraySize = len(command)

    print('continuous repeat sequence? y/n')
    
    repeat = raw_input()

    if(repeat == 'n'):
        time.sleep(0.5)
        toEnter = ('irsend SEND_ONCE ' + getRemoteName(command[0]) + ' ' + keys[command[0]])   
        os.system(toEnter)
        print('sent ' + toEnter)

    while(repeat == 'y'):
        print('Please enter seconds between each command')
        timeBetween = raw_input()
        print(timeBetween + ' second delay')
        timeBetween = float(timeBetween)

        for i in range(arraySize):
            time.sleep(timeBetween)
            toEnter = ('irsend SEND_ONCE ' + getRemoteName(command[i]) + ' ' + keys[command[i]])   
            os.system(toEnter)
            print('sent ' + toEnter)

        
