# Differential Uniformity

### Description
--- 
Differential uniformity is a critical measure used in the evaluation of cryptographic primitives, especially in assessing the security of functions like S-boxes in block ciphers. This metric is integral to the domain of symmetric cryptography, where ensuring resistance to known attack vectors is paramount.

#### Understanding the Score:
The score, often denoted by Δ, represents the worst-case scenario differential, quantifying the non-uniformity of the function concerning differential properties. In simpler terms, it indicates the highest number of times a particular output difference can be achieved for a given input difference.

- A **perfect score** would be 2, implying that for every input difference (except the trivial zero difference), there are precisely two input pairs that lead to the specific output difference.
- A **higher score** indicates a higher likelihood of predicting an output difference for a given input difference, thus making the cryptographic function more susceptible to differential attacks.

#### Implications of the Score:
- **Lower Scores are Preferred:** A lower score implies that the S-box or the function exhibits a more random behavior, making it difficult for attackers to exploit patterns using differential cryptanalysis.
- **Not the Only Metric:** While differential uniformity is essential, it is one of many metrics used to evaluate S-boxes. Other properties like non-linearity, bijectiveness, and absence of fixed points also play crucial roles in determining the security of an S-box.

In essence, for a function over a finite field, differential uniformity gauges the maximum number of input values that, when XORed with a given non-zero input difference, result in a specified non-zero output difference. In the realm of cryptography, where unpredictability and resistance to attacks are of utmost importance, aiming for lower differential uniformity values in functions like S-boxes is crucial to ensure robust security.

### Python Script
---
The provided Python script computes the differential uniformity for a specified S-box (substitution box) function:

1. A toy S-box function is defined which maps inputs to outputs.
2. The differential_uniformity function computes the differential uniformity of the given S-box:
        It iterates over all possible non-zero input and output differences.
        For each pair of differences, it counts the number of input values that satisfy the differential property.
        It tracks the maximum count across all differential pairs.
3. The script finally prints the computed differential uniformity of the S-box.

### Usage
---
```python
def s_box(input_value):
    # A toy example of an S-box. In real-world scenarios, this would be more complex (duh).
    sbox = [3, 1, 0, 2]
    return sbox[input_value]

print("Differential Uniformity of the S-box:", differential_uniformity(s_box))
```

To compute the differential uniformity of your S-box, replace the toy s_box function with your desired function.
