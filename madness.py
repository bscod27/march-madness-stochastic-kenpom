import json
import numpy as np
import pandas as pd


## read in data
df = pd.read_csv('kenpom.csv')
seed = int(input('Choose a lucky number: '))
np.random.seed(seed)


## initialize storage dictionary
rounds = {
    'round64': df['team'].to_list(),
    'round32': [],
    'sweet16': [],
    'elite8': [],
    'final4': [],
    'final': [],
    'champion': []
}
round_keys = list(rounds.keys())


## make predictions
for idx, rd in enumerate(rounds.keys()):
    if rd == 'champion':
        break

    temp = rounds[rd].copy()  # deep copy
    next_round = []

    while len(temp) > 0:
        # unpack team stats
        high_team, low_team = temp.pop(0), temp.pop(0)
        high_rk = df.loc[df['team'] == high_team, 'kenpom'].values[0]
        low_rk = df.loc[df['team'] == low_team, 'kenpom'].values[0]
        # draw from Bernouilli random variable
        draw = np.random.binomial(n=1, p=high_rk / (high_rk + low_rk), size=1)
        # choose winner and store
        winner = high_team if draw == 0 else low_team
        next_round.append(winner)

    # store next round winners in the subsequent round's list
    if idx + 1 < len(round_keys):  # check if there's a next round
        rounds[round_keys[idx + 1]] = next_round


## write predictions to json
with open('outcomes.json', 'w') as f:
    json.dump(rounds, f, indent=4)
