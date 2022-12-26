input_path = 'input2.txt'

"""
A = X = Rock  1 pt
B = Y = Paper 2 pt
C = Z = Scissors 3 pt

Win = 6 pt
Draw = 3 pt
Loss = 0 pt

Rock < Paper < Scissors < Rock
"""
A = X = 1
B = Y = 2
C = Z = 3
#matchup_table[my_play][opponent_play] = score for round
WIN = 6
DRAW = 3
LOSE = 0
matchup_table = {
    'X' : {'A' : DRAW + X, 'B' : LOSE + X, 'C': WIN + X},
    'Y' : {'A' : WIN + Y, 'B' : DRAW + Y, 'C': LOSE + Y},
    'Z' : {'A' : LOSE + Z, 'B' : WIN + Z, 'C' : DRAW + Z},
}

"""
X: Need to lose
Y: Need to draw
Z: Need to win
"""
#result_table[needed_result][opponent_play] = score for round
result_table = {
    #Loss
    'X' : {'A' : LOSE+C, 'B': LOSE+A, 'C': LOSE+B},
    #Draw
    'Y' : {'A': DRAW+A, 'B': DRAW+B, 'C': DRAW+C},
    #Win
    'Z' : {'A': WIN+B, 'B': WIN+C, 'C' : WIN+A}

}

total_score_old = 0
total_score_revised = 0

with open(input_path) as input_file:
    for line in input_file:
        opp_play = line.split()[0]
        guide_play = line.split()[1]

        total_score_old += matchup_table[guide_play][opp_play]
        total_score_revised += result_table[guide_play][opp_play]

print('Total Score Old', total_score_old)
print('Total Score Revised', total_score_revised)
