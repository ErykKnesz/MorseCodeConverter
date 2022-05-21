morse_code = {
    'a': '· −',
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
}


def convert_to_morse(text):
    morse_output = ""
    for char in text.lower():
        for k in morse_code:
            if char == k:
                morse_output += morse_code[k]
                break
            else:
                if k == 'z':
                    raise ValueError(
                        "Only English alphabet letters are allowed. "
                        f"Input character: {char}"
                    )

    return morse_output



