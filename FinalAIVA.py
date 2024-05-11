# Importing the necessary libraries for the program
# Pyttsx3 library is used for text-to-speech conversion
import pyttsx3

# Speech_recognition library is used for speech recognition
import speech_recognition as sr

# Mysql.connector library is used to connect to a MySQL database
import mysql.connector

# Wikipedia library is used to retrieve information from Wikipedia
import wikipedia


# listen_to_voice() function is used to listen to the user's voice input
def listen_to_voice():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    
    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Say your query:")
        # listen for the user's voice
        audio = r.listen(source)
        
    try:
        # Using google to recognize speech
        return r.recognize_google(audio)
    except:
        # If speech is not recognized, return an empty string
        return ""


# search_html_tag() function is used to search for the specified HTML tag in the database
def search_html_tag(tag):
    # Connecting to the MySQL database using the provided credentials
    connection = mysql.connector.connect(user='root', password='HelloSir@SQL420', host='localhost', database='mysql')
    cursor = connection.cursor()
    
    # Constructing the SQL query to search for the specified HTML tag in the database
    query = "SELECT * FROM keshav_html WHERE tag ='" + tag + "';"
    
    # Executing the SQL query
    cursor.execute(query)
    
    # Fetching the result of the query
    result = cursor.fetchone()
    
    # If a result is found, return the result
    if result:
        return result
    else:
        # If no result is found, return None
        return None


# speak_output() function is used to convert the given text to speech using the pyttsx3 library
def speak_output(output):
    # Initializing the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Speaking the given output
    engine.say(output)
    
    # Running and waiting for the output to be spoken completely
    engine.runAndWait()

# search_on_wikipedia() function is used to search for the given tag on Wikipedia
def search_on_wikipedia(tag):
    try:
        # Searching for the summary of the given tag on Wikipedia
        result = wikipedia.summary(tag, sentences=5)
        
        # If the search is successful, return the result
        return result
    except:
        # If the search is unsuccessful, return an error message
        return "Error searching for information on " + tag + " on Wikipedia."


'''
This code is the main function of the voice assistant program.
It starts by greeting the user and asking for their name.
Then, it asks the user if they would like to input their query through voice or text.
If the user chooses 'voice', the program listens for their query and stores it in a variable.
If the user chooses 'text', the program prompts the user to type their query and stores it in a variable.
The query is then passed to the search_html_tag function to search for any HTML tags.
If a result is found, it will be returned and displayed.
'''
def main():
    print("Hello, I'm AIVA. Your Artificial Intelligence Voice Assistant.")
    speak_output("Hello, I'm AIVA. Your Artificial Intelligence Voice Assistant.")
    speak_output("What is Your Name?")
    name = input("What is your name: ")
    speak_output("Hello " + name + "!")
    while True:
        speak_output("\n you like to input your query through voice or text?")
        print("Would you like to input your query through voice or text?")
        voice_or_text = input("Type 'voice' or 'text': ")

        if voice_or_text == "voice":
            speak_output("Say your Querry!")
            query = listen_to_voice()
        else:
            speak_output("Type your Querry!")
            print("\nNOTE:")
            print("If you're looking to learn about HTML tags, simply type in the tag name with the brackets, for example <HTML>")
            print("and you'll get information about that specific tag.")
            print("For any other inquiries, feel free to search normally and our voice assistant will do its best to provide you with relevant information.")
            print("Thank you for using our program and we hope it helps with your HTML needs.")
            query = input("\nType Your Query: ")
            result = search_html_tag(query)


        if result:
            print("\nTag name: " + str(result[1]) + "\nDescription: " + str(result[2]) + "\nExample: " + str(result[3]))
            speak_output("Tag name: " + str(result[1]) + "\nDescription: " + str(result[2]))
        else:
            speak_output("Searching on wikipedia...")
            result = search_on_wikipedia(query)
            first_paragraph = result.split('\n')[0]
            speak_output(first_paragraph)
            print("\nAccording to Wikipedia: " + result)
            
        speak_output("Would you like to search for another query?")
        another_search = input("\nWould you like to search for another query? (yes/no) ")
        if another_search == "no":
            speak_output("Thank you for using AIVA! Have a great day.")
            print("\nThank you for using AIVA! Have a great day.")
            print("We would like to acknowledge and give credit to all those who have contributed to the creation and development of this Project.")
            print("The program is version 1.0 and we are would love to continuously working to improve it.")
            print("Our goal is to provide the best user experience and we believe that the best is yet to come.")
            print("\nCopyright © 2023 by KESHAV VYAS. All rights reserved.")

            break

'''
This line of code is checking if the current script
is being executed as the main program.
If it is, then it will run the main() function.
If not, it means that the script is being imported as a
module into another program and the main() function will not be executed.
'''

if __name__ == "__main__":
    main()
