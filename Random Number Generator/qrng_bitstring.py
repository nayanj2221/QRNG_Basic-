"""
Quantum Random Number Generator (QRNG) for generating random bitstrings using Qiskit 2.x.
Quantum se random bitstrings banata hai (jaise 10110011).

Language: Python 3.6+
Dependencies:
- Qiskit 2.0+: `pip install qiskit>=2.0`
- Qiskit-Aer: `pip install qiskit-aer>=0.12.0`
- Matplotlib: `pip install matplotlib>=3.5.0`
Parameters:
- num_bits: Number of bits in the bitstring (e.g., 8 for '10110011').
- show_graph: Boolean to display histogram of bitstring distribution (default: False).
Usage:
- Set `num_bits` (e.g., 8) and `show_graph` (True/False).
- Run: `python qrng_bitstring.py`
Features:
- Generates random bitstrings using Hadamard gates and Qiskit Aer Sampler.
- Fixed graph display issue with explicit plt.show().
- Bilingual Hindi-English comments and output for accessibility.
"""
%matplotlib inline
from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_qrng_circuit(num_qubits: int) -> QuantumCircuit:
    """
    Create a quantum circuit with Hadamard gates for random bitstring generation.
    Hadamard gates ke saath quantum circuit banata hai random bitstring ke liye.
    
    Args:
        num_qubits (int): Number of qubits (bits) in the circuit.
        Qubits ki sankhya (bits) circuit mein.
    
    Returns:
        QuantumCircuit: Circuit with Hadamard gates and measurements.
        Quantum circuit jo Hadamard gates aur measurements ke saath hai.
    """
    qc = QuantumCircuit(num_qubits)
    qc.h(range(num_qubits))  # Put qubits into superposition
    qc.measure_all()  # Measure all qubits
    return qc

def get_random_bitstring(qc: QuantumCircuit) -> str:
    """
    Generate a random bitstring from the quantum circuit.
    Quantum circuit se random bitstring banata hai.
    
    Args:
        qc (QuantumCircuit): Quantum circuit to sample from.
        Quantum circuit jisse sample karna hai.
    
    Returns:
        str: Random bitstring (e.g., '10110011').
        Random bitstring (jaise '10110011').
    """
    try:
        sampler = Sampler()
        result = sampler.run(qc, shots=1).result()
        counts = result.quasi_dists[0]
        bitstring = max(counts, key=counts.get)  # Most probable bitstring
        return bitstring
    except Exception as e:
        print(f"Error: {str(e)}")
        return ""

def visualize_distribution(qc: QuantumCircuit, shots: int = 1024) -> None:
    """
    Visualize the probability distribution of bitstrings.
    Bitstrings ki probability distribution visualize karta hai.
    
    Args:
        qc (QuantumCircuit): Quantum circuit to sample from.
        Quantum circuit jisse sample karna hai.
        shots (int): Number of samples for distribution (default: 1024).
        Samples ki sankhya distribution ke liye (default: 1024).
    """
    try:
        sampler = Sampler()
        result = sampler.run(qc, shots=shots).result()
        counts = result.quasi_dists[0]
        if counts:
            plot_histogram(counts)
            plt.title("Quantum Random Bit Distribution / Quantum Bit Vitaran")
            plt.xlabel("Bitstrings / Bitstrings")
            plt.ylabel("Probability / Sambhavna")
            plt.show()  # Explicitly show the plot
        else:
            print("No data to visualize. Visualization skipped. / Koi data nahi hai, visualization skip hui.")
    except Exception as e:
        print(f"Error in visualization: {str(e)}")

def run_qrng(num_bits: int = 8, show_graph: bool = False):
    """
    Main function to run the QRNG and generate a random bitstring.
    QRNG chalaane ka mukhya function random bitstring ke liye.
    
    Args:
        num_bits (int): Number of bits in the bitstring (default: 8).
        Bitstring mein bits ki sankhya (default: 8).
        show_graph (bool): Whether to show the probability distribution (default: False).
        Probability distribution dikhana hai ya nahi (default: False).
    """
    try:
        if not isinstance(num_bits, int) or num_bits <= 0:
            raise ValueError("Number of bits must be a positive integer. Bits ki sankhya positive integer honi chahiye.")
        
        qc = create_qrng_circuit(num_bits)
        random_bits = get_random_bitstring(qc)
        if random_bits:
            print(f"🎲 Quantum Generated {num_bits}-bit Random Number: {random_bits}. "
                  f"Quantum se bana {num_bits}-bit random number: {random_bits}")
        
        if show_graph:
            visualize_distribution(qc)
    
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage / Uddharan
if __name__ == "__main__":
    run_qrng(num_bits=8, show_graph=True)