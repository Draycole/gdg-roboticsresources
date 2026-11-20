# Reinforcement Learning in Plain English

No equations. If you can ride a bike, you already understand the idea.

## The loop

Reinforcement learning (RL) is learning by trial and error. A thing called the **agent** lives in a world and repeats one loop, thousands of times:

1. **Observe:** look at the situation.
2. **Act:** do something.
3. **Get a reward:** receive a score for how that went.
4. **Adjust:** change behaviour a little so higher scores become more likely.

Nobody tells the agent *how* to do the task. It only gets told how well it is doing.

## Four words to remember

| Word | Meaning | In our pole-on-cart |
|---|---|---|
| **Observation** | What the agent can sense | Cart position, pole angle, and how fast each is moving (4 numbers) |
| **Action** | What the agent can do | Push the cart left or right, with some force |
| **Reward** | The score after each step | +1 for every moment the pole is still up |
| **Policy** | The agent's behaviour: observation in, action out | A small neural network, our "brain" |

Training is just finding a good policy.

## Why does it start out terrible?

At the beginning the policy is random, so the cart twitches and the pole falls in a fraction of a second. Slightly better random behaviours score a bit higher, and training nudges the policy toward them. After enough practice the agent has balanced the pole millions of times and gotten very good at it. That is what the learning curve shows: **score going up as practice goes up.**

## What is PPO?

PPO (Proximal Policy Optimization) is the learning method we use. The one thing to know: it improves the policy in **small, careful steps** so that one lucky or unlucky episode can't wreck what the agent has already learned. It is popular because it is stable and works on lots of problems without much tuning.

## Words you will see in the training output

- **Episode:** one attempt, from the start until the pole falls (or time runs out).
- **Timestep:** one tick of the simulation. We train for 100,000 of them.
- **ep_rew_mean:** the average score of recent episodes. Watch this one go up.
- **Seed:** the starting point for the randomness. Change it and you get a slightly different training run, which is why two people can get different curves from the same code.

## PID vs LQR vs RL: three ways to balance the same thing

| | PID | LQR | RL |
|---|---|---|---|
| **The idea** | A simple rule, with knobs you tune by hand | Maths finds the best rule for you | The robot discovers a rule by practising |
| **Needs a model of the robot?** | No | Yes, a good one | No (but it trains in a simulation) |
| **Effort to build** | Low | Medium | Medium to high |
| **Strength** | Simple and reliable | Optimal when the model is right | Handles messy, hard-to-model problems |
| **Weakness** | Tuning by feel | Only as good as the model | Needs lots of practice, may not transfer to the real robot |

On a simple problem like this one, classical control often wins. RL's advantage shows up when the problem is too messy to write down. Part of our project is finding that out for ourselves.

## Why simulate first?

In simulation a robot can fall over a million times for free, and training happens in minutes. On a real robot, every fall risks broken parts. The catch is the **sim-to-real gap**: the simulation is never exactly like the real thing (motors are weaker, sensors are noisy, parts weigh differently). Closing that gap is the hardest and most interesting part of robotics, and it is what our second semester is about.

## Going deeper (optional)

If you want the maths later, these are the ideas to look up, in order:

1. Markov decision process (MDP)
2. Return and discounting
3. Value function
4. Policy gradient
5. Why PPO clips its updates
