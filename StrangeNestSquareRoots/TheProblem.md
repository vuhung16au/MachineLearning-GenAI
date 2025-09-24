# Strange nested square roots

Let $x_{k+1} = 2x_k\sqrt{1 - x_k^2}$ with initial condition $x_0 \in [0,1]$. 


- Find an $x_0$ such that all $x_k$ are rational numbers. 

- The sequence $(x_k)$ represents a **discrete dynamical system**. 
Find its main **invariant measure** using AI. Explain what it means, and find related systems and their main invariant measure using AI. 

- Can there be more than one invariant measure? 

- Establish the connection to **normal numbers** via the **dyadic map** (a related dynamical system). 

- Show that these systems are **ergodic**, and explain this concept and the role that it plays, in layman's terms, using AI.

## Solution

Let $(p, r, q)$ be a **Pythagorean triple** [Wiki]. That is, $p, q, r$ are integers with $p^2 + r^2 = q^2$. If $x_k = \frac{p}{q}$ then it is easy to show that

$$x_{k+1} = \frac{p'}{q'}$$

with $p' = 2p\sqrt{q^2 - p^2}$, $q' = q^2$, $r' = q^2 - 2p$,

defines a new Pythagorean triple $(p', q', r')$. So $x_0 = \frac{3}{5}$ works. This answers the first question. Now, the prompt "invariant measure of mapping x to 2x sqrt(1-x^2) on [0, 1]" leads to

$$f_X(x) = \frac{2}{\pi}\frac{1}{\sqrt{1-x^2}}, \quad 0 \leq x \leq 1 \quad (1.28)$$

which is the correct probability density function. Typically AI explains what it is along with the computation. Try with different LLMs to confirm that they all return this result. This is not an easy problem, as it requires solving a **stochastic integral equation**. AI may suggest the logistic map as a sister mapping.

If you start with almost any $x_0 \in [0,1]$, the sequence $(x_k)$ is aperiodic and the **empirical distribution** of the successive values has a density approaching (1.28) as the number of terms increases. There are exceptions, for instance, if $x_0$ is such that $x_0 = x_{10}$. Likewise in the dyadic map $x_{k+1} = 2x_k - \lfloor 2x_k \rfloor$, if $x_0$ is a rational number, the sequence is periodic and will not follow the main invariant measure: the uniform distribution on $[0,1]$. Otherwise $x_0$ is called a **normal number**. The ergodic property is used in proving these results. It states that you can retrieve the invariant measure using one infinite sequence with a single seed $x_0$, or using infinitely many very short sequences $(x_0, x_1)$, each one with a random seed $x_0$. For a table of related dynamical systems and their invariant measure, see section 3.2 (probabilistic properties of numeration systems) in [12].
