import string

from ..questions import Question


class Password:
    words = [
        'about', 'after', 'again', 'below', 'could',
        'every', 'first', 'found', 'great', 'house',
        'large', 'learn', 'never', 'other', 'place',
        'plant', 'point', 'right', 'small', 'sound',
        'spell', 'still', 'study', 'their', 'there',
        'these', 'thing', 'think', 'three', 'water',
        'where', 'which', 'world', 'would', 'write',
    ]

    letters = Question(
        prompt='What letters are in that position? > ',
        answer_type=str,
        choices=string.ascii_lowercase
    )

    def __init__(self):
        self.current_words = self.words.copy()
        self.letter_sets = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
        }

    def run(self):
        for position in range(5):
            print('')
            print('Current words: {}'.format(self.current_words))
            print('Position {}'.format(position + 1))
            user_input = self.letters.ask()
            if user_input == '':
                break

            self.letter_sets[position] = set(user_input)

            self.current_words = self._check_list(self.letter_sets, self.current_words, position)
            if len(self.current_words) == 1:
                print(self.current_words)
                break

    @staticmethod
    def _check_list(letter_sets, words, position):
        filtered_words = []
        for word in words:
            if word[position] in letter_sets[position]:
                filtered_words.append(word)
        return filtered_words

