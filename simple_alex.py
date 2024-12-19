import speech_recognition as sr

#  text to speach conversion in python(pyttsx3)
import pyttsx3

# PyAudio
# PyWhatKit
# PyJokes
# Wikipedia
# OpenweatherApi


# listener = sr.Recognizer()
engine = pyttsx3.init()
def listen():
    recognizer = sr.Recognizer()  # Create an instance of Recognizer
    with sr.Microphone() as source:  # Create an instance of Microphone
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        voice = recognizer.listen(source)  # Capture audio from the microphone
        

    try:
        command = recognizer.recognize_google(voice)  # Use Google Speech Recognition
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
        return None



def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant said: ",text)
    
speak("hello! How are you")

while True:
    command = listen()
    if "hello" in command.lower():
        speak("Hello! how may i assist you?")
    elif "good bye" in command.lower():
        speak("Goodbye!")
        break
    else:
        speak("Sorry, I don't know how to respond.")