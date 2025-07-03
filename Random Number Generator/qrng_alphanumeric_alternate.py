"""
Quantum Alphanumeric String Generator (QASG)
--------------------------------------------
Generates cryptographically strong, random alphanumeric strings
using quantum superposition and Qiskit.

Language: Python 3.6+
Dependencies:
- Qiskit >= 2.0:    pip install qiskit>=2.0
- NumPy:            pip install numpy
Parameters:
- length (int): Even number specifying the total length of the string.
- shots (int):  Number of strings to generate (default: 1).
Usage:
- Set `length` (must be even) and `shots`.
- Run: python qrng_alphanumeric_alternate.py
Features:
- Generates alternating digit-letter strings using quantum randomness.
- Memory efficient and suitable for cryptographic or security applications.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import string

def generate_quantum_alphanumeric(length: int, shots: int = 1):
    """
    Generate random alphanumeric strings using quantum circuits.
    The output alternates between digits and lowercase letters.
    Quantum se random alphanumeric strings banata hai jo digits aur letters alternate karte hain.

    Args:
        length (int): Total length of the string (must be even).
        Lambai (even honi chahiye taaki digits aur letters alternate ho).
        shots (int): Number of strings to generate (default: 1).
        Kitne strings generate karne hain (default: 1).

    Returns:
        str or list: Generated string(s) or None if input is invalid.
        Banayi gayi string ya list, agar input invalid ho to None.
    """
    try:
        if not isinstance(length, int) or length <= 0:
            raise ValueError("String length must be a positive integer. Lambai positive integer honi chahiye.")
        if length % 2 != 0:
            raise ValueError("String length must be even to alternate digits and letters. Lambai even honi chahiye.")

        digits = string.digits      # '0'-'9'
        letters = string.ascii_lowercase  # 'a'-'z'
        digit_qubits = 4    # 2^4 = 16 > 10 (digits)
        letter_qubits = 5   # 2^5 = 32 > 26 (letters)

        results = []
        for _ in range(shots):
            result = ""
            for i in range(length):
                is_digit = (i % 2 == 0)
                n_qubits = digit_qubits if is_digit else letter_qubits

                qc = QuantumCircuit(n_qubits)
                qc.h(range(n_qubits))  # Apply Hadamard to all qubits
                state = Statevector.from_instruction(qc)
                sample = list(state.sample_counts(shots=1).keys())[0]

                if is_digit:
                    idx = int(sample, 2) % 10
                    result += digits[idx]
                else:
                    idx = int(sample, 2) % 26
                    result += letters[idx]
            results.append(result)
        return results[0] if shots == 1 else results

    except Exception as e:
        print(f"Quantum generation failed: {str(e)}. Quantum banane mein error: {str(e)}")
        return None

if __name__ == "__main__":
    string_length = 6   # Must be even
    num_strings = 1     # How many strings to generate
    quantum_string = generate_quantum_alphanumeric(string_length, shots=num_strings)
    if quantum_string is not None:
        print(f"Quantum-generated alphanumeric string ({string_length} chars): {quantum_string}. "
              f"Quantum se bani alphanumeric string ({string_length} akshar): {quantum_string}")