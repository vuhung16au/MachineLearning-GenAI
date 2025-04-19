
Create index.html and related CSS, JS:

Title of the web page: 
"Performance of Algorithsm for Minimum Coin Change Problem"

Structure of index.html

Section 0: Fibbinaci Run Time Comparisons

Data:


runtime for US coins:
```
Amount,Memoized DP (Recursive),Memoized DP (Iterative),Bottom-Up DP,Greedy
734,0.0016908645629882812,0.001569986343383789,0.0005049705505371094,5.7220458984375e-06
1000,0.002452373504638672,0.0024051666259765625,0.0007419586181640625,5.0067901611328125e-06
2001,0.004880189895629883,0.004127025604248047,0.0013308525085449219,1.0013580322265625e-05
3003,0.00795602798461914,0.0053060054779052734,0.0015468597412109375,4.0531158447265625e-06
5000,0.008040904998779297,0.007536172866821289,0.002366304397583008,3.0994415283203125e-06
```
runtime for standard coins:
```
Amount,Memoized DP (Recursive),Memoized DP (Iterative),Bottom-Up DP,Greedy
734,0.0022039413452148438,0.002128124237060547,0.0006780624389648438,1.0967254638671875e-05
1000,0.002905130386352539,0.0025298595428466797,0.0008089542388916016,4.76837158203125e-06
2001,0.004912137985229492,0.0029370784759521484,0.001461029052734375,4.76837158203125e-06
3003,0.006478786468505859,0.005897045135498047,0.0017991065979003906,4.0531158447265625e-06
5000,0.008990049362182617,0.008638143539428711,0.002565145492553711,6.198883056640625e-06

```
runtime for prime coins:
```
Amount,Memoized DP (Recursive),Memoized DP (Iterative),Bottom-Up DP,Greedy
734,0.003110170364379883,0.00205230712890625,0.0003991127014160156,6.198883056640625e-06
1000,0.004837989807128906,0.0018630027770996094,0.0005507469177246094,4.0531158447265625e-06
2001,0.01987481117248535,0.0038251876831054688,0.0011668205261230469,7.867813110351562e-06
3003,0.00556492805480957,0.005759000778198242,0.0016939640045166016,7.867813110351562e-06
5000,0.009869098663330078,0.009532928466796875,0.0030050277709960938,1.2874603271484375e-05

```

runtime for binary coins:
```
Amount,Memoized DP (Recursive),Memoized DP (Iterative),Bottom-Up DP,Greedy
734,0.0013279914855957031,0.0011188983917236328,0.0003769397735595703,4.76837158203125e-06
1000,0.0017228126525878906,0.001870870590209961,0.0005950927734375,1.6689300537109375e-06
2001,0.00526118278503418,0.005318880081176758,0.0017330646514892578,5.7220458984375e-06
3003,0.007047176361083984,0.0066950321197509766,0.0020329952239990234,4.0531158447265625e-06
5000,0.010161161422729492,0.009437084197998047,0.002872943878173828,5.9604644775390625e-06
```

Plot graphs to compare the run time
x-axis: amount
y-axis: run time

suggested lib: charts.js

Section 1: Findings

Base on the data on Section 1, write your findings here. 

Section 2: 

Define what is a the the "coin minimum problem" and the objectives & the approaches (algorithms) to solve the problem

Hint: 
```
The minimum coin change problem involves finding the smallest number of coins needed to make a target amount using given coin denominations. For example, with coins [1, 2, 5] and a target of 7, the answer is 2 coins (5 + 2). Dynamic programming is a powerful approach to solve this problem efficiently, ensuring the optimal solution. Below, I’ll present Python code implementing multiple algorithms, compare their performance, and explain their mathematical foundations.
```
Section 2.1:

Visualise how to solve the "coin minimum problem"

Section 3: Explain Space complexity, time complexity and space-time trade-off

Section 4: Explain the algorithms used

Section 4.1: 
Algorithm 1: Naive Recursive Approach (we don't implement it because it is too slow)

Section 4.2: 
Algorithm 2: Memoized Recursive Approach (Top-Down DP)

Section 4.3:
Algorithm 3: Bottom-Up Dynamic Programming

Section 4.4:
Algorithm 4: Greedy Approach (for comparison)


Section 5: 
Calculate mathematically the time/space complexity of the mentioned algorithms in Section 4

Section 6: 
Write conclusion

Footer of index.html

Add link to github repo: 
https://github.com/vuhung16au/MachineLearning-GenAI

Other requirements: 

use:
mathjax-config.js
es6-promise.auto.min.js

Put all CSS files under folder ./css
Put all JavaScripts files under folder ./js

Add anchor to each section so that users can jump to sections (i.e: index.html#SectionName)

Tone/style:
Use simple English to make it easy to understand.
The target audience is ppl new to algorithm.

Also refer to `README.md`, `Grok.md` and `coin-minimum.py` for more information 