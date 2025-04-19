# Coin Minimum Problem - Decision Tree Visualization

The coin minimum problem aims to find the minimum number of coins needed to make a specific amount of money, given a set of coin denominations.

```mermaid
graph TD
    A[Start: Amount = 11; Coins = 1, 5, 10] --> B[Choose coin 1]
    A --> C[Choose coin 5]
    A --> D[Choose coin 10]
    
    B --> B1[Remaining Amount = 10]
    C --> C1[Remaining Amount = 6]
    D --> D1[Remaining Amount = 1]
    
    B1 --> B2[Choose coin 1]
    B1 --> B3[Choose coin 5]
    B1 --> B4[Choose coin 10]
    
    C1 --> C2[Choose coin 1]
    C1 --> C3[Choose coin 5]
    C1 --> C4[Choose coin 10]
    
    D1 --> D2[Choose coin 1]
    
    B2 --> B21[Remaining Amount = 9]
    B3 --> B31[Remaining Amount = 5]
    B4 --> B41[Remaining Amount = 0; Solution: 2 coins]
    
    C2 --> C21[Remaining Amount = 5]
    C3 --> C31[Remaining Amount = 1]
    C4 --> C41[Invalid]
    
    D2 --> D21[Remaining Amount = 0; Solution: 2 coins]
    
    B21 --> B211[...]
    B31 --> B311[Choose coin 5]
    
    C21 --> C211[Choose coin 5]
    C31 --> C311[Choose coin 1]
    
    B311 --> B3111[Remaining Amount = 0; Solution: 3 coins]
    C211 --> C2111[Remaining Amount = 0; Solution: 3 coins]
    C311 --> C3111[Remaining Amount = 0; Solution: 3 coins]
    
    subgraph Legend
    L1[Optimal solution]
    L2[Valid but non-optimal]
    L3[Invalid path]
    end
    
    style B41 fill:#9f9,stroke:#6c6
    style D21 fill:#9f9,stroke:#6c6
    style B3111 fill:#ffc,stroke:#cc9
    style C2111 fill:#ffc,stroke:#cc9
    style C3111 fill:#ffc,stroke:#cc9
    style C41 fill:#fcc,stroke:#c99
    
    style L1 fill:#9f9,stroke:#6c6
    style L2 fill:#ffc,stroke:#cc9
    style L3 fill:#fcc,stroke:#c99
```

## Explanation:

1. We start with the amount 11 and available coins {1, 5, 10}
2. At each step, we choose one of the available coins
3. We continue until we reach the target amount (0 remaining)
4. The optimal solution is the path with the fewest coins
5. In this example, we have two optimal solutions with 2 coins:
   - Using a 10-cent coin followed by a 1-cent coin
   - Using a 1-cent coin followed by a 10-cent coin

Green nodes represent the optimal solutions, yellow nodes represent valid but non-optimal solutions, and red nodes represent invalid paths.
