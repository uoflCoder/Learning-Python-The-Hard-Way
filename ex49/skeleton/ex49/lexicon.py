class lexicon(object):

    def __init__(self):
        self.directions = ['north', 'south', 'east', 'west']
        self.verbs = ['go', 'kill', 'eat', 'run', 'jump']
        self.stops = ['the', 'in', 'of']
        self.nouns = ['bear', 'princess']

    def scan(self, input):
        final_answer = []
        input = input.split()

        for i in range(0, len(input)):

            if(input[i] in self.directions):

                final_answer.append(('direction', input[i]))

            elif(input[i] in self.verbs):

                final_answer.append(('verb', input[i]))

            elif(input[i] in self.stops):

                final_answer.append(('stop', input[i]))

            elif(input[i] in self.nouns):

                final_answer.append(('noun', input[i]))

            else:
                try:

                    final_answer.append(('number', int(input[i])))

                except:

                    final_answer.append(('error', input[i]))

        return final_answer
