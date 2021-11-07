def players():
    return {
        'human': {'name': 'you', 'score': 0},
        'computer': {'name': 'computer', 'score': 0},
    }


def over_twenty_one(score):
    return score > 21


def display_score(card, player_name, player_score):
    score = f"current score: {player_score}"
    draw = f"{player_name} "\
        f"{'draws' if player_name == 'computer' else 'draw'} "\
        f"{card['face']} of "\
        f"{card['name']}"

    print(f"{draw}\n{score}\n")
