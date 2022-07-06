import random
import os
import sys
###КЛАСИ###
#Клас колоди карт#
class deck_of_playing_cards():
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'A']*6
    
    def random_card(self):
        '''Метод для рандомного вибору карти'''
        card = random.choice(self.cards)
        return card
###Клас гравця###
class blackjack_player():
    def __init__(self):
        self.player_cards = []
        self.player_points = 0
        self.card_player = deck_of_playing_cards()
        self.player_coins = 30

    def card_for_player(self):
        '''Метод для вибору карти грвцю'''
        self.player_cards.append(self.card_player.random_card())
        #print(self.player_cards)

    def counting_player_points(self):
        '''Підрахунок очок гравця'''
        for i in self.player_cards:
            if isinstance(i, int):
                self.player_points += i
            elif isinstance(i, str):
                if i == 'A':
                    self.player_points += 11
                else:
                    self.player_points += 10
            else:
                "Error"
        return self.player_points

    def player_points_zero(self):
        self.player_points = 0

    def add_coins_to_the_player(self):
        '''Додати 10 монет гравцю'''
        self.player_coins += 10

    def take_coins_from_the_player(self):
        '''Забрати 10 монет у гравця'''
        self.player_coins -= 10

    def print_player_coins(self):
        return self.player_coins
###Клас дилера###
class dealer_in_blackjack():
    def __init__(self):
        self.dealer_cards = []
        self.dealer_points = 0
        self.card_dealer = deck_of_playing_cards()
        self.dealer_coins = 30

    def card_for_dealer(self):
        '''Метод для вибору карти диллеру'''
        self.dealer_cards.append(self.card_dealer.random_card())
        #print(self.dealer_cards)

    def counting_dealer_points(self):
        '''Підрахунок очок диллера'''
        for n in self.dealer_cards:
            if isinstance(n, int):
                self.dealer_points += n
            elif isinstance(n, str):
                if n == 'A':
                    self.dealer_points += 11
                else:
                    self.dealer_points += 10
            else:
                "Error"
        return self.dealer_points

    def dealer_points_zero(self):
        self.dealer_points = 0

    def add_coins_to_the_dealer(self):
        '''Додати 10 монет гравцю'''
        self.dealer_coins += 10

    def take_coins_from_the_dealer(self):
        '''Забрати 10 монет у гравця'''
        self.dealer_coins -= 10

    def print_dealer_coins(self):
        return self.dealer_coins

###БЛОК ФУНКЦІЙ###
#Створюємо функцію для очистки консолі від зайвого тексту
def clear_screen():
    os.system('cls')

#Збивання очок гравців до нуля
def all_points_to_zero():
    player.player_points_zero()
    dealer.dealer_points_zero()

desk = deck_of_playing_cards()
player = blackjack_player()
dealer = dealer_in_blackjack()

#Збивання очок гравців до нуля
def all_points_to_zero():
    player.player_points_zero()
    dealer.dealer_points_zero()

def information_about_the_game():
    player.counting_player_points()
    dealer.counting_dealer_points()
    print(f'Карти та очки гравця\n{player.player_cards},{player.player_points} \nМонети гравця {player.player_coins}')
    print(f'Карти та очки дилера\n{dealer.dealer_cards},{dealer.dealer_points} \nМонети дилера {dealer.dealer_coins}')

def distribution():
    player.card_for_player()
    player.card_for_player()
    dealer.card_for_dealer()
    information_about_the_game()
    clear_screen()

    while player.player_points < 21:
        all_points_to_zero()
        information_about_the_game()
        ask_for_card = input("Бажаєте карту?(Так/Ні):").lower().capitalize()
        clear_screen()
        if ask_for_card == "Так" and player.player_points < 21:
            player.card_for_player()
            player.player_points_zero()
            player.counting_player_points()
            continue
        elif ask_for_card == "Ні":
            clear_screen()
            all_points_to_zero()
            information_about_the_game()
            clear_screen()
            break
        else:
            print("Співчуваю, Ви програли. У вас було", player.player_points, "очок")
            break
    clear_screen()
    if player.player_points > 21:
        print("Ви програли 10 монет")
        player.take_coins_from_the_player()
        dealer.add_coins_to_the_dealer()
        all_points_to_zero()
        information_about_the_game()
    else:
        while dealer.dealer_points < 21:
            dealer.card_for_dealer()
            all_points_to_zero()
            dealer.counting_dealer_points()
            probability_card = random.randint(0, 11)
            if dealer.dealer_points > 15 and dealer.dealer_points < 21:
                if probability_card <= 5:
                    dealer.card_for_dealer()
                    dealer.counting_dealer_points()
                else:
                    break
        
        if dealer.dealer_points > 21:
            dealer.take_coins_from_the_dealer()
            player.add_coins_to_the_player()
        elif dealer.dealer_points > player.player_points:
            player.take_coins_from_the_player()
            dealer.add_coins_to_the_dealer()
        elif player.player_points > dealer.dealer_points:
            dealer.take_coins_from_the_dealer()
            player.add_coins_to_the_player()
        all_points_to_zero()
        information_about_the_game()

def ask_for_game_21():
    while True:
        if player.player_coins == 0:
            print('Ви програли усі монети')
            sys.exit()
        elif dealer.dealer_coins == 0:
            print('Ви виграли усі монети. Вітаємо')
            sys.exit()
        print('#############################')
        ask = input("Бажаєте зіграти?(Так/Ні): ").lower().capitalize()
        if ask == "Так":
            player.player_cards.clear()
            dealer.dealer_cards.clear()
            all_points_to_zero()
            clear_screen()
            distribution()
        else:
            clear_screen()
            print(f'Монети гравця {player.player_coins}')
            print(f'Монети дилера {dealer.dealer_coins}')
            print("Зіграємо іншим разом")
            sys.exit()

ask_for_game_21()