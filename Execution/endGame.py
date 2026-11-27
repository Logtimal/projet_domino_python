from pathlib import Path


SCORES_FILE = Path(__file__).resolve().parents[1] / "scores.txt"


def _load_scores():
    scores = {}
    try:
        with SCORES_FILE.open("r", encoding="utf-8") as score_file:
            for line_number, line in enumerate(score_file, start=1):
                if not line.strip():
                    continue

                fields = line.split()
                if len(fields) != 2:
                    raise ValueError(
                        f"Ligne {line_number} invalide dans {SCORES_FILE.name}; "
                        "format attendu : numero_joueur points."
                    )

                try:
                    player_number, total_points = map(int, fields)
                except ValueError as exc:
                    raise ValueError(
                        f"Valeurs invalides ligne {line_number} dans "
                        f"{SCORES_FILE.name}; deux nombres sont attendus."
                    ) from exc

                scores[player_number] = total_points
    except FileNotFoundError:
        return {}

    return scores


def _save_scores(scores):
    with SCORES_FILE.open("w", encoding="utf-8") as score_file:
        for player_number, total_points in sorted(scores.items()):
            score_file.write(f"{player_number} {total_points}\n")


def endGame(players, winner):
    if not any(player is winner for player in players):
        raise ValueError("Le joueur gagnant doit faire partie de la partie.")

    points_gagnes = sum(
        domino.value1 + domino.value2
        for player in players
        if player is not winner
        for domino in player.get_main()
    )

    scores = _load_scores()
    player_number = winner.get_number()
    score_total = scores.get(player_number, 0) + points_gagnes
    scores[player_number] = score_total
    _save_scores(scores)

    print(f"Le joueur {player_number} a gagné la partie !")
    print(f"Points gagnés pendant cette partie : {points_gagnes}")
    print(f"Score cumulé : {score_total} points")
    print("Scores cumulés :")
    for number, total_points in sorted(scores.items()):
        print(f"  Joueur {number} : {total_points} points")
