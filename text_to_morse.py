import librosa

from morse_code_tool import MorseCodeTool

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


morse_code_tool = MorseCodeTool(dit=DIT, dah=DAH, dit_len=DIT_LEN,
                                dah_len=DAH_LEN, morse_code=morse_code)
encoded_text = morse_code_tool.convert_to_morse('Daga Knesz')

morse_code_tool.play_morse_code(encoded_text)