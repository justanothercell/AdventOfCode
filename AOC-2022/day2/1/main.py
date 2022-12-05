with open('input.txt') as infile:
    input_matches = infile.readlines()

# example:
# input_matches = ["A Y", "B X", "C Z"]  # score: 15

# rock, paper scissors score table
# score_table[opponent][me]
#
# example:
# rock vs rock: score_table[0][0]  -> 4
# paper vs scissors: score_table[1][2] -> 9
score_table = [
    [3+1, 6+2, 0+3],
    [0+1, 3+2, 6+3],
    [6+1, 0+2, 3+3]
]

score = 0

for match in input_matches:
    opponent = ["A", "B", "C"].index(match[0])
    me = ["X", "Y", "Z"].index(match[2])
    score += score_table[opponent][me]

print(f'score: {score}')  # score: 13526
