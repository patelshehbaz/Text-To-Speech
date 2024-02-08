from datetime import datetime

# constants for tts project
APPLICATION_NAME = 'text_to_speech'
ARTIFACT_DIR_KEY = 'artifact'
AUDIO_DIR = 'tts_audio'
TEXT_DIR = 'tts_text'

TEXT_FILE_NAME  = 'userinput.txt'

# Creating a timestamp for the current time.
fmt = "%Y-%m-%d %H%M%S"
CURRENT_TIME_STAMP = f"{datetime.now().strftime(fmt)}"