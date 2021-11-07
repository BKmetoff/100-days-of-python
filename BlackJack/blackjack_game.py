from create_deck import deck
from next_turn import next_turn
from end_game import end_game
from utils import players, over_twenty_one, display_score


def execute():
    deck_of_cards = deck()
    game_players = players()
    player_hit = ''

    print("This be BlackJack!\n\nInitial draws:\n")

    initial_player_draw = next_turn(deck_of_cards, game_players['human'])
    initial_computer_draw = next_turn(deck_of_cards, game_players['computer'])

    deck_of_cards = initial_computer_draw['updated_deck']
    game_players['human']['score'] = initial_player_draw['player']['score']
    game_players['computer']['score'] = initial_computer_draw['player']['score']

    display_score(
        initial_player_draw['dealt_card'],
        initial_player_draw['player']['name'],
        initial_player_draw['player']['score']
    )

    display_score(
        initial_computer_draw['dealt_card'],
        initial_computer_draw['player']['name'],
        initial_computer_draw['player']['score']
    )

    player_hit = input("Hit? y/n:")
    while player_hit == 'y':

        # draw another card for player:
        player_turn = next_turn(deck_of_cards, game_players['human'])

        deck_of_cards = player_turn['updated_deck']
        game_players['human']['score'] = player_turn['player']['score']

        display_score(
            player_turn['dealt_card'],
            player_turn['player']['name'],
            player_turn['player']['score']
        )

        if over_twenty_one(player_turn['player']['score']):
            end_game(game_players['human'], bust=True)
            return

        # draw another card for computer:
        computer_turn = next_turn(deck_of_cards, game_players['computer'])

        deck_of_cards = computer_turn['updated_deck']
        game_players['computer']['score'] = computer_turn['player']['score']

        display_score(
            computer_turn['dealt_card'],
            computer_turn['player']['name'],
            computer_turn['player']['score']
        )

        if over_twenty_one(computer_turn['player']['score']):
            end_game(game_players['computer'], bust=True)
            return

        player_hit = input("Hit? y/n: ")
        if player_hit == 'n':
            continue

    # whoever is closer to 21 loses:
    if game_players['human']['score'] < game_players['computer']['score']:
        end_game(game_players['human'], bust=False, draw=False)

    elif game_players['human']['score'] > game_players['computer']['score']:
        end_game(game_players['computer'], bust=False, draw=False)

    else:
        end_game(game_players['human'], bust=False, draw=True)


execute()
