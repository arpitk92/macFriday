import json
import os

import speech_recognition as sr


class Utils:
    def __init__(self):
        with open("settings.json", "r") as content:
            self.setting = json.load(content)

    def getMicrophoneList(self):
        r = sr.Recognizer()
        mic_list = sr.Microphone.list_microphone_names()
        return mic_list

    def getMicrophoneID(self, mic_name):
        mic_list = self.getMicrophoneList()
        for i, microphone_name in enumerate(mic_list):
            if microphone_name == mic_name:
                return i
        return None

    def getVoiceList(self):
        # using say command of mac 
        cmd = "for voice in `say -v '?' | awk '{print $1}'`; do echo \"Voice of $voice.\"; say -v \"$voice\" \"Hello, my name is $voice.\"; done"
        os.system(cmd)

    def changeVoice(self, name):
        # reading the content and changing it
        content = open("settings.json", "r")
        setting = json.load(content)
        setting["voice"]["default"] = name
        content.close()

        # rewriting the content of json file
        content = open("settings.json", "w")
        content.truncate()
        content.write(str(json.dumps(setting)))
        content.close()

    def wish(self):
        greetings = ""
        from datetime import datetime as dt
        currentTime = dt.now()

        if currentTime.hour < 12:
            greetings = "Good Morning sir. "
        elif 12 <= currentTime.hour < 18:
            greetings = "Good afternoon sir. "
        else:
            greetings = "Good evening sir. "

        intro = "I am {}. ".format(self.setting["voice"]["name"])

        msg = "Tell me how can i help you?"

        return greetings+intro+msg
