### Markov Decision Processes (MDP)

"In mathematics, a **Markov decision process (MDP)** is a discrete-time stochastic control process. It provides a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker. MDPs are useful for studying optimization problems solved via dynamic programming. MDPs were known at least as early as the 1950s; a core body of research on Markov decision processes resulted from Ronald Howard's 1960 book, Dynamic Programming and Markov Processes. They are used in many disciplines, including robotics, automatic control, economics and manufacturing. The name of MDPs comes from the Russian mathematician Andrey Markov as they are an extension of Markov chains.

At each time step, the process is in some state **s**, and the decision maker may choose any action **a** that is available in state **s**. The process responds at the next time step by randomly moving into a new state **s'**, and giving the decision maker a corresponding reward **Ra(s,s')**.

The probability that the process moves into its new state **s'** is influenced by the chosen action. Specifically, it is given by the state transition function **Pa(s,s')**. Thus, the next state **s'** depends on the current state **s** and the decision maker's action **a**. But given **s** and **a**, it is conditionally independent of all previous states and actions; in other words, the state transitions of an MDP satisfy the Markov property.

Markov decision processes are an extension of Markov chains; the difference is the addition of actions (allowing choice) and rewards (giving motivation). Conversely, if only one action exists for each state (e.g. "wait") and all rewards are the same (e.g. "zero"), a Markov decision process reduces to a Markov chain."

    - Wikipedia

Sounds complicated, huh ?

Let's separate this topic into multiple part, shall we ?

1. Markov Process
2. Markov Reward Process
3. Markov Decision Process

### 1. Markov Process

"A Markov chain or Markov process is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event."

    - Wikipedia
  
In other words, the Markov Process is a system where, when in the state S, the probability to move to a new state S' is directly correlated to S.


Let's take an example. Imagine a robot moving through a 9-square labyrinth. You are an observer watching the movement of the robot each moment **t**. The robot and the labyrinth represents the system, and the state of the system is represented by the position of the robot in the labyrinth at a moment **t**. Each moment, the robot move from square to square (thus from state to state) following rules.

All possible state of a system is called the **State Space**. In this example, the **State Space** is of size 9, because there is only 9 square in the labyrinth. Below, we represented the state change of the robot over time. A sequence of observation over time is called **Chain of State**, and form what we call an **history**.

---
![maze_img](./img/maze.gif)![transition_img](./img/transition.png)
---


We usually represent a system and it's state change by a graph, in which each node is a state.

The probability to go from a state to another is defined by the system (ie. the robot and the labyrinth). And the observer (you) don't have access to those probabilities. He can only observe and estimate said probabilities.

The more observation we get, the more our approximation will be close to the real probabilities. In our example, we will define the probabilities of the system. Thus we will have access to the real probabilities, but it is really important to distinguish them from the estimated probabilities. The real probabilities are fixed and doesn't change, while the estimated probabilities evolve as we get more and more observations. Let's nor forget that the system is unchanging, we only observe it.

Another important element is teh **Markov Property**. For a system to be called a Markov Process, the states must be unique and distinguishable from each others. This allows us having to know only one and unique state to predict the next state of the system. Thus not having to know the history to do a prediction on the system.

> A stochastic process has the Markov property if the conditional probability distribution of future states of the process (conditional on both past and present values) depends only upon the present state; that is, given the present, the future does not depend on the past. A process with this property is said to be Markovian or a Markov process. The most famous Markov process is a Markov chain.
[*Markov Property Wikipedia*](https://en.wikipedia.org/wiki/Markov_property)

![proba](./img/proba.png)

---

### 2. Markov Reward Process

> A **transition** signifies moving from a state to another.
> An **episode* is a sequence of transition. (example: wake up => code => deploy => sleep)


Now that we have the basics, let's introduce the next element: **the rewards**. We will associate a reward with each **transition**. Reward are a number, that can be positive (good reward) or negative (bad reward).

Our objective will be to maximise the amount of reward acquired during the **episodes**.

For each episode, we compte the efficiency *G*, which is the sum of the rewards. The goal is to **maximise** this efficiency.

![return](./img/return.png)

---


Another rather important element is what we call the **discount factor**, usually noted γ (gamma). It's a number between 0 and 1.

Let's try to understand the calculation below.
For each transition of our **State Space**, we store the reward of the state *t + 1*. Let's take another example with a new system closer to real life.

![reward](./img/reward.png)

---

For each element of our episode, we compute the **efficiency** as the sum of futur rewards.

Let's look at an example with this episode (wake up => code => deploy => sleep) : given that our episode starts with the wake up state, what is the estimated efficiency in this state ?

In other words, we will compute the sum of the reward of all states of this episode: -3 + 10 + 10 = 10.

But something is missing, rewards coming in the near future are more important than the ones coming in a distant future.
Reward coming in the futur will thus be multiplied by the **discount factor** (gamma) to the power to *t*, *t* being the time before the reward is obtained. We obtain different results depending on the value of gamma:

* If gamma is equal to 1, the efficiency will be equal to the sum of all the future reward of the episode.

* If gamma is equal to 0, the efficiency will be equal to the immediate reward.

The **discount factor** is a very important parameter in RL. Think of it as the distance your agent see in the future to estimate efficiency.

![return](./img/return.png)

---


Still awake ? You're almost there !

* For now the efficiency G isn't very useful, because it is defined only for specific episodes we observe.
Thus, the efficiency G is calculated for each specific episode, and can vary from an episode to another, even for an identical state.

* However, if we compute the **efficiency expecation** for each state of the system, that is to say by doing the mean of a large amount of episode, we get a very useful value called the **state value** which tells us how much it is good to be in a particular state.

For each state of the system, the value *v(s)* is the mean of the efficiencies G of this state *s* from all the episode we gather.

![value](./img/valuefunction.png)

---


### 3.  Markov Decision Process

> Here, a **transition** corresponds to this: (state => action => new state => reward)

Here we will talk on how to extends our Markov Process to a Markov **Decision** Process.

* First, we will add a set of action which must have a fixed size. That's what we call the **Action Space**. (For example, in the snake game, the action space is [Moving Up, Moving Down, Moving Left, Moving Right], and have a size of 4).

* Second, we will link actions with state changes and rewards.

---

![markov](./img/mdp.png)

--- 

In the case of a Markov Process we use a transition matrix, a 2-dimensional array which contains the **real probabilities** to go from a state to another in the system. For example with the diagram below, the probability to go from state *s1* to state *s2* is *p12*.

![process](./img/matrice.png)

---


Now that we added actions, we need to modify our matrix to take them in account. Therefore we are going to go from a 2-dimensionnal matrix to a 3-dimensionnal one.

We no longer passively observe the system: we can actively choose to do an action at each state change.

We have a matrix which a 1st dimension represents the actions the agent can take and the 2nd and 3rd represents the original state (before taking the action) and the state of arrival (after taking the action). Below a summary diagram.

![mdp_pro](./img/mdp_rpo.png)

---