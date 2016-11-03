#mapping numbers as labelled on remote

keys = {
    '1': 'KEY_S',
    '2': 'key_TV',
    '3': 'KEY_POWER',
    '4': 'KEY_DVD',
    '5': 'KEY_AUX',
    '6': 'KEY_RECORD',
    '7': 'KEY_REWIND',
    '8': 'KEY_FORWARD',
    '9': 'KEY_VIDEO',
    '10': 'KEY_STOP',
    '11': 'KEY_PAUSE',
    '12': 'KEY_PLAY',
    '13': 'KEY_REPLY',
    '14': 'KEY_FRAMEFORWARD',
    '15': 'KEY_OPEN',
    '16': 'KEY_MENU',
    '17': 'KEY_R',
    '18': 'KEY_BACK',
    '19': 'KEY_SETUP',
    '20': 'KEY_A',
    '21': 'KEY_UP',
    '22': 'KEY_LEFT',
    '23': 'KEY_RIGHT',
    '24': 'KEY_DOWN',
    '25': 'KEY_OK',
    '26': 'KEY_EXIT',
    '27': 'KEY_INFO',
    '28': 'BTN_A',
    '29': 'BTN_B',
    '30': 'BTN_C',
    '31': 'KEY_VOLUMEUP',
    '32': 'KEY_VOLUMEDOWN',
    '33': 'KEY_G',
    '34': 'KEY_MUTE',
    '35': 'KEY_LAST',
    '36': 'KEY_CHANNELUP',
    '37': 'KEY_CHANNELDOWN',
    '38': 'KEY_1',
    '39': 'KEY_2',
    '40': 'KEY_3',
    '41': 'KEY_4',
    '42': 'KEY_5',
    '43': 'KEY_6',
    '44': 'KEY_7',
    '45': 'KEY_8',
    '46': 'KEY_9',
    '47': 'KEY_DELETE',
    '48': 'KEY_0',
    '49': 'KEY_ENTER',
}

#get remote name according to gap length
def getRemoteName(inputKey):
    keyEntered = int(inputKey)

    if(keyEntered == 15 or
       keyEntered == 21 or
       keyEntered == 22 or
       keyEntered == 23 or
       keyEntered == 24 or
       keyEntered == 25 or
       keyEntered == 27 or
       keyEntered == 31 or
       keyEntered == 32 or
       keyEntered == 33 or
       keyEntered == 34 or
       keyEntered == 35):
        remoteName = 'ARRIS_N'
    elif(keyEntered == 3 or
         keyEntered == 16 or
         keyEntered == 18 or
         keyEntered == 26):
        remoteName = 'ARRIS_BACL'
    elif(keyEntered == 17 or
         keyEntered == 20):
        remoteName = 'ARRIS_89'
    else:
        remoteName = 'ARRIS_2'

    return remoteName;
