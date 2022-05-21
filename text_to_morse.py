import time
import librosa
from playsound import playsound

DIT = 'sounds/dit.wav'
DAH = 'sounds/dah.wav'

DIT_LEN = librosa.get_duration(filename=DIT)
DAH_LEN = librosa.get_duration(filename=DAH)

morse_code = {
    'a': '·−',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '----- ',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----. ',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    ';': '-.-.-.',
    ':': '---...',
    '—': '-....-',
    '/': '-..-.',
    "'": '.----.',
    '"': '.-..-.',
    ' ': '/',
}


def convert_to_morse(text):
    """Convert text input to morse code.

    Accept only English alphabet letters and Arabic numerals.

    Parameters
    ----------
    text : str

    Raises
    ----------
    ValueError
        if character is not within the morse_code dict variable (no English
        letter, Arabic numeral, punctuation mark or space.

    Return a string.
    """
    morse_output = ""
    for char in text.lower():
        for k in morse_code:
            if char == k:
                morse_output += (morse_code[k] + " ")
                break
            else:
                if k == ' ':
                    raise ValueError(
                        "Only English alphabet letters, arabic numerals, "
                        "punctuation marks and spaces are allowed."
                        f"Input character: {char}"
                    )

    return morse_output


def play_morse_code(encoded_text):
    """Convert encoded text to sound

    Parameters:
    encoded_text : str
    """
    for char in encoded_text:
        if char == '.':
            playsound(DIT)
        elif char == '-':
            playsound(DAH)
        elif char == ' ':
            time.sleep(DIT_LEN)
        else:
            time.sleep(DIT_LEN * 3)


encoded_text = convert_to_morse('Daga Knesz')
