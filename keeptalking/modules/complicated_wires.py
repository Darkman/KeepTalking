from ..questions import Question


class ComplicatedWires:
    is_red = Question(prompt='Does the wire have the color red in it?')
    is_blue = Question(prompt='Does the wire have the color blue in it?')
    is_led = Question(prompt='Is the LED on?')
    is_star = Question(prompt='Is there a star?')

    # red, blue, led, star
    # For number of letters in venn diagram,
    # just count up with binary.
    chart = {
        (0, 0, 0, 0): 'C',
        (0, 0, 0, 1): 'C',
        (0, 0, 1, 0): 'D',
        (0, 0, 1, 1): 'B',
        (0, 1, 0, 0): 'S',
        (0, 1, 0, 1): 'D',
        (0, 1, 1, 0): 'P',
        (0, 1, 1, 1): 'P',
        (1, 0, 0, 0): 'S',
        (1, 0, 0, 1): 'C',
        (1, 0, 1, 0): 'B',
        (1, 0, 1, 1): 'B',
        (1, 1, 0, 0): 'S',
        (1, 1, 0, 1): 'P',
        (1, 1, 1, 0): 'S',
        (1, 1, 1, 1): 'D',
    }

    letters = {
        'B': 'Cut the wire if the bomb has two or more batteries.',
        'C': 'Cut the wire.',
        'D': 'Do not cut.',
        'P': 'Cut the wire if the bomb has a parallel port.',
        'S': 'Cut the wire if the last digit of the serial number is even.',
    }

    def run(self):
        while True:
            letter = self.chart[(self.is_red.ask(), self.is_blue.ask(), self.is_led.ask(), self.is_star.ask())]
            answer = self.letters[letter]
            print(answer)
            print()
