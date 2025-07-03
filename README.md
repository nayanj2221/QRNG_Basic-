# Quantum Random Number Generator Suite

A collection of Python scripts for generating quantum-random numbers and alphanumeric strings using Qiskit.  
Leverage quantum superposition to produce high-entropy, unpredictable values for cryptography, testing, and research.

## 📦 Contents

This repository includes three main scripts:

| File Name                     | Description                                                     |
|--------------------------------|-----------------------------------------------------------------|
| **qrng_alphanumeric_alternate .py** | Generates alternating digit-letter strings (e.g., `12ej45`).   |
| **qrng_alphanumeric_pattern.py**      | Generates custom-pattern strings with parallel sampling and entropy (e.g., `DDL` -> `12e`). |
| **qrng_bitstring.py**                 | Generates random bitstrings (e.g., `10110011`) with optional histogram visualization. |

## 🚀 Features

- **Quantum Randomness:** All scripts use quantum circuits for true randomness.
- **Alphanumeric Generation:** Produce alternating or custom-pattern strings.
- **Bitstring Generation:** Create random bit sequences for low-level applications.
- **Custom Patterns:** Define patterns like `DDL` (digit-digit-letter) in `qrng_alphanumeric_pattern.py`.
- **Entropy Calculation:** Assess randomness with Shannon entropy (in `qrng_alphanumeric_pattern.py`).
- **Parallel Sampling:** Boost performance in `qrng_alphanumeric_pattern.py`.
- **Visualization:** Display bitstring distribution histograms in `qrng_bitstring.py`.
- **Memory Efficiency:** Uses 4–5 qubits per character or adjustable bits.

## 🧑‍💻 Requirements

- Python 3.6+
- [Qiskit](https://qiskit.org/) >= 2.0
- Qiskit-Aer >= 0.12.0 (for `qrng_bitstring.py`)
- NumPy
- Matplotlib >= 3.5.0 (for `qrng_bitstring.py` visualization)

Install dependencies:

```bash
pip install qiskit>=2.0 qiskit-aer>=0.12.0 numpy matplotlib>=3.5.0


```

## 🗂️ Usage

### 1. **Quantum Alphanumeric Alternate Generator**

**File:** `qrng_alphanumeric_alternate.py`

- **Purpose:** Generates strings with alternating digits and lowercase letters (e.g., `12ej45`).
- **How to run:**

  ```bash
  python qrng_alphanumeric_alternate.py
  ```

- **Sample output:**
  ```
  Quantum-generated alphanumeric string (6 chars): 12ej45. Quantum se bani alphanumeric string (6 akshar): 12ej45
  ```
- **Configuration:**
  - `length` (int): Even number for string length (default: 6).
  - `shots` (int): Number of strings (default: 1).

### 2. **Quantum Alphanumeric Pattern Generator**

**File:** `qrng_alphanumeric_pattern.py`

- **Purpose:** Generates custom-pattern strings with parallel sampling and entropy (e.g., `DDL` -> `12e`).
- **How to run:**

  ```bash
  python qrng_alphanumeric_pattern.py
  ```

- **Sample output:**
  ```
  Generated 10 quantum alphanumeric strings for pattern 'DDL':
  1. 12e
  2. 78m
  ...
  Entropy of generated strings: 3.45 bits.
  ```
- **Configuration:**
  - `pattern` (str): String of 'D' (digit) or 'L' (letter), e.g., 'DDL'.
  - `shots` (int): Number of strings (default: 10).
  - `parallel` (bool): Enable parallel sampling (default: True).

### 3. **Quantum Bitstring Generator**

**File:** `qrng_bitstring.py`

- **Purpose:** Generates random bitstrings (e.g., `10110011`) with optional histogram visualization.
- **How to run:**

  ```bash
  python qrng_bitstring.py
  ```

- **Sample output:**
  ```
  🎲 Quantum Generated 8-bit Random Number: 10110011. Quantum se bana 8-bit random number: 10110011
  [Histogram displayed if show_graph=True]
  ```
- **Configuration:**
  - `num_bits` (int): Number of bits in the bitstring (default: 8).
  - `show_graph` (bool): Display histogram of bit distribution (default: True).

## ⚙️ Configuration

Customize each script by editing the parameters in the `if __name__ == "__main__":` section:
- **Length/Characters:** Adjust `length` or `pattern` to change output size.
- **Number of Outputs:** Modify `shots` for multiple strings.
- **Parallel Mode:** Set `parallel=True` in `qrng_alphanumeric_pattern.py` for performance.
- **Visualization:** Set `show_graph=True` in `qrng_bitstring.py` to see bit distribution.

## 📊 Entropy

The `qrng_alphanumeric_pattern.py` script calculates Shannon entropy to measure randomness. Higher entropy indicates better unpredictability, ideal for cryptographic use.

## 📄 License

This project is licensed under the MIT License.  
See [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Open an issue or submit a pull request to enhance this suite.

## 💡 Acknowledgments

- Built using [Qiskit](https://qiskit.org/) and Qiskit-Aer.
- Developed with support from xAI’s Grok, inspired by quantum computing advancements.

## 📬 Contact

For questions or suggestions, open an issue or contact [nayan02221@gmail.com].


