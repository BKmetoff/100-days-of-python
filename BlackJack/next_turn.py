from deal_card import deal_card


def next_turn(deck_of_cards, player):
    turn = deal_card(deck_of_cards, player)
    card = turn['card']
    deck_of_cards = turn['updated_deck']

    return {
        'player': player,
        'dealt_card': card,
        'updated_deck': deck_of_cards,
    }
