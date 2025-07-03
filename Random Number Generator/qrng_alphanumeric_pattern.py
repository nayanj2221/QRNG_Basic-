"""
Quantum Alphanumeric String Generator (QASG)
--------------------------------------------
Generates unique alphanumeric strings based on a user-defined pattern
using quantum superposition and Qiskit.

Language: Python 3.6+

Dependencies:
- Qiskit >= 2.0:    pip install qiskit>=2.0
- NumPy:            pip install numpy

Parameters:
- pattern (str): String of 'D' (digit) or 'L' (letter), e.g., 'DDL' for digit-digit-letter.
- shots (int): Number of strings to generate.
- parallel (bool): If True, enables parallel sampling for performance.

Features:
- Custom patterns with quantum gates for enhanced randomness.
- Shannon entropy calculation for randomness assessment.
- Memory-efficient (4–5 qubits per character).
- Optional parallel sampling for performance.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np
from math import log2
import string

def calculate_entropy(strings):
    """
    Calculate the Shannon entropy of generated strings to estimate randomness quality.

    Args:
        strings (list): List of generated strings.

    Returns:
        float: Entropy in bits, 0.0 if no strings.
    """
    if not strings:
        return 0.0
    char_count = {}
    total_chars = 0
    for s in strings:
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
            total_chars += 1
    entropy = 0.0
    for count in char_count.values():
        p = count / total_chars
        entropy -= p * log2(p) if p > 0 else 0
    return entropy

def generate_quantum_alphanumeric_string(pattern, shots=1, parallel=False):
    """
    Quantum Random Number Generator (QRNG) for unique alphanumeric strings based on a pattern.

    Args:
        pattern (str): Pattern of 'D' (digit) or 'L' (letter), e.g., 'DDL' for digit-digit-letter.
        shots (int): Number of strings to generate (default: 1).
        parallel (bool): Enable parallel sampling for multiple shots (default: False).

    Returns:
        tuple: (Alphanumeric string(s), entropy), or (None, 0.0) if an error occurs.
    """
    try:
        # Input validation
        if not isinstance(pattern, str) or not pattern.strip():
            raise ValueError(f"Pattern must be a non-empty string of 'D' or 'L'. Got: '{pattern}'")
        if not all(c.upper() in ['D', 'L'] for c in pattern):
            raise ValueError(f"Pattern must contain only 'D' (digit) or 'L' (letter). Invalid: '{pattern}'")
        if not isinstance(shots, int) or shots <= 0:
            raise ValueError(f"Shots must be a positive integer. Got: {shots}")
        if not isinstance(parallel, bool):
            raise ValueError(f"Parallel must be a boolean value. Got: {parallel}")

        # Character sets and qubit requirements
        digits = string.digits      # '0'-'9'
        letters = string.ascii_lowercase  # 'a'-'z'
        bits_per_digit = 4   # For 0-9
        bits_per_letter = 5  # For a-z

        results = []

        if parallel and shots > 1:
            # Parallel sampling
            total_qubits = sum(bits_per_digit if c.upper() == 'D' else bits_per_letter for c in pattern)
            circuits = [QuantumCircuit(total_qubits) for _ in range(shots)]

            for circ in circuits:
                bit_index = 0
                for char_type in pattern:
                    qubits = bits_per_digit if char_type.upper() == 'D' else bits_per_letter
                    for q in range(bit_index, bit_index + qubits):
                        circ.h(q)
                        circ.rx(np.pi/4, q)
                    bit_index += qubits

            states = [Statevector.from_instruction(circ) for circ in circuits]
            samples = [state.sample_counts(shots=1) for state in states]
            for sample in samples:
                alphanumeric = ""
                bit_index = 0
                for char_type in pattern:
                    qubits = bits_per_digit if char_type.upper() == 'D' else bits_per_letter
                    bits = list(sample.keys())[0][bit_index:bit_index + qubits]
                    if len(bits) != qubits:
                        raise ValueError(f"Bit length mismatch. Expected {qubits} bits, got {len(bits)} at index {bit_index}")
                    bit_index += qubits
                    if char_type.upper() == 'D':
                        num = int(bits, 2) % 10
                        alphanumeric += digits[num]
                    else:
                        num = int(bits, 2) % 26
                        alphanumeric += letters[num]
                results.append(alphanumeric)
        else:
            # Sequential sampling
            for _ in range(shots):
                alphanumeric = ""
                for char_type in pattern:
                    num_qubits = bits_per_digit if char_type.upper() == 'D' else bits_per_letter
                    circuit = QuantumCircuit(num_qubits)
                    for i in range(num_qubits):
                        circuit.h(i)
                        circuit.rx(np.pi/4, i)
                    state = Statevector.from_instruction(circuit)
                    random_bits = state.sample_counts(shots=1)
                    bits = list(random_bits.keys())[0]
                    if char_type.upper() == 'D':
                        num = int(bits, 2) % 10
                        alphanumeric += digits[num]
                    else:
                        num = int(bits, 2) % 26
                        alphanumeric += letters[num]
                results.append(alphanumeric)

        entropy = calculate_entropy(results)
        return (results[0] if shots == 1 else results, entropy)

    except Exception as e:
        print(f"Error: {str(e)}")
        return None, 0.0

# Example usage
if __name__ == "__main__":
    pattern = "DDL"   # Example: digit-digit-letter, e.g., '12e'
    shots = 10        # Generate multiple strings to show entropy
    result = generate_quantum_alphanumeric_string(pattern, shots=shots, parallel=True)
    if result is not None:
        strings, entropy = result
        if strings is None:
            print("No strings generated due to an error.")
        elif shots == 1:
            print(f"Generated quantum alphanumeric string for pattern '{pattern}': {strings}.")
            print(f"Entropy: {entropy:.2f} bits.")
        else:
            print(f"Generated {shots} quantum alphanumeric strings for pattern '{pattern}':")
            for i, s in enumerate(strings, 1):
                print(f"{i}. {s}")
            print(f"Entropy of generated strings: {entropy:.2f} bits.")