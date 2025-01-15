# **Quantum Teleportation Circuit**

Introduction

This repository contains a learning code for simulating quantum teleportation using Qiskit, an open-source quantum computing framework. Quantum teleportation is a fundamental protocol in quantum information theory that allows the transfer of quantum states from one qubit to another, using entanglement and classical communication.

Prerequisites

To run the code, you'll need the following:
- Python 3.7+
- Qiskit 0.23.0+ (or the latest version)

Installation

You can install Qiskit using pip if you don't have it installed already:

```bash
pip install qiskit
```

For running the code in a Jupyter notebook, you may also need to install Jupyter:

```bash
pip install jupyter
```

Contents

The repository includes the following files:
- `quantum_teleportation.py`: Main script for simulating the quantum teleportation circuit.
- `teleportation.ipynb`: Jupyter notebook containing the same code with added explanations and visualizations.
- `README.md`: This file.

Quantum Teleportation Circuit

The quantum teleportation protocol involves three qubits:
1. Alice's Qubit (qubit 0): The qubit whose state we want to teleport.
2. Entangled Qubit 1 (qubit 1): Part of the entangled pair used for teleportation.
3. Entangled Qubit 2 (qubit 2): The other part of the entangled pair, initially with Bob.

Steps of the Protocol

1. Preparation:
   - Prepare qubit 0 in the state to be teleported.
   - Create an entangled pair of qubits (qubits 1 and 2).

2. Bell Measurement:
   - Apply a CNOT gate and a Hadamard gate on qubits 0 and 1.
   - Measure qubits 0 and 1, sending the classical results to Bob.

3. Classical Communication:
   - Based on the measurement results, Alice sends two classical bits to Bob.
   - Bob applies the corresponding Pauli gates on qubit 2 to recover the teleported state.

Running the Code

Using the Python Script

You can run the main script directly using Python:

```bash
python quantum_teleportation.py
```

Using the Jupyter Notebook

You can explore the quantum teleportation protocol interactively using the Jupyter notebook:

```bash
jupyter notebook teleportation.ipynb
```

Visualization

The code visualizes the quantum circuit and the measurement results using Qiskit's built-in tools. The final outcome is displayed in a histogram showing the probabilities of different measurement results.

Conclusion

This code provides a hands-on learning experience for understanding quantum teleportation, a key concept in quantum computing.

Feel free to experiment with the code and explore the fascinating world of quantum mechanics!

## Resources

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Quantum Teleportation Protocol](https://qiskit.org/textbook/ch-algorithms/teleportation.html)
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)

---
