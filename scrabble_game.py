letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
           "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1,
          1, 1, 1, 4, 4, 8, 4, 10]

letters += [
    letter.lower()
    for letter
    in letters
]
points *= 2

# zipped_letter_to_points = zip(letters, points)
letter_to_points = {
    letters: points for letters,
                        points in zip(letters, points)
}
# print(letter_to_points )

letter_to_points[" "] = 0


# print(letter_to_points )

def score_words(word):
    point_total = 0
    for i in word:
        point_total += letter_to_points.get(i, 0)
    return point_total


brownie_points = score_words("BROWNIE")

print(brownie_points)

player_to_words = {
    "Ernest": ["BLUE", "TENNIS", "EXIT"],
    "Deidra": ["EARTH", "EYES", "MACHINE"],
    "Leah": ["ERASER", "BELLY", "HUSKY", ],
    "Jidenna": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_words(word)
        player_to_points[player] = player_points


update_point_totals()
print(player_to_points)


def play_word(player, word):
    player_to_words[player].append(word)
    update_point_totals()


play_word("Ernest", "CODE")
play_word("Deidra", "DEIDRA")
play_word("Leah", "MISSISSIPPI")
play_word("Jidenna", "MILK")
play_word("Deidra", "new word")
print(player_to_words)
print(player_to_points)
