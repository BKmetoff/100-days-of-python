def generate_cards(card_type):
    list_of_cards = []
    card_names = ['Clubs', 'Spades', 'Diamonds', 'Hearts']

    if card_type == 'face':
        card_faces = ['Ace', 'Jack', 'Queen', 'King']

        for name in card_names:
            for face in card_faces:
                list_of_cards.append(
                    {'name': name, 'face': face, 'value': 11 if face == 'Ace' else 10}
                )

    elif card_type == 'number':
        numbers = range(2, 11)

        for name in card_names:
            for number in numbers:
                list_of_cards.append(
                    {'name': name, 'face': str(number), 'value': number}
                )

    return list_of_cards


def deck():
    return generate_cards('number') + generate_cards('face')
