'''
Requirements:
In workon cv envirnment write the following
pip3 install pyrebase
pip3 install pyfcm
pip3 install requests
pip3 install python-firebase
'''

from firebase import firebase
import json
from pyfcm import FCMNotification
import pyrebase
import time

def send_alarm(src):
    config = {
        "apiKey": "AAAAXDKjDeY:APA91bHLONjob43L-tynyMAicqee38C9yuAo6rZFdlc25zmCmmnqyrcyG7NIugNLECKIU2q4QpyNPTzN0NsJHTm8SyiuzJOxzL5JPmHwIoJO7LrYDboUJU0-115EXKWpK8vLVJor1-Pi",
        "authDomain": "homeattender.firebaseapp.com",
        "databaseURL": "https://homeattender.firebaseio.com/",
        "storageBucket": "homeattender.appspot.com"
    }
    #base firebase setup
    firebase = firebase.FirebaseApplication('https://homeattender.firebaseio.com/', None)
    push_service = FCMNotification(api_key=config["apiKey"])
    registration_id = "cp5OKaH4C_Y:APA91bEtcHMcJINecS8SpGYMckeO_Jj9HYwyrQXs4jGBObxgrT8yGCYmdh0JHVE4VP0Q0MmlGxH-OOC6ixT9pFNkqfivOke-nTXanJnhbyVkVBK28bT7KMhSH_Mun3SuWRj14xH58e0V3ZAJLpsFFds8BwFjbyXbnQ"
    #picture pyrebase setup to send from rasp to phone
    pyrebase = pyrebase.initialize_app(config)
    storage = pyrebase.storage()

    #PUSH
    file_sorce = sprintf(image_name, "/home/pi/lip/LeotonModule/fire_%.4d.jpg", src);
    picture_name = "fire{}.png".format(time.strftime("%Y%m%d-%H%M%S"))
    storage.child(picture_name).put(src)
    time=""
    msg = "Fire detected!".time
    firebase.patch('/FireAlarm', {'Info': msg, 'PicName': picture_name})
    
    #NOTIFICATION
    message_title = "FIRE"
    message_body = "FIRE HAS BEEN DETECTED"
    firebase.patch('/', {'Alert': 'off'})
    push_service.notify_single_device(registration_id=self.registration_id, message_title=message_title,
                                                   message_body=message_body)
    return '0'


def get_intruder():
    firebase = firebase.FirebaseApplication('https://homeattender.firebaseio.com/', None)
    r = firebase.get('/Fire', None)
    if(r=='True')
        return '1'
    else
        return '0'