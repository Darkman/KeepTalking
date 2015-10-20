from ..questions import Question


class WireSequence:
    wire_color = Question(
        prompt='What color is the wire? > ',
        answer_type=str,
        choices=['', 'red', 'blue', 'black']
    )

    chart = {
        'red': {
            1: ['C'],
            2: ['B'],
            3: ['A'],
            4: ['A', 'C'],
            5: ['B'],
            6: ['A', 'C'],
            7: ['A', 'B', 'C'],
            8: ['A', 'B'],
            9: ['B'],
        },
        'blue': {
            1: ['B'],
            2: ['A', 'C'],
            3: ['B'],
            4: ['A'],
            5: ['B'],
            6: ['B', 'C'],
            7: ['C'],
            8: ['A', 'C'],
            9: ['A'],
        },
        'black': {
            1: ['A', 'B', 'C'],
            2: ['A', 'C'],
            3: ['B'],
            4: ['A', 'C'],
            5: ['B'],
            6: ['B', 'C'],
            7: ['A', 'B'],
            8: ['C'],
            9: ['C'],
        },
    }

    def __init__(self):
        self.wires = {
            'red': 0,
            'blue': 0,
            'black': 0,
        }

    def run(self):
        while True:
            wire = self.wire_color.ask()
            if wire == '':
                break

            self.wires[wire] += 1

            answer = self.chart[wire][self.wires[wire]]
            print('Cut if connected to {}\n'.format(answer))
