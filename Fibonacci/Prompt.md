
Create index.html and related CSS, JS:

Title of the web page: 
"Fibonacci Numbers Calculation Algorithm Performance Comparison""

Structure of index.html

Section 0: Fibbinaci Run Time Comparisons

Data:
```
n,fib_iterative,fib_iterative_optimized,fib_memo,fib_matrix
10,2.86102294921875e-06,9.5367431640625e-07,3.0994415283203125e-06,1.0013580322265625e-05
100,7.152557373046875e-06,3.0994415283203125e-06,1.0013580322265625e-05,1.2874603271484375e-05
200,9.298324584960938e-06,6.198883056640625e-06,1.7881393432617188e-05,1.5974044799804688e-05
500,3.719329833984375e-05,1.6927719116210938e-05,6.198883056640625e-05,2.002716064453125e-05
1000,6.67572021484375e-05,3.814697265625e-05,0.00011801719665527344,2.5033950805664062e-05
5000,0.0005660057067871094,0.00040340423583984375,0.0008132457733154297,0.00013709068298339844
10000,0.0023758411407470703,0.0016300678253173828,0.0027680397033691406,0.0004010200500488281
20000,0.008448123931884766,0.005677938461303711,0.009376049041748047,0.001138925552368164
30000,0.017866134643554688,0.012006044387817383,0.019356966018676758,0.0016720294952392578
40000,0.03313422203063965,0.02028799057006836,0.03336310386657715,0.003522157669067383
50000,0.04944109916687012,0.03174018859863281,0.053086042404174805,0.004241943359375
60000,0.07253313064575195,0.04559898376464844,0.07424211502075195,0.005203962326049805
70000,0.09551477432250977,0.06156802177429199,0.10172724723815918,0.009676933288574219
80000,0.12384605407714844,0.07849907875061035,0.12499594688415527,0.010717153549194336
90000,0.15742015838623047,0.10072088241577148,0.16397833824157715,0.013051271438598633
100000,0.19235467910766602,0.12029099464416504,0.20043182373046875,0.013135194778442383
```

Plot graphs (linear, log) to compare the run time
x-axis: n
y-axis: run time

suggested lib: charts.js

Section 1: Findings

Base on the data on Section 1, write your findings here. 

Section 2: 

Define what is a Fibonnaci sequence. 

Section 2.1:

Visualise Fibonacci sequence using animation is actually revealing the Fibonacci spiral. This spiral, originated from the Fibonacci sequence, is often compared to the Golden Ratio Spiral,  a spiral commonly found in nature. (To be honest I once thought both were the same, but the fact is that this spiral gets closer and closer to the golden ratio spiral as it ventures towards infinity)
 
Section 3: Explain Space complexity, time complexity and space-time trade-off

Section 4: Explain the algorithms used

- Recursive (Naive)
- Iterative (DP)
- Iterative (DP, Optimized)
- Memoization
- Matrix Exponentiation

Section 4: 
Calculate mathematically the time/space complexity of the 5 mentioned algorithms in Section 4

Section 5: 
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

Also refer to `README.md` and `fibonacci.py` for more information 