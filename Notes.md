"Even with a discount factor only slightly lower than 1, Q-function learning leads to propagation of errors and instabilities when the value function is approximated with an artificial neural network.[7] In that case, starting with a lower discount factor and increasing it towards its final value accelerates learning.[8]"

**Current To Dos:**

### ToDO

##### Code:

Prio 1:

* check deepQ logging (do i log target or local)
* for NN: verify value ranges of inputs
* reduce narrowness at trophy/construct goal
* add orientation state (y position, xy dist/orientation toof trophy to checkpoint...) to state (? - policy vs observations)
  * if I wont to keep it robust and not have checkpoints in inference, distance to checkpoint should not be included in state
* Add later exploration impulses: Annilated / Sinus-based decay or coupled with progress in learning Q
* Analyse Q table via 2/3D-PCA - any paths? (good if smooth edges between paths) or bad: isolated maxima/uniform patterns/jumps?. Maybe mark maxQ paths

Prio 2:

* add logging: growth of Qtable, n checkpoints reached, win/loss
* Re-Check binning: 0 of direction, speed as float


Later:

* Fix Penalty for top wall (move trophy?)

Viz:

* Live graph of logging metrics

With DeepQ via NN:

* replay buffer with LSTM sequences
* Policy-gradient approaches (PPO)
* Soft actor-critic

Done:

* smoothen out distance penalty
* dynamic reward_dict
* debugging binning (still not ideal ideal)
* For NN/meaningful binning: Direction as sin/cos (?)
* reduce backwarsd speed so that it advances forward preferrably
* time penalty? -x at destination



# Key Takeaways

### QTable

* Most important:
  * Meaningful discretization of continuous state - each bin needs a meaning
  * Reward shaping until smooth and meaningful everywhere
* Overwriting Q-values if win/loss or level checkpoint gives the push
* Explicit guidance: level checkpoints really helpful
* Adding minimal resting speed helps with being stuck in local minima

### DeepQ

v0:
* Learns wall penalty quite fast
* But the opening of checkpoint vs penatly of wall seems to get lost as noise
v1:
* add distance/angle to checkpoint&trophy, and checkpoint extra reward and penalty if gone below previous checkpoint again
* a lot of oscillations
* Larger state = way longer learning right at the start. does not learn well