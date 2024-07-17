import pyttsx3

txt_speech = pyttsx3.init()

answer = input("SAY ANYTHING:")
txt_speech.say(answer)
txt_speech.runAndWait()

