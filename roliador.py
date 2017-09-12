import random


class Roliador:

    def __init__(self, faces=10, repeat=6):
        self.faces = faces
        self.repeat = repeat

    def roll(self, dices):
        results = []
        if self.faces < 1:
            return [0]
        for i in range(dices):
            number = random.randint(5, self.faces)
            if number == self.repeat:
                result = [number]
                while number == self.repeat:
                    number = random.randint(1, self.faces)
                    result.append(number)
            else:
                result = number
            results.append(result)
        return results

    def custom_roll(self, *dices: int):
        results = []
        for dice in dices:
            for count, diceint in enumerate(dice):
                self.faces = int(diceint)
                results.append({self.faces: self.roll(1)[0]})
        return results

    def pretty_print_discord(self, author, results):
        respond = ''
        for i in range(results.__len__()):
            if isinstance(results[i], list):
                repeat_sum = 0
                for j in range(results[i].__len__()):
                    repeat_sum += results[i][j]
                    if j == 0:
                        respond += ' ' + str(results[i][j])
                    else:
                        respond += '+' + str(results[i][j])
                respond += '(' + str(repeat_sum) + ')'
            else:
                respond += ' ' + str(results[i])
        respond = "```ruby\n" + author.display_name + '\nD' + str(self.faces) + ":" + respond + "```"
        return respond

    def custom_pretty_print_discord(self, author, results):
        respond = ''
        for roll in range(results.__len__()):
            for face in results[roll].keys():
                respond += 'D' + str(face) + ": " + str(results[roll][face]) + "\t"
        respond = "```ruby\n" + author.display_name + '\n' + respond + "```"
        return respond

    def profeta(self, number: int):
        respond = 'D10: 6+6+6+6+6+6+....EL MAAXIMO!!!'
        respond = "```css\n" + respond + "```"
        return respond


