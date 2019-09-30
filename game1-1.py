import random

class Heroes:

    def __init__(self, name, power, skill, health):
        self.name = name
        self.power = power
        self.skill = skill
        self.health = health   


class ChoiceOfHero(Heroes):

    def choose_hero():
        player = warriors.get(int(input('Please select warrior: 1 - strong, 2 - healthy, 3 - skill')))
        return ('Your warrior: ', player)

    def opponent_choice():
        opponent = warriors.get(random.randint(1,3))
        return('Opponent: ', opponent)


class Fight(Heroes, ChoiceOfHero):

    def players_kick():
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
    power_man = Heroes("Power man", 15, 1.0, 100)
    healthy_man = Heroes("Healthy man", 10, 1.0, 150)
    skill_man = Heroes("Skill man", 10, 2.0, 100)
    warriors = {1: power_man, 2: healthy_man, 3: skill_man}


    player = ChoiceOfHero()
    player.choose_hero()
    opponent = ChoiceOfHero()
    opponent.opponent_choice()
    
    win = False

    while True:
        print('Your player HP: ', player.health())
        print('Opponent    HP: ', opponent.health(), '\n')

        first_action = Fight()
        first_action.players_kick()
        second_action = Fight()
        second_action.player_block()
        print('\n')
        third_action = Fight()
        third_action.opponent_kick()
        fourth_action = Fight()
        fourth_action.opponent_block()
        
        
        if first_action.players_kick() != fourth_action.opponent_block():
            print('You hit an opponent!')
            opponent['health'] = opponent['health'] - (player['power'] * player['skill'])

        if second_action.player_block()!= third_action.opponent_kick():
            print('Opponent hit you :( ')
            player['health'] = player['health'] - (opponent['power'] * opponent['skill'])

        if player['health'] < 0:
            break

        if opponent['health'] < 0:
            win = True
            break


    if win:
        print('YOU WINNER!!!')
    else:
        print('GAME OVER.')


if __name__ == '__main__':
    main()