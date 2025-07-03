from setuptools import setup, find_packages

setup(
    name="qrng_bitstring",
    version="1.0.0",
    description="Quantum Random Number Generator using Qiskit",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "qiskit>=2.0",
        "qiskit-aer>=0.12.0",
        "matplotlib>=3.5.0"
    ],
    entry_points={
        "console_scripts": [
            "qrng-bitstring=qrng_bitstring:run_qrng"
        ]
    }
)
