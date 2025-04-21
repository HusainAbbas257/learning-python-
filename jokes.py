import pyjokes
import pyttsx3
jokes=pyjokes.get_joke()
print(jokes)

engine =pyttsx3.init()
engine.say(jokes)
engine.runAndWait()