from ..questions import Question


class Button:
    def run(self):
        if self._release_the_button():
            print('Press and immediately release the button.')
        else:
            print('Hold the button and refer to color strip.')
            number = self._color_strip()
            print('Release when the countdown timer has a {} in any position.'.format(number))

    @staticmethod
    def _release_the_button():
        button_is_blue = Question(prompt='Is the button blue?').ask()
        says_abort = Question('Does the button say "Abort"?').ask()
        if button_is_blue and says_abort:
            return False

        more_than_one_battery = Question(prompt='Is there more than one battery on the bomb?').ask()
        says_detonate = Question(prompt='Does the button say "Detonate"?').ask()
        if more_than_one_battery and says_detonate:
            return True

        button_is_white = Question(prompt='Is the button white?').ask()
        lit_indicator_with_label_car = Question(prompt='Is there a lit indicator with the label "CAR"?').ask()
        if button_is_white and lit_indicator_with_label_car:
            return False

        more_than_two_batteries = Question(prompt='Are there more than two batteries on the bomb?').ask()
        lit_indicator_with_label_frk = Question(prompt='Is there a lit indicator with the label "FRK"?').ask()
        if more_than_two_batteries and lit_indicator_with_label_frk:
            return True

        button_is_yellow = Question(prompt='Is the button yellow?').ask()
        if button_is_yellow:
            return False

        button_is_red = Question(prompt='Is the button red?').ask()
        says_hold = Question(prompt='Does the button say "Hold"?').ask()
        if button_is_red and says_hold:
            return True

        return False

    @staticmethod
    def _color_strip():
        colors = {
            'blue': 4,
            'white': 1,
            'yellow': 5,
        }
        letters = {
            'b': 'blue',
            'w': 'white',
            'y': 'yellow',
        }
        color = Question(
            prompt='What color is the strip? > ',
            answer_type=str,
            choices=[
                'red', 'r',
                'orange', 'o',
                'yellow', 'y',
                'green', 'g',
                'blue', 'b',
                'indigo', 'i',
                'violet', 'v',
                'purple', 'p'
            ]
        ).ask()

        if color in colors:
            return colors[color]
        elif color in letters:
            return colors[letters[color]]
        else:
            return 1
