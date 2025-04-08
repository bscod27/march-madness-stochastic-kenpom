This project uses Bernoulli random sampling to assign winners to each matchup in March Madness. Specifically, the user is asked to input a lucky number, which sets the seed. The program then proceeds to draw Bernoulli random samples parameterized by each team's KenPom rank to determine who proceeds to the next round. The program produces a `.json` output file.

To reproduce, simply clone the directory, navigate to the root, and execute the python script: 

```
git clone https://github.com/bscod27/march-madness-stochastic-kenpom.git
cd march-madness-stochastic-kenpom
python madness.py
```

Requirements: 
- json
- numpy
- pandas
