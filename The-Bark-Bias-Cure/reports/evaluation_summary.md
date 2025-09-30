
# Dog Behavior Model Evaluation Report

## Dataset Overview
- Total samples: 5,000
- Positive samples: 1,973
- Positive rate: 39.46%

## Overall Performance
- Accuracy: 0.7600
- Precision: 0.7460
- Recall: 0.5940
- F1 Score: 0.6614
- AUC Score: 0.8264

## Bias Analysis Summary
### By Race
- Hispanic: -0.107 bias score
- Middle Eastern: -0.125 bias score
- Black: +0.010 bias score
- Native American: -0.122 bias score
- White: -0.131 bias score
- Asian: -0.006 bias score

### By Gender
- Male: -0.069 bias score
- Non-binary: -0.080 bias score
- Female: -0.094 bias score

## Fairness Metrics
- Race Statistical Parity Difference: 0.5296
- Gender Statistical Parity Difference: 0.1039

## Recommendations
1. High racial bias detected (SPD=0.530). Consider retraining with balanced data or using fairness constraints.
2. High gender bias detected (SPD=0.104). Review feature engineering and consider gender-aware preprocessing.
3. Significant bias detected for Hispanic group (bias=-0.107). Investigate feature importance and data representation.
4. Significant bias detected for Middle Eastern group (bias=-0.125). Investigate feature importance and data representation.
5. Significant bias detected for Native American group (bias=-0.122). Investigate feature importance and data representation.
6. Significant bias detected for White group (bias=-0.131). Investigate feature importance and data representation.
