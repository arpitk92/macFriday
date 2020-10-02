import json
import os
import time
import speech_recognition as sr
import wikipedia

from actions import Utils


class ItsFriday:

    def __init__(self):
        with open("settings.json", "r") as content:
            self.setting = json.load(content)
        self.current_voice = self.setting["voice"]["default"]

    def speak(self, audio):
        command = "say -v {} '{}'".format(self.current_voice, audio)
        os.system(command)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index=self.setting["microphone"]["default_device_id"],
                           sample_rate=self.setting["microphone"]["sample_rate"],
                           chunk_size=self.setting["microphone"]["chunk_size"]) as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio)  # Using google for voice recognition.
                print(f"User said: {query}\n")

            except Exception as e:
                print("Say that again please...")
                return "None"  # None  will be returned
        return query

    @staticmethod
    def takeAction(action):
        utils = Utils()
        action = action.lower()
        print("Executing Action")
        if 'wikipedia' in action:
            ItsFriday().speak("Searching Wikipedia")
            action = action.replace("wikipedia", "")
            results = wikipedia.summary(action, sentences=2)
            print(results)
            ItsFriday().speak(results)
        if 'get microphone list' in action:
            mic_list = utils.getMicrophoneList()
            print(mic_list)
            ItsFriday().speak("The list is as follows {}".format(mic_list))

        if 'get voice list' in action:
            utils.getVoiceList()

        if 'change voice to' in action:
            action = action.replace("change voice to", "")
            utils.changeVoice(action.strip())
            ItsFriday().speak("Voice changed successfully")

        if 'shutdown' in action:
            quit()
