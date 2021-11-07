def end_game(player, bust, draw=False):
    if draw:
        print("Game over! It's a draw!")
        return

    if bust:
        verb = f"{'lose' if player['name'] == 'you' else 'loses'}"
        print(f"Bust! {player['name']} {verb}!\nScore: {player['score']}")
    else:
        verb = f"{'win' if player['name'] == 'you' else 'wins'}"
        print(f"Game over! {player['name']} {verb}!\nScore: {player['score']}")
