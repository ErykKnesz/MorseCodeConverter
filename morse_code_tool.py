import time
from playsound import playsound


class MorseCodeTool:

    def __init__(self, dit, dah, dit_len, dah_len, morse_code):
        self.dit = dit
        self.dah = dah
        self.dit_len = dit_len
        self.dah_len = dah_len
        self.morse_code = morse_code

    def convert_to_morse(self, text):
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
            for k in self.morse_code:
                if char == k:
                    morse_output += (self.morse_code[k] + " ")
                    break
                else:
                    if k == ' ':
                        raise ValueError(
                            "Only English alphabet letters, arabic numerals, "
                            "punctuation marks and spaces are allowed."
                            f"Input character: {char}"
                        )

        return morse_output

    def play_morse_code(self, encoded_text):
        """Convert encoded text to sound.

        Parameters:
        encoded_text : str
        """
        for char in encoded_text:
            if char == '.':
                playsound(self.dit)
            elif char == '-':
                playsound(self.dah)
            elif char == ' ':
                time.sleep(self.dit_len)
            else:
                time.sleep(self.dit_len * 3)