# Q_Entanglement_Basic
This repository shows the basic Quantum Entanglement Circuit built using the qiskit* library provided by IBM.

This shows the basic implementation of the circuit where first three qubits are taken and Quantum gates are applied to them as per the rquirements.
X Gate = Applied to only a single Qubit. Representation of Pauli-X Gate is a simple Bit-Flip.
H Gate = Hadamard Gate, applied on a single qubit and changes |0> to |+> and |1> to |-> and vice versa.
CX Gate = Controlled-X Gate for a binary qubit operation. It is somewhat similar to the classical XOR Gate.
Barriers are applied to separate one section of the circuit from the other.
Next the cicuit is measured which can be seen in the cicuital representation. Measuring quantum circuits is not the sam as the classical ones due to the presence of something known as "Noise" which requires the former to be executed multiple times for the correct outcome to be measured via the probability of the outcome having more of it.
Here the "counts" variable dictates the number of times the circuit must execute and provide the output for the same.
This concludes the basics of the code and its implementation.

*Note that this is compatible with the qiskit version '0.44.0' and not the latest one.
