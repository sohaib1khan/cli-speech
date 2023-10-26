# CLI-Speech

The `cli-speech` project allows users to execute shell commands, receive visual output, and also get auditory feedback using a text-to-speech system. It utilizes `pyttsx3` for speech synthesis and handles command execution using Python's subprocess module.

## equirements

- Python 3
- Bash shell
- Virtual environment (recommended)

## Setup

### 1. Clone the Repository

Assuming you've already obtained the repository:

```
cd path/to/repository
```

### 2. Create a Virtual Environment

For isolation, it's recommended to run the program within a virtual environment:

```
python3 -m venv cli-speech-env
```

Activate the virtual environment:

```
source cli-speech-env/bin/activate
```

### 3. Install Dependencies

The main dependency for this project is `pyttsx3`, which can be installed via pip:

```
pip install pyttsx3
```

### 4. Permissions for Bash Script

Ensure that the bash script `run_cli_speech.sh` is executable:

```
chmod +x run_cli_speech.sh
```

### 5. Create Named Pipe

This program communicates between the bash script and the Python script via a named pipe. To set this up:

```
mkfifo /tmp/command_pipe
```

## Running the Program

Once everything is set up, you can run the program using the bash script:

```
./run_cli_speech.sh
```

## Files Overview

- `cli-speech.py`: The main Python script that handles command execution and speech synthesis.
- `run_cli_speech.sh`: A bash script to interface with the user and relay commands to the Python script.
- `voices.py` (if present): A script to list and test available voices for speech synthesis.
- Other directories such as `bin`, `include`, `lib`, `lib64`, and `pyvenv.cfg` relate to the virtual environment and can be ignored for the project's functionality.