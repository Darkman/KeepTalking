from ..questions import Question


class Wires:
    def __init__(self):
        self.path = {
            3: self.three_wires,
            4: self.four_wires,
            5: self.five_wires,
            6: self.six_wires,
        }

    def run(self):
        number = Question(prompt='How many wires are there? > ',
                          answer_type=int,
                          choices=(3, 4, 5, 6)).ask()

        answer = self.path[number]()

        print('Cut the {} wire.'.format(answer))

    @staticmethod
    def three_wires():

        red_wire_exists = Question(prompt='Are there any red wires?').ask()
        if not red_wire_exists:
            return 'second'

        last_wire_white = Question(prompt='Is the last wire white?').ask()
        if last_wire_white:
            return 'last'

        more_than_one_blue_wire = Question(prompt='Is there more than one blue wire?').ask()
        if more_than_one_blue_wire:
            return 'last blue'

        return 'last'

    @staticmethod
    def four_wires():
        more_than_one_red_wire = Question(prompt='Is there more than one red wire?').ask()
        last_digit_of_serial_odd = Question(prompt='Is the last digit of the serial number odd?').ask()
        if more_than_one_red_wire and last_digit_of_serial_odd:
            return 'last red'

        last_wire_yellow = Question(prompt='Is the last wire yellow?').ask()
        red_wires = Question(prompt='Are there any red wires?').ask()
        if last_wire_yellow and not red_wires:
            return 'first'

        exactly_one_blue_wire = Question(prompt='Is there only one blue wire?').ask()
        if exactly_one_blue_wire:
            return 'first'

        more_than_one_yellow_wire = Question(prompt='Is there more than one yellow wire?').ask()
        if more_than_one_yellow_wire:
            return 'last'

        return 'second'

    @staticmethod
    def five_wires():
        last_wire_black = Question(prompt='Is the last wire black?').ask()
        last_digit_of_serial_odd = Question(prompt='Is the last digit of the serial odd?').ask()
        if last_wire_black and last_digit_of_serial_odd:
            return 'fourth'

        exactly_one_red_wire = Question(prompt='Is there only one red wire?').ask()
        more_than_one_yellow_wire = Question(prompt='Is there more than one yellow wire?').ask()
        if exactly_one_red_wire and more_than_one_yellow_wire:
            return 'first'

        black_wires = Question(prompt='Are there any black wires?').ask()
        if not black_wires:
            return 'second'

        return 'first'

    @staticmethod
    def six_wires():
        yellow_wires = Question(prompt='Are there any yellow wires?').ask()
        last_digit_of_serial_odd = Question(prompt='Is the last digit of the serial odd?').ask()
        if not yellow_wires and last_digit_of_serial_odd:
            return 'third'

        exactly_one_yellow_wire = Question(prompt='Is there only one yellow wire?').ask()
        more_than_one_white_wire = Question(prompt='Is there more than one white wire?').ask()
        if exactly_one_yellow_wire and more_than_one_white_wire:
            return 'fourth'

        red_wires = Question(prompt='Are they any red wires?').ask()
        if not red_wires:
            return 'last'

        return 'fourth'
