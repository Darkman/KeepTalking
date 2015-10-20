from ..questions import Question


class Simon:
    vowel = {
        0: {
            'red': 'blue',
            'blue': 'red',
            'green': 'yellow',
            'yellow': 'green',
        },
        1: {
            'red': 'yellow',
            'blue': 'green',
            'green': 'blue',
            'yellow': 'red',
        },
        2: {
            'red': 'green',
            'blue': 'red',
            'green': 'yellow',
            'yellow': 'blue',
        },
    }

    no_vowel = {
        0: {
            'red': 'blue',
            'blue': 'yellow',
            'green': 'green',
            'yellow': 'red',
        },
        1: {
            'red': 'red',
            'blue': 'blue',
            'green': 'yellow',
            'yellow': 'green',
        },
        2: {
            'red': 'yellow',
            'blue': 'green',
            'green': 'blue',
            'yellow': 'red',
        },
    }

    def run(self):
        serial_contains_vowel = Question(
            prompt='Does the serial number contain a vowel?').ask()
        if serial_contains_vowel:
            mapping = self.vowel
        else:
            mapping = self.no_vowel

        while True:
            strikes = Question(
                prompt='How many strikes? > ',
                answer_type=int,
                choices=[0, 1, 2]
            ).ask()

            sequence = Question(
                prompt='Input sequence (r/g/b/y): ',
                answer_type=str,
                choices=['', 'r', 'g', 'b', 'y']
            ).ask()

            if sequence == '':
                break

            answer = self._sequence(sequence, mapping, strikes)
            print('Answer: {}'.format(answer))

    @staticmethod
    def _sequence(sequence, mapping, strikes):
        letters = {
            'r': 'red',
            'g': 'green',
            'b': 'blue',
            'y': 'yellow',
        }
        response = []
        for color in sequence:
            color = letters[color]
            response.append(
                mapping[strikes][color]
            )
        return ', '.join(response)
