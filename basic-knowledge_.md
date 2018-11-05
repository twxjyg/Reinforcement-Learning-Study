# What is Reinforcement Learning
  
TBD
# Markov Decision Processes
  
Markov Decision Processes try to give us a framework, the framework need we describe our problem
with these important concepts:
|Concept | Math present| Describetion |
|---:|:------:|:---|
|States| <img src="https://latex.codecogs.com/gif.latex?S"/> | describes the world's state|
|Model|<img src="https://latex.codecogs.com/gif.latex?T(s,a,s^{&#x5C;prime})%20=%20P(s^{&#x5C;prime}&#x5C;|s,%20a)"/>| T is Transition Model function it give that the probability that if you were in state s, and you toke action a and you end up transitioning with state s^{\prime}|
|Actions|<img src="https://latex.codecogs.com/gif.latex?A(s)"/>, A|the actions you can do in the world|
|Reward|R(s), R(s, a), R(s, a, s^{\prime})|Reward function give you some rewards when you were in state s, or you were in state s and toke action a, or you were in state a and toke action a and you end up transitioning at <img src="https://latex.codecogs.com/gif.latex?s^{&#x5C;prime}"/>|
|Policy|<img src="https://latex.codecogs.com/gif.latex?&#x5C;pi(s)=a,%20&#x5C;pi^{*}"/> | <img src="https://latex.codecogs.com/gif.latex?&#x5C;pi(s)"/> is policy we need to find and it give that when you were in state s and what action you should take in the next step and this policy can help you find the answer or get destination or whatever, and <img src="https://latex.codecogs.com/gif.latex?&#x5C;pi^{*}"/> is the best policy you found in these all possible policies|
  
States, Model(Transition Model), Actions, Reward they are problem, Policy is the solution.
  
## Reward function
  
  
Try to think about whats the different if your reward function is <img src="https://latex.codecogs.com/gif.latex?R(s)%20=%202"/> and <img src="https://latex.codecogs.com/gif.latex?R(s)%20=%20-2"/>, that mean whatever state you are, you will get 2 or -2 reward, that the simplest reward function. 
<img src="https://latex.codecogs.com/gif.latex?R(2)%20=%202"/> will encourage you to stay in the world insteal of getting terminal state.
<img src="https://latex.codecogs.com/gif.latex?R(2)%20=%202"/> will keep you want to leave away from the world.
  
## Stationary Preferences
  
  
if you use s util function to compare two sequence of state like:
<img src="https://latex.codecogs.com/gif.latex?U_{1}(s_{0},%20s_{1},%20s_{2},%20s_{3},%20s_{4},%20...)"/>
<img src="https://latex.codecogs.com/gif.latex?U_{2}(s_{0},%20s_{1}^{&#x5C;prime},%20s_{2}^{&#x5C;prime},%20s_{3}^{&#x5C;prime},%20s_{4}^{&#x5C;prime},%20...)"/>
and you get the conclusion that <img src="https://latex.codecogs.com/gif.latex?U_{1}%20&gt;%20U_{2}"/>
then for these two sequence of state:
<img src="https://latex.codecogs.com/gif.latex?U_{1}(s_{1},%20s_{2},%20s_{3},%20s_{4},%20...)"/>
<img src="https://latex.codecogs.com/gif.latex?U_{2}(s_{1}^{&#x5C;prime},%20s_{2}^{&#x5C;prime},%20s_{3}^{&#x5C;prime},%20s_{4}^{&#x5C;prime},%20...)"/>
you will also think:
<img src="https://latex.codecogs.com/gif.latex?U_2%20&gt;%20U_3"/>
that is the stationary preferences
  
## Sequences of Reward
  
  
if one kind of U function like this:
<img src="https://latex.codecogs.com/gif.latex?U(s_{0},%20s_{1},%20s_{2},%20s_{3},%20...)%20=%20&#x5C;sum_{t=0}^{&#x5C;infin}%20R(s_t)%20=%20&#x5C;infin"/>
that's true because the reward is always positive.
this is a typical infinite world situation, if your U function like this, each step of your decision making will be nothing.
but if your U function like this:
<img src="https://latex.codecogs.com/gif.latex?U(s_{0},%20s_{1},%20s_{2},%20s_{3},%20...)%20=%20&#x5C;sum_{t=0}^{&#x5C;infin}%20&#x5C;gamma^{t}R(t)"/>
the <img src="https://latex.codecogs.com/gif.latex?&#x5C;gamma^{t}"/> will change the thing to a situation that you still in a infinite world but you will reach a point that whatever you choose to go, you never get the bound of the world.
also you will get a equition:
<img src="https://latex.codecogs.com/gif.latex?U%20&lt;=%20&#x5C;sum_{t%20=%200}^{&#x5C;infin}&#x5C;gamma^{t}R_{max}%20=%20&#x5C;frac{R_{max}}{1%20-%20&#x5C;gamma}"/>
because:
<img src="https://latex.codecogs.com/gif.latex?x%20=%20(&#x5C;gamma^{0}%20+%20&#x5C;gamma^{1}%20+%20&#x5C;gamma^{2}%20+%20&#x5C;gamma^{3}%20+%20...)"/>
<img src="https://latex.codecogs.com/gif.latex?x%20=&#x5C;gamma^{0}%20+%20&#x5C;gamma%20&#x5C;cdot%20(&#x5C;gamma^{0}%20+%20&#x5C;gamma^{1}%20+%20&#x5C;gamma^{2}%20+%20...)"/>
<img src="https://latex.codecogs.com/gif.latex?x%20=%20&#x5C;gamma^{0}%20+%20&#x5C;gamma%20&#x5C;cdot%20x"/>
<img src="https://latex.codecogs.com/gif.latex?x%20=%20&#x5C;frac{&#x5C;gamma^{0}}{1%20-%20&#x5C;gamma}"/>
so:
<img src="https://latex.codecogs.com/gif.latex?&#x5C;sum_{t%20=%200}^{&#x5C;infin}&#x5C;gamma^{t}R_{max}%20=%20&#x5C;frac{R_{max}}{1%20-%20&#x5C;gamma}%20=%20%20&#x5C;frac{&#x5C;gamma^{0}}{1%20-%20&#x5C;gamma}%20&#x5C;cdot%20R_{max}"/>
  
  
## Policies
  
  
How we use mathematic way to express policy function:
<img src="https://latex.codecogs.com/gif.latex?&#x5C;pi^{*}%20=%20&#x5C;underset{&#x5C;pi}{argmax}%20E[&#x5C;sum_{t=0}^{&#x5C;infin}&#x5C;gamma^{t}R(s_{t})|&#x5C;pi]"/>
that means the optimal policy is that if we follow this policy, we can get a sequences of states and it's corresponding rewards sum is max. Also the rewards is discounted by <img src="https://latex.codecogs.com/gif.latex?&#x5C;gamma"/> factor.
  
Next how to express the utility of s:
<img src="https://latex.codecogs.com/gif.latex?U^{&#x5C;pi}(s)%20=%20E[&#x5C;sum_{t=0}^{&#x5C;infin}&#x5C;gamma^{t}R(s_{t})|&#x5C;pi,%20s_{0}%20=%20s]"/>
so the utility of s is the long term reward of current state reward plus all the other rewards follow the policy <img src="https://latex.codecogs.com/gif.latex?&#x5C;pi"/> which is the rewards from s on to the infinite state.
  
Note: R(s) is immediately feedback/reward U(s) is long term feedback/reward
  
if we have utility we have new policy function:
<img src="https://latex.codecogs.com/gif.latex?&#x5C;pi^{*}(s)%20=%20&#x5C;underset{a}{argmax}&#x5C;sum_{s^{&#x5C;prime}}T(s,a,s^{&#x5C;prime})U(s^{&#x5C;prime})"/>
Now the utility is always follow the optimal policy:
<img src="https://latex.codecogs.com/gif.latex?U(s)%20=%20U^{&#x5C;pi^{*}}(s)"/>
  
It's means the optimal policy for every state, return the action a that maximizes my expected utility. This is recursive function because we use optimal policy <img src="https://latex.codecogs.com/gif.latex?&#x5C;pi^{*}"/> to calculate itself, later we will make it possible.
  
## Bellman Equation
  
Now we introduce bellman equation:
<img src="https://latex.codecogs.com/gif.latex?U(s)%20=%20R(s)%20+%20&#x5C;gamma%20&#x5C;underset{a}{max}&#x5C;sum_{s^{&#x5C;prime}}T(s,a,s^{&#x5C;prime})U(s^{&#x5C;prime})"/>
We ganna use <img src="https://latex.codecogs.com/gif.latex?U(s^{&#x5C;prime})"/> to calculate <img src="https://latex.codecogs.com/gif.latex?U(s)"/>, the utility equals immediately reward at state s plus discounted utility that use the action a which maximizes the long term rewards from s on.
  
## Finding Policies 1
  
  
Right now we have Bellman equation, and we don't know how to solve U(s), the Value Iteration method could be a way to solve it but I don't know why, so let do a quiz:
![finding policy](finding-policy-quiz.png )
What we need to know is, all the state initial utility is ZERO except green grid and red grid its One and negative One:
<img src="https://latex.codecogs.com/gif.latex?U_{1}(x)%20=%20R(x)%20+%20&#x5C;gamma%20&#x5C;underset{a}{max}&#x5C;begin{cases}%20%20%20%20&#x5C;sum_{a_{up}}T(x,%20a_{up},%20x^{up})U_{0}(x^{up})%20&#x5C;&#x5C;%20%20%20%20&#x5C;sum_{a_{down}}T(x,%20a_{down},%20x^{down})U_{0}(x^{down})%20&#x5C;&#x5C;%20%20%20%20&#x5C;sum_{a_{left}}T(x,%20a_{left},%20x^{left})U_{0}(x^{left})%20&#x5C;&#x5C;%20%20%20%20&#x5C;sum_{a_{right}}T(x,%20a_{right},%20x^{right})U_{0}(x^{right})&#x5C;end{cases}"/>
then we choose the max one:
<img src="https://latex.codecogs.com/gif.latex?U_{1}(x)%20=%20-0.04%20+%200.5%20&#x5C;times%20&#x5C;underset{a}{max}&#x5C;begin{cases}%20%20%20%200.8&#x5C;times0+0.1&#x5C;times1+0.1&#x5C;times0%20=%200.1%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times0+0.1&#x5C;times1+0.1&#x5C;times0%20=%200.1%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0%20=%200%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times1+0.1&#x5C;times0+0.1&#x5C;times0%20=%200.8&#x5C;end{cases}%20=%20-0.04%20+%200.5&#x5C;times(0.8&#x5C;times1+0.1&#x5C;times0+0.1&#x5C;times0)%20=%200.36"/>
  
This was because we always want max value so we first choose to go right to red grid at same time we have 0.2 probability to go wrong direction to go down and go up.
When we go up and down, we'll get ZERO utility because initial utility is ZERO. Next we use <img src="https://latex.codecogs.com/gif.latex?U_{1}(x)"/> to solve <img src="https://latex.codecogs.com/gif.latex?U_{2}(x)"/>:
<img src="https://latex.codecogs.com/gif.latex?U_{2}(x)%20=%20R(x)%20+%20&#x5C;gamma%20&#x5C;underset{a}{max}&#x5C;begin{cases}%20%20%20%20&#x5C;sum_{a_{up}}T(x,%20a_{up},%20x^{up})U_{1}(&#x5C;colorbox{green}x)%20&#x5C;&#x5C;%20%20%20%20&#x5C;sum_{a_{down}}T(x,%20a_{down},%20x^{down})U_{1}(x^{down})%20&#x5C;&#x5C;%20%20%20%20&#x5C;sum_{a_{left}}T(x,%20a_{left},%20x^{left})U_{1}(x^{left})%20&#x5C;&#x5C;%20%20%20%20&#x5C;sum_{a_{right}}T(x,%20a_{right},%20x^{right})U_{1}(x^{right})&#x5C;end{cases}"/>
as you see we need to get <img src="https://latex.codecogs.com/gif.latex?U_{1}(x^{up|down|left|right})"/>, we can fellow the function <img src="https://latex.codecogs.com/gif.latex?U_{1}(x)"/> way to get it, so:
<img src="https://latex.codecogs.com/gif.latex?U_{1}(x^{up})"/> is out of grid so we assume <img src="https://latex.codecogs.com/gif.latex?U_1{x^{up}}%20=%200"/>.
  
<img src="https://latex.codecogs.com/gif.latex?U_{1}(x^{down})%20=%20-0.04%20+%200.5%20&#x5C;times%20&#x5C;underset{a}{max}&#x5C;begin{cases}%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times-1%20=%20-0.1%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times-1%20=%20-0.1%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0%20=%200%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times-1+0.1&#x5C;times0+0.1&#x5C;times0%20=%20-0.8&#x5C;end{cases}"/>
<img src="https://latex.codecogs.com/gif.latex?=%20-0.04%20+%200.5&#x5C;times(0.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0)%20=%20-0.04"/>
  
<img src="https://latex.codecogs.com/gif.latex?U_{1}(x^{left})%20=%20-0.04%20+%200.5%20&#x5C;times%20&#x5C;underset{a}{max}&#x5C;begin{cases}%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0%20=%200%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0%20=%200%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0%20=%200%20&#x5C;&#x5C;%20%20%20%200.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0%20=%200&#x5C;end{cases}"/>
<img src="https://latex.codecogs.com/gif.latex?=%20-0.04%20+%200.5&#x5C;times(0.8&#x5C;times0+0.1&#x5C;times0+0.1&#x5C;times0)%20=%20-0.04"/>
  
<img src="https://latex.codecogs.com/gif.latex?U_{1}(x^{right})"/> is already given with 1 so <img src="https://latex.codecogs.com/gif.latex?U_{1}(x^{right})%20=%201"/>
  
now let's use above result to get <img src="https://latex.codecogs.com/gif.latex?U_{2}(x)"/>:
<img src="https://latex.codecogs.com/gif.latex?U_{2}(x)%20=%20-0.04%20+%200.5%20&#x5C;times%20&#x5C;underset{a}{max}&#x5C;begin{cases}0.8%20&#x5C;times%200.36%20+%200.1%20&#x5C;times%20-0.04%20+%200.1%20&#x5C;times%201%20=%20%200.384%20&#x5C;&#x5C;0.8%20&#x5C;times%20-0.04%20+%200.1%20&#x5C;times%20-0.04%20+%200.1%20&#x5C;times%201%20=%20%200.064%20&#x5C;&#x5C;0.8%20&#x5C;times%20-0.04%20+%200.1%20&#x5C;times%200.36%20+%200.1%20&#x5C;times%20-0.04%20=%20%200%20&#x5C;&#x5C;0.8%20&#x5C;times%201%20+%200.1%20&#x5C;times%200.36%20+%200.1%20&#x5C;times%20-0.04%20=%200.832&#x5C;end{cases}"/>
<img src="https://latex.codecogs.com/gif.latex?=%20-0.04%20+%200.5&#x5C;times(0.8%20&#x5C;times%201%20+%200.1%20&#x5C;times%200.36%20+%200.1%20&#x5C;times%20-0.04)%20=%200.376"/>
  
  
<img src="https://latex.codecogs.com/gif.latex?U_{2}(x)%20=%20-0.04%20+%200.5(0.8%20&#x5C;times%201%20+%200.1%20&#x5C;times%200.36%20+%200.1%20&#x5C;times%20-0.04)%20=%200.376"/>
  
Now we get <img src="https://latex.codecogs.com/gif.latex?U_{2}(x)"/>, the most interesting thing is I found current Utility of state is similar to anergy spreading from center on, in our situation, the anergy center is <img src="https://latex.codecogs.com/gif.latex?x^{right}"/> who's Utility is 1, other utility of state is like under anergy spreading and their value is smaller than center, the smallest one is most faraway one:
![anwser](quiz-anwser.png )
  
## Finding Policies 2
  
  
So far we learned about getting Utility, and before we have been informed that the policy equation <img src="https://latex.codecogs.com/gif.latex?&#x5C;pi^{*}(s)%20=%20a"/> need the core components U(s) to solve it, so next we will use the important result to find policy.
  
  
  