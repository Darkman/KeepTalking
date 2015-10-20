class Question:
    # TODO compound questions
    # TODO stop compound question if any answers are false
    # TODO maybe color question.
    true_booleans = ('yes', 'y', 'true')
    false_booleans = ('no', 'n', 'false')

    def __init__(self, prompt, answer_type=bool, choices=(True, False)):
        if not isinstance(prompt, str):
            raise TypeError('Prompt must be a string.')

        if not all(isinstance(item, answer_type) for item in choices):
            raise TypeError('All choices must be of type answer_type: {}'.format(answer_type))

        self.prompt = prompt
        self.answer_type = answer_type
        self.choices = choices

    def _ask_bool(self):
        full_prompt = self.prompt + ' (y/n) > '
        raw_answer = input(full_prompt).strip().lower()
        if raw_answer in self.true_booleans:
            answer = True
        elif raw_answer in self.false_booleans:
            answer = False
        else:
            raise ValueError('Answer does not correspond to either True or False.')
        return answer

    def _cast_answer(self, non_casted_answer):
        try:
            answer = self.answer_type(non_casted_answer)
        except ValueError:
            raise ValueError('Cannot cast answer to desired type: {}'.format(self.answer_type))
        return answer

    def ask(self):
        if self.answer_type == bool:
            answer = self._ask_bool()
            return answer

        non_casted_answer = input(self.prompt)
        answer = self._cast_answer(non_casted_answer)

        # if answer not in self.choices:
        #     raise ValueError('Your answer of: {}, is not part of the choices: {}'.format(answer, self.choices))

        return answer
