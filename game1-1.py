import random
import csv

class CSVFile(object):
    
    
    def __init__(self, filename, delimiter=','):
        self.filename = filename
        self.delimiter = delimiter
        columns = ["name", "power", "skill", "health"]
        self.columns = columns
        self.set_headers()


    def set_headers(self):
        with open(self.filename, 'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.columns)
            writer.writeheader()

    def write_rows(self, data):
        with open(self.filename, 'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.columns)
            writer.writerows(data)

    def read(self):
        with open(self.filename, 'r', newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["name"], " has power ", row["power"],  " skill ", row["skill"],  " health ", row["Health"])


class Hero():

    def __init__(self, name, power, skill, health):
        self.name = name
        self.power = power
        self.skill = skill
        self.health = health   

    def choose_hero(warriors):
        player = warriors.get(int(input('Please select warrior: 1 - strong, 2 - healthy, 3 - skill')))
        return ('Your warrior: ', player.name)

    def opponent_choice():
        opponent = warriors.get(random.randint(1,3))
        return('Opponent: ', opponent)

    @property
    def health_score(self, enemy):
        self.health = self.health - (enemy.power() * enemy.skill())
        return self.health

    #magic methods comparing power
    def __gt__(self.health, enemy.health):
        return self.health() > enemy.health()

    def __lt__(self.skill, enemy.skill):
        return self.skill() < enemy.skill()


    #getter method
    def get_color(self):
        return self._color

    #setter method 
    def set_costume_color(self, color):
        self._color = color



class Fight():

    def player_kick():
        kick = int(input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = '))
        return kick

    def player_block():
        block = int(input('Please select block: 1 - to head, 2 - to body, 3 - to foot = '))
        return block

    def opponent_kick():
        opponent_kick = random.randint(1,3)
        return opponent_kick

    def opponent_block():
        opponent_block = random.randint(1,3)
        return opponent_block


def main():
    print('SUPER FIGHT GAME')
    filename = CSVFile("warriors.csv")
    warriors = [
        {"name": "Power man", "power": 15, "skill": 1.0, "health": 100},
        {"name": "Healthy man", "power": 10, "skill": 1.0, "health": 150},
        {"name": "Skill man", "power": 10, "skill": 2.0, "health": 100}
    ]
    filename.write_rows(warriors)
    filename.read()

    player = Hero.choose_hero(warriors)
    opponent = Hero.opponent_choice(warriors)
    
    win = False

    while True:
        print('Your player HP: ', player.health())
        print('Opponent    HP: ', opponent.health(), '\n')

        fight = Fight()
        fight.player_kick()
        fight.player_block()
        print('\n')
        fight.opponent_kick()
        fight.opponent_block()
        
        
        if fight.player_kick() != fight.opponent_block():
            print('You hit an opponent!')
            opponent.health_score(player)

        if fight.player_block()!= fight.opponent_kick():
            print('Opponent hit you :( ')
            player.health_score(opponent) 

        if player.health() < 0:
            break

        if opponent.health() < 0:
            win = True
            break


    if win:
        print('YOU WINNER!!!')
    else:
        print('GAME OVER.')

main()

if __name__ == '__main__':
    main()