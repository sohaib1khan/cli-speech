#!/bin/bash

# Start the Python script in the background
python3 cli-speech.py &

# Infinite loop to prompt user for commands
while true; do
    # Prompt the user for a command
    read -p "Enter command: " user_command

    # If the user types "exit", break out of the loop and exit
    if [ "$user_command" == "exit" ]; then
        break
    fi

    # Echo the user's command to the named pipe
    echo "$user_command" > /tmp/command_pipe
done

# Optionally kill the background python process when done
# Note: This assumes only one python process is running, adjust as necessary
kill $(pgrep python)
