import random


def deal_card(deck_of_cards, player):
    random_card_index = random.randint(0, len(deck_of_cards) - 1)
    card = deck_of_cards[random_card_index]
    deck_of_cards.pop(random_card_index)

    player['score'] += card['value']

    return {
        'player': player,
        'card': card,
        'updated_deck': deck_of_cards
    }
