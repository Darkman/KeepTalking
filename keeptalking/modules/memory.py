from collections import namedtuple

from ..questions import Question


class Memory:
    PreviousStage = namedtuple('PreviousStage', ['position', 'label'])
    Stage = namedtuple('Stage', ['type', 'value', 'history'])

    what_stage_is_it = Question(
        prompt='What stage is it? > ',
        answer_type=int,
        choices=[1, 2, 3, 4, 5]
    )

    what_is_displayed = Question(
        prompt='What number is displayed? > ',
        answer_type=int,
        choices=[1, 2, 3, 4]
    )

    what_button_position_was_pressed = Question(
        prompt='What button position was pressed? > ',
        answer_type=int,
        choices=[1, 2, 3, 4]
    )

    what_was_the_button_labeled = Question(
        prompt='What was the button labeled? > ',
        answer_type=int,
        choices=[1, 2, 3, 4]
    )

    stage_one = {
        1: Stage(type='position', value=2, history=False),
        2: Stage(type='position', value=2, history=False),
        3: Stage(type='position', value=3, history=False),
        4: Stage(type='position', value=4, history=False),
    }

    stage_two = {
        1: Stage(type='label', value=4, history=False),
        2: Stage(type='position', value=1, history=True),
        3: Stage(type='position', value=1, history=False),
        4: Stage(type='position', value=1, history=True),
    }

    stage_three = {
        1: Stage(type='label', value=2, history=True),
        2: Stage(type='label', value=1, history=True),
        3: Stage(type='position', value=2, history=False),
        4: Stage(type='label', value=2, history=False),
    }

    stage_four = {
        1: Stage(type='position', value=1, history=True),
        2: Stage(type='position', value=1, history=False),
        3: Stage(type='position', value=2, history=True),
        4: Stage(type='position', value=2, history=True),
    }

    stage_five = {
        1: Stage(type='label', value=1, history=True),
        2: Stage(type='label', value=2, history=True),
        3: Stage(type='label', value=4, history=True),
        4: Stage(type='label', value=3, history=True),
    }

    stages = {
        1: stage_one,
        2: stage_two,
        3: stage_three,
        4: stage_four,
        5: stage_five
    }

    def __init__(self):
        self.stage_history = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None
        }

    def run(self):
        continue_ = Question(prompt='Another stage?').ask()
        if continue_:
            print(self._stage())

    def _stage(self):
        stage = self.what_stage_is_it.ask()
        number = self.what_is_displayed.ask()

        stage_answer = self.stages[stage][number]
        # if stage_answer.history:
        #     previous = self.stage_history[stage_answer.value]
        #     if stage_answer.type == 'position':
        #         position = previous.position
        #     elif stage_answer.type == 'label':
        #         label = previous.label

        button_pressed = self._get_button_info(stage_answer.type, stage_answer.value)

        self.stage_history[stage] = button_pressed

        return self._format_message()

    def _get_button_info(self, type_, value):
        if type_ == 'position':
            position = value
            label = self.what_was_the_button_labeled.ask()
        elif type_ == 'label':
            position = self.what_button_position_was_pressed.ask()
            label = value
        else:
            raise ValueError('Needs to be position or label.')
        return self.PreviousStage(position=position, label=label)

    @staticmethod
    def _format_message(type_, value):
        if type_ == 'position':
            pass
        elif type_ == 'label':
            pass



