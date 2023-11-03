# Differential Uniformity
### Description

Differential uniformity is a critical measure used in the evaluation of cryptographic primitives, especially in assessing the security of functions like S-boxes in block ciphers. It quantifies a function's resistance to differential cryptanalysis by measuring the worst-case scenario of a non-trivial input difference leading to a specific output difference.

In essence, for a function over a finite field, differential uniformity gauges the maximum number of input values that, when XORed with a given non-zero input difference, result in a specified non-zero output difference. Lower differential uniformity values indicate better resistance against differential cryptanalysis.

### Python Script

The provided Python script computes the differential uniformity for a specified S-box (substitution box) function:

1. A toy S-box function is defined which maps inputs to outputs.
2. The differential_uniformity function computes the differential uniformity of the given S-box:
        It iterates over all possible non-zero input and output differences.
        For each pair of differences, it counts the number of input values that satisfy the differential property.
        It tracks the maximum count across all differential pairs.
3. The script finally prints the computed differential uniformity of the S-box.

### Usage

```python
def s_box(input_value):
    # Replace this with your S-box function.
    pass

print("Differential Uniformity of the S-box:", differential_uniformity(s_box))
```

To compute the differential uniformity of your S-box, replace the toy s_box function with your desired function.
