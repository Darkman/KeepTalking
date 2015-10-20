class MorseCode:
    morse_code = {
        '.-':   'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':  'D',
        '.':    'E',
        '..-.': 'F',
        '--.':  'G',
        '....': 'H',
        '..':   'I',
        '.---': 'J',
        '-.-':  'K',
        '.-..': 'L',
        '--':   'M',
        '-.':   'N',
        '---':  'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.':  'R',
        '...':  'S',
        '-':    'T',
        '..-':  'U',
        '...-': 'V',
        '.--':  'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
    }

    frequencies = {
        'shell': '3.505 MHz',
        'halls': '3.515 MHz',
        'slick': '3.522 MHz',
        'trick': '3.532 MHz',
        'boxes': '3.535 MHz',
        'leaks': '3.542 MHz',
        'strobe': '3.545 MHz',
        'bistro': '3.552 MHz',
        'flick': '3.555 MHz',
        'bombs': '3.565 MHz',
        'break': '3.572 MHz',
        'brick': '3.575 MHz',
        'steak': '3.582 MHz',
        'sting': '3.592 MHz',
        'vector': '3.595 MHz',
        'beats': '3.600 MHz',
    }

    def __init__(self):
        self.letters = set()

    def run(self):
        while True:
            code_letter = input('Input morse code letter (./-) > ')
            if code_letter == '':
                break

            if self._is_morse(code_letter, self.morse_code):
                letter = self.morse_code[code_letter].lower()
                self.letters.add(letter)
            else:
                print('Not morse code')
                continue

            matches = self._get_matches(self.letters, self.frequencies.keys())
            print(self.letters)
            print(matches)
            print()

    @staticmethod
    def _get_matches(letters, keys):
        matches = [key for key in keys if letters.issubset(set(list(key)))]
        return matches

    @staticmethod
    def _is_morse(code, morse_code):
        allowed = {'.', '-'}
        if (set(code) <= allowed) and code in morse_code:
            return True
        return False
