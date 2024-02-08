from text_to_speech.exception import TTSException
from text_to_speech.logger import logger
import sys

def get_accent_tld(user_input):
    """
    It takes a user input and returns the top level domain (tld) for the accent the user wants
    
    Args:
      user_input: The user's input.
    
    Returns:
      The tld is being returned.
    """
    try:
        accent_input = {
            'Australian': 'com.au',
            'South Africa': 'co.za',
            'British': 'co.uk',
            'Indian': 'co.in',
            'Canadian': 'ca',
            'Irish': 'ie',
            'Spanish': 'es'
        }
        tld = accent_input.get(user_input)
        return tld
    except Exception as e:
        raise TTSException(e, sys)

def get_accent_message():
    """
    It returns a list of accents.
    
    Returns:
      A list of accents
    """
    try:
        accent = ['Australian', 'South Africa', 'British',
                'Indian', 'Canadian', 'Irish', 'Spanish']
        return accent
    except Exception as e:
        raise TTSException(e, sys)from e