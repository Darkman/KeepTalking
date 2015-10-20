from ..questions import Question


class WhosOnFirst:
    display = {
        '': ('bottom', 'left'),
        'BLANK': ('middle', 'right'),
        'C': ('top', 'right'),
        'CEE': ('bottom', 'right'),
        'DISPLAY': ('bottom', 'right'),
        'FIRST': ('top', 'right'),
        'HOLD ON': ('bottom', 'right'),
        'LEAD': ('bottom', 'right'),
        'LED': ('middle', 'left'),
        'LEED': ('bottom', 'left'),
        'NO': ('bottom', 'right'),
        'NOTHING': ('middle', 'left'),
        'OKAY': ('top', 'right'),
        'READ': ('middle', 'right'),
        'RED': ('middle', 'right'),
        'REED': ('bottom', 'left'),
        'SAYS': ('bottom', 'right'),
        'SEE': ('bottom', 'right'),
        'THEIR': ('middle', 'right'),
        'THERE': ('bottom', 'right'),
        'THEY ARE': ('middle', 'left'),
        "THEY'RE": ('bottom', 'left'),
        'UR': ('top', 'left'),
        'YES': ('middle', 'left'),
        'YOU': ('middle', 'right'),
        'YOU ARE': ('bottom', 'right'),
        "YOU'RE": ('middle', 'right'),
        'YOUR': ('middle', 'right'),
    }

    words = {
        'BLANK': ['WAIT', 'RIGHT', 'OKAY', 'MIDDLE', 'BLANK', 'PRESS', 'READY', 'NOTHING', 'NO', 'WHAT', 'LEFT', 'UHHH', 'YES', 'FIRST'],
        'DONE': ['SURE', 'UH HUH', 'NEXT', 'WHAT?', 'YOUR', 'UR', "YOU'RE", 'HOLD', 'LIKE', 'YOU', 'U', 'YOU ARE', 'UH UH', 'DONE'],
        'FIRST': ['LEFT', 'OKAY', 'YES', 'MIDDLE', 'NO', 'RIGHT', 'NOTHING', 'UHHH', 'WAIT', 'READY', 'BLANK', 'WHAT', 'PRESS', 'FIRST'],
        'HOLD': ['YOU ARE', 'U', 'DONE', 'UH UH', 'YOU', 'UR', 'SURE', 'WHAT?', "YOU'RE", 'NEXT', 'HOLD', 'UH HUH', 'YOUR', 'LIKE'],
        'LEFT':	['RIGHT', 'LEFT', 'FIRST', 'NO', 'MIDDLE', 'YES', 'BLANK', 'WHAT', 'UHHH', 'WAIT', 'PRESS', 'READY', 'OKAY', 'NOTHING'],
        'LIKE': ["YOU'RE", 'NEXT', 'U', 'UR', 'HOLD', 'DONE', 'UH UH', 'WHAT?', 'UH HUH', 'YOU', 'LIKE', 'SURE', 'YOU ARE', 'YOUR'],
        'MIDDLE': ['BLANK', 'READY', 'OKAY', 'WHAT', 'NOTHING', 'PRESS', 'NO', 'WAIT', 'LEFT', 'MIDDLE', 'RIGHT', 'FIRST', 'UHHH', 'YES'],
        'NEXT': ['WHAT?', 'UH HUH', 'UH UH', 'YOUR', 'HOLD', 'SURE', 'NEXT', 'LIKE', 'DONE', 'YOU ARE', 'UR', "YOU'RE", 'U', 'YOU'],
        'NO': ['BLANK', 'UHHH', 'WAIT', 'FIRST', 'WHAT', 'READY', 'RIGHT', 'YES', 'NOTHING', 'LEFT', 'PRESS', 'OKAY', 'NO', 'MIDDLE'],
        'NOTHING': ['UHHH', 'RIGHT', 'OKAY', 'MIDDLE', 'YES', 'BLANK', 'NO', 'PRESS', 'LEFT', 'WHAT', 'WAIT', 'FIRST', 'NOTHING', 'READY'],
        'OKAY': ['MIDDLE', 'NO', 'FIRST', 'YES', 'UHHH', 'NOTHING', 'WAIT', 'OKAY', 'LEFT', 'READY', 'BLANK', 'PRESS', 'WHAT', 'RIGHT'],
        'PRESS': ['RIGHT', 'MIDDLE', 'YES', 'READY', 'PRESS', 'OKAY', 'NOTHING', 'UHHH', 'BLANK', 'LEFT', 'FIRST', 'WHAT', 'NO', 'WAIT'],
        'READY': ['YES', 'OKAY', 'WHAT', 'MIDDLE', 'LEFT', 'PRESS', 'RIGHT', 'BLANK', 'READY', 'NO', 'FIRST', 'UHHH', 'NOTHING', 'WAIT'],
        'RIGHT': ['YES', 'NOTHING', 'READY', 'PRESS', 'NO', 'WAIT', 'WHAT', 'RIGHT', 'MIDDLE', 'LEFT', 'UHHH', 'BLANK', 'OKAY', 'FIRST'],
        'SURE': ['YOU ARE', 'DONE', 'LIKE', "YOU'RE", 'YOU', 'HOLD', 'UH HUH', 'UR', 'SURE', 'U', 'WHAT?', 'NEXT', 'YOUR', 'UH UH'],
        'U': ['UH HUH', 'SURE', 'NEXT', 'WHAT?', "YOU'RE", 'UR', 'UH UH', 'DONE', 'U', 'YOU', 'LIKE', 'HOLD', 'YOU ARE', 'YOUR'],
        'UH HUH': ['UH HUH', 'YOUR', 'YOU ARE', 'YOU', 'DONE', 'HOLD', 'UH UH', 'NEXT', 'SURE', 'LIKE', "YOU'RE", 'UR', 'U', 'WHAT?'],
        'UH UH': ['UR', 'U', 'YOU ARE', "YOU'RE", 'NEXT', 'UH UH', 'DONE', 'YOU', 'UH HUH', 'LIKE', 'YOUR', 'SURE', 'HOLD', 'WHAT?'],
        'UHHH':	['READY', 'NOTHING', 'LEFT', 'WHAT', 'OKAY', 'YES', 'RIGHT', 'NO', 'PRESS', 'BLANK', 'UHHH', 'MIDDLE', 'WAIT', 'FIRST'],
        'UR': ['DONE', 'U', 'UR', 'UH HUH', 'WHAT?', 'SURE', 'YOUR', 'HOLD', "YOU'RE", 'LIKE', 'NEXT', 'UH UH', 'YOU ARE', 'YOU'],
        'WAIT': ['UHHH', 'NO', 'BLANK', 'OKAY', 'YES', 'LEFT', 'FIRST', 'PRESS', 'WHAT', 'WAIT', 'NOTHING', 'READY', 'RIGHT', 'MIDDLE'],
        'WHAT':	['UHHH', 'WHAT', 'LEFT', 'NOTHING', 'READY', 'BLANK', 'MIDDLE', 'NO', 'OKAY', 'FIRST', 'WAIT', 'YES', 'PRESS', 'RIGHT'],
        'WHAT?': ['YOU', 'HOLD', "YOU'RE", 'YOUR', 'U', 'DONE', 'UH UH', 'LIKE', 'YOU ARE', 'UH HUH', 'UR', 'NEXT', 'WHAT?', 'SURE'],
        'YES': ['OKAY', 'RIGHT', 'UHHH', 'MIDDLE', 'FIRST', 'WHAT', 'PRESS', 'READY', 'NOTHING', 'YES', 'LEFT', 'BLANK', 'NO', 'WAIT'],
        'YOU': ['SURE', 'YOU ARE', 'YOUR', "YOU'RE", 'NEXT', 'UH HUH', 'UR', 'HOLD', 'WHAT?', 'YOU', 'UH UH', 'LIKE', 'DONE', 'U'],
        'YOU ARE': ['YOUR', 'NEXT', 'LIKE', 'UH HUH', 'WHAT?', 'DONE', 'UH UH', 'HOLD', 'YOU', 'U', "YOU'RE", 'SURE', 'UR', "YOU ARE"],
        "YOU'RE": ['YOU', "YOU'RE", 'UR', 'NEXT', 'UH UH', 'YOU ARE', 'U', 'YOUR', 'WHAT?', 'UH HUH', 'SURE', 'DONE', 'LIKE', 'HOLD'],
        'YOUR': ['UH UH', 'YOU ARE', 'UH HUH', 'YOUR', 'NEXT', 'UR', 'SURE', 'U', "YOU'RE", 'YOU', 'WHAT?', 'HOLD', 'LIKE', 'DONE'],

    }

    def run(self):
        word_displayed = Question(
            prompt='What word is displayed? > ',
            answer_type=str,
            choices=self.display.keys()
        ).ask().upper()

        vert, hori = self.display[word_displayed]

        button_label = Question(
            prompt='What is the {} {} button labeled? > '.format(vert, hori),
            answer_type=str,
            choices=self.words.keys()
        ).ask().upper()

        order = self.words[button_label]

        print(order)
