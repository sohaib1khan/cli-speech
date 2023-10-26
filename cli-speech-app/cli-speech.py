import pyttsx3
import subprocess
import threading

# ASCII Art
eyes_art = """
    .--.      
   |o_o |     
   |:_/ |     
  //   \ \    
 (|     | )   
/'\_   _/`\   
\___)=(___/   
"""

print(eyes_art)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Adjust the speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Decrease the rate by 50 units

# Fetch available voices
voices = engine.getProperty('voices')

# Set a specific voice by its ID
chosen_voice_id = voices[17].id  # Example: choose the 18th voice (0-based indexing)
engine.setProperty('voice', chosen_voice_id)

shell_process = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def execute_command(command):
    try:
        # Execute the command and return the output with a timeout of 10 seconds
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            stdout, stderr = process.communicate(timeout=15)  # Set a timeout of 10 seconds
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            return "Command timed out"

        if process.returncode != 0:
            return "Error: " + stderr
        return stdout.strip()
    except Exception as e:
        return str(e)


def listen_for_command():
    with open('/tmp/command_pipe', 'r') as pipe:
        while True:
            command = pipe.readline().strip()
            if command:
                # Execute command and get the output
                output = execute_command(command)

                # Print and read out the result
                print(f"Command: {command}")
                print(f"Output:\n{output}\n")
                engine.say(output)
                engine.runAndWait()

# Run the listener function in a new thread
threading.Thread(target=listen_for_command).start()

# Usage: python cli-speech.py
