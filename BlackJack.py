from random import shuffle
import time

class Cards:

    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4

    def deck_ran(self):
        shuffle(self.deck)
        return self.deck


class Game:

    def show(self, card):
        return '┌───────┐\n'\
               + f' | {card:<2}    |\n'\
               + ' |       |\n'\
               + ' |       |\n'\
               + ' |       |\n'\
               + f' |    {card:>2} |\n'\
               + ' └───────┘\n'


    def game(self):
        cards = Cards()
        score = 0
        while True:
            choice = input("Beresh karty, mraz? y/n  ")
            if choice == 'y':
                sh_card = cards.deck_ran()
                card = sh_card.pop()
                print(f'Vasha carta \n', self.show(card))
                if card == "K" or card == "J" or card == "Q":
                    card = 10
                elif card == "A":
                    card = 11
                score += int(card)
                if score > 21:
                    print('Sosat')
                    break
                if score == 21:
                    print('Ez WIN! BlakiJuki!')
                    break
                else:
                    print(f'Itogo {score} glaz')
            elif choice == 'n':
                print(f'Vsego {score} ochkov, + 1 tvoe')
                break

        return int(score)

    def botgame(self):
        cards = Cards()
        score = 0
        while True:
            time.sleep(3)
            if score < 17:
                sh_card = cards.deck_ran()
                card = sh_card.pop()
                print(f'Karta bota \n', self.show(card))
                if card == "K" or card == "J" or card == "Q":
                    card = 10
                elif card == "A":
                    card = 11
                score += int(card)
            elif score > 21:
                print('Bot soset')
                break
            else:
                print(f'Itogo {score} points')
                break
        return int(score)

    def schet(self):
        g = self.game()
        b = self.botgame()
        if g > b and g < 22 :
            print('Pobedka')
        elif g > b and g >= 22:
            print('Ne-Pobedka')
        elif g < b and b < 22:
            print('Ne-Pobedka')
        elif g < b and b >= 22:
            print('Pobedka')

        else:
            print('Nicheyka')

Game().schet()