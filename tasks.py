import mute_alsa
import speech_recognition as sr
import subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from pynput.keyboard import Controller as KeyboardController
import time

#global driver 
#option = webdriver.ChromeOptions()
#otions.add_argument("--user-data-dir=/home/red/.config/google-chrome/default")



def recognize_speech():
    with sr.Microphone() as source:
        recognizer = sr.Recognizer() 
        recognizer.adjust_for_ambient_noise(source)
        print("Say something...")
        audio = recognizer.listen(source)
    try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
    except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""

def activate_grid(row, col):  
    # Find a way to get resulotion automatically
    SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
    NUM_ROWS, NUM_COLUMNS = 8, 8
    QUADRANT_WIDTH = SCREEN_WIDTH // NUM_COLUMNS
    QUADRANT_HEIGHT = SCREEN_HEIGHT // NUM_ROWS
    x = col * QUADRANT_WIDTH
    y = row * QUADRANT_HEIGHT
    pyautogui.moveTo(x + QUADRANT_WIDTH // 2, y + QUADRANT_HEIGHT // 2)


def scroll_up():
    pyautogui.scroll(+20)

def scroll_down():
    pyautogui.scroll(-20)

def open_tasks():
    change_directory = "cd /home/red/repos/tasks/"
    activate_venv = ". /home/red/repos/tasks/tasks/bin/activate"
    command_within_venv = "jupyter notebook"
    combined_command = f"{change_directory} && {activate_venv} && {command_within_venv}"
    result = subprocess.Popen(combined_command, shell=True)

def open_text_editor():
    # Use subprocess to run the gedit command as a separate process
    subprocess.Popen(['gedit'])
    time.sleep(1)  # Wait for the text editor to open

def create_text_document():
    with subprocess.Popen(['gedit']) as process:
        # Wait for the process to complete (this will wait until you close the text editor)
        process.wait()
    #time.sleep(1)  # Wait for the new document to open

def write_text(text):
    keyboard = KeyboardController()
    keyboard.type(text)

def stage_questions():
    open_text_editor()
    write_text("Stage Questions")
    print("Text document created with 'Stage Questions' written.")

def open_vsc():
    subprocess.Popen(['code'])
    
def open_chatgpt():
    global driver
    options = webdriver.FirefoxOptions()
    options.profile = "/home/red/.mozilla/firefox/cb6ump6i.default"
    driver = webdriver.Firefox(options=options)
    driver.get("https://chat.openai.com")

def skip_ads():
    screen_width, screen_height = pyautogui.size()
    click_x = screen_width - 550
    click_y = screen_height - 260
    pyautogui.click(click_x, click_y)
      

def process_input(input_text):
    input_text = input_text.lower()
    selected_option = passphrase.get(input_text)
    if selected_option:
        selected_option()
    else:
        print("Invalid Option")

passphrase = {
    "open tasks" : open_tasks,
    "stage questions": stage_questions,
    "open visual studio code": open_vsc,
    "scroll up": scroll_up,
    "scroll down": scroll_down,
    "open chat": open_chatgpt,
    "skip ads" : skip_ads,
            # NEED A BETTER WAY OF DOING THE FOLLOWING
    "activate a1": lambda: activate_grid(0,0),
    "activate a2": lambda: activate_grid(0,1),
    "activate a3": lambda: activate_grid(0,2),
    "activate a4": lambda: activate_grid(0,3),
    "activate a5": lambda: activate_grid(0,4),
    "activate a6": lambda: activate_grid(0,5),
    "activate a7": lambda: activate_grid(0,6),
    "activate a8": lambda: activate_grid(0,7),
    "activate b1": lambda: activate_grid(1,0),
    "activate b2": lambda: activate_grid(1,1),
    "activate b3": lambda: activate_grid(1,2),
    "activate b4": lambda: activate_grid(1,3),
    "activate b5": lambda: activate_grid(1,4),
    "activate b6": lambda: activate_grid(1,5),
    "activate b7": lambda: activate_grid(1,6),
    "activate b8": lambda: activate_grid(1,7),
    "activate c1": lambda: activate_grid(2,0),
    "activate c2": lambda: activate_grid(2,1),
    "activate c3": lambda: activate_grid(2,2),
    "activate c4": lambda: activate_grid(2,3),
    "activate c5": lambda: activate_grid(2,4),
    "activate c6": lambda: activate_grid(2,5),
    "activate c7": lambda: activate_grid(2,6),
    "activate c8": lambda: activate_grid(2,7),
    "activate d1": lambda: activate_grid(3,0),
    "activate d2": lambda: activate_grid(3,1),
    "activate d3": lambda: activate_grid(3,2),
    "activate d4": lambda: activate_grid(3,3),
    "activate d5": lambda: activate_grid(3,4),
    "activate d6": lambda: activate_grid(3,5),
    "activate d7": lambda: activate_grid(3,6),
    "activate d8": lambda: activate_grid(3,7),
    "activate e1": lambda: activate_grid(4,0),
    "activate e2": lambda: activate_grid(4,1),
    "activate e3": lambda: activate_grid(4,2),
    "activate e4": lambda: activate_grid(4,3),
    "activate e5": lambda: activate_grid(4,4),
    "activate e6": lambda: activate_grid(4,5),
    "activate e7": lambda: activate_grid(4,6),
    "activate e8": lambda: activate_grid(4,7),
    "activate f1": lambda: activate_grid(5,0),
    "activate f2": lambda: activate_grid(5,1),
    "activate f3": lambda: activate_grid(5,2),
    "activate f4": lambda: activate_grid(5,3),
    "activate f5": lambda: activate_grid(5,4),
    "activate f6": lambda: activate_grid(5,5),
    "activate f7": lambda: activate_grid(5,6),
    "activate f8": lambda: activate_grid(5,7),
    "activate g1": lambda: activate_grid(6,0),
    "activate g2": lambda: activate_grid(6,1),
    "activate g3": lambda: activate_grid(6,2),
    "activate g4": lambda: activate_grid(6,3),
    "activate g5": lambda: activate_grid(6,4),
    "activate g6": lambda: activate_grid(6,5),
    "activate g7": lambda: activate_grid(6,6),
    "activate g8": lambda: activate_grid(6,7),
    "activate g1": lambda: activate_grid(7,0),
    "activate h2": lambda: activate_grid(7,1),
    "activate h3": lambda: activate_grid(7,2),
    "activate h4": lambda: activate_grid(7,3),
    "activate h5": lambda: activate_grid(7,4),
    "activate h6": lambda: activate_grid(7,5),
    "activate h7": lambda: activate_grid(7,6),
    "activate h8": lambda: activate_grid(7,7),

}

def main():
    

    while True:
        user_input = recognize_speech().lower()
        process_input(user_input)
        
      
    

if __name__ == "__main__":
    main()
