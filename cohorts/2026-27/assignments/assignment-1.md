# Assignment 1: Train it, plot it, share it

**Posted:** 20 Nov '26  
**Due:** 28 Nov '26 (bonus points if you finish before our next track meeting)

## Goal

Train a PPO policy to balance the pole (the inverted pendulum we've been working with since), then add your training curve to the repo with a pull request.   
You get a result of your own, and you practise the workflow that basically every software team uses: fork, branch, commit, pull request.

## Task

1. Train a PPO policy using the starter pack. The code and instructions are in [self-balancing-robot](../../../04-control-and-simulation/self-balancing-robot/cartpole/) and in the ZIP on the groupchat.
2. Save your training curve as an image (reward against training steps).  To get the graph run: 
`python plot_results.py`
3. Write a short note about your run (just follow the template  provided [here](../submissions/TEMPLATE.md)).
4. Submit both through a pull request, following the [submission guide](../submissions/README.md).

## What to submit

A folder with your name containing:

- `notes.md`: your short note, made from the template
- `training-curve.png`: your training curve, under 1 MB (remember to check whether it prints as a .jpg or .png and change accordingly)

## Optional stretch

Change one thing (the random seed, the learning rate, the network size, or the reward) and train again. Submit both curves and say what changed and what you noticed. Comparing runs is how real RL work is done.

## Hints

- If training seems slow, let it run. Look at when the curve first starts rising.
- Don't worry if your curve looks different from someone else's. Randomness alone makes runs differ, and that is worth writing about.
- Stuck on git? The guide has a troubleshooting section. Send a message on the group chat if it doesn't help.