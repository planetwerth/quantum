from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.circuit import Parameter
import numpy as np

def folded_ansatz(n, depth=2):
    """Hardware-efficient spectral-folding ansatz."""
    qc = QuantumCircuit(2*n)
    thetas = [Parameter(f"θ_{i}") for i in range(depth*2*n)]
    idx = 0
    for d in range(depth):
        # RY layer on system + mirror
        for q in range(2*n):
            qc.ry(thetas[idx], q); idx += 1
        # Entangle system↔mirror pairs
        for q in range(n):
            qc.cx(q, 2*n-1-q)
        # Swap halves to implement mirror J
        for q in range(n//2):
            qc.swap(q, n-1-q)
    return qc, thetas

def cost(theta_vals, h_terms, mirror=False, shots=2048):
    """Evaluate \<ψ|H_f|ψ\> (or mirror cost) on Aer simulator."""
    qc, params = folded_ansatz(n_qubits)
    qc_bound = qc.bind_parameters(dict(zip(params, theta_vals)))
    # append H-term Pauli strings as measurements
    # (toy demo: assume H = sum Z_i)
    backend = Aer.get_backend('qasm_simulator')
    tqc = transpile(qc_bound, backend)
    job = execute(tqc, backend, shots=shots)
    counts = job.result().get_counts()
    exp = 0.0
    for bitstr, c in counts.items():
        zvals = [(1 if bit == '0' else -1) for bit in bitstr[::-1][:n_qubits]]
        term = sum(zvals)
        if mirror:
            term *= -1  # simplistic mirror flip for demo
        exp += term * c / shots
    return exp

# --- hyper-demo ---
n_qubits = 4
theta0 = 2*np.pi*np.random.rand(4*2*n_qubits)
print("Initial cost:", cost(theta0, None))
