import pyjokes              # Imports the pyjokes library to get random programming jokes
import pyttsx3              # Imports the pyttsx3 library for text-to-speech conversion

jokes = pyjokes.get_joke()  # Fetches a random joke and stores it in the variable 'jokes'
print(jokes)                # Prints the joke to the console

engine = pyttsx3.init()     # Initializes the text-to-speech engine
engine.say(jokes)           # Queues the joke to be spoken aloud
engine.runAndWait()         # Runs the speech engine to speak the joke
