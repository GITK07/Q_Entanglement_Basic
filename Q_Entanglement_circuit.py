circuit=QuantumCircuit(3,3)
circuit.x(0)
circuit.barrier()
circuit.h(1)
circuit.cx(1,2)
circuit.cx(0,1)
circuit.h(0)
%matplotlib inline
circuit.draw()

circuit.barrier()
circuit.measure([0,1],[0,1])
circuit.draw()

circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)
circuit.draw()

circuit.measure(2,2)
backend=Aer.get_backend('qasm_simulator')
result=execute(circuit, backend=backend, shots=1024).result()
counts=result.get_counts()
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)
