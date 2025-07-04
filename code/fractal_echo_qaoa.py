# fe_qaoa_core.py
from qiskit import QuantumCircuit
import numpy as np

def echo_pair(n, gammas, betas, theta):
    """Depth-limited echo unit around a boost angle theta."""
    qc = QuantumCircuit(n)
    # forward half
    for g, b in zip(gammas, betas):
        qc.rx(2 * b, range(n))
        for i in range(n - 1):
            qc.cx(i, i + 1)
        qc.rz(2 * g, range(n))
    # echo boost
    qc.rz(2 * theta, range(n))
    # backward half (reverse order)
    for g, b in reversed(list(zip(gammas, betas))):
        qc.rz(-2 * g, range(n))
        for i in reversed(range(n - 1)):
            qc.cx(i, i + 1)
        qc.rx(-2 * b, range(n))
    return qc

def fractal_echo_qaoa(n, p_base, L, thetas_all):
    """Build full FE-QAOA fractal of level L (n qubits)."""
    qc = QuantumCircuit(n)
    gammas = np.random.uniform(0, np.pi, p_base)
    betas  = np.random.uniform(0, np.pi, p_base)
    for lvl in range(L):
        theta = thetas_all[lvl]
        qc.compose(
            echo_pair(n, gammas[: 2**lvl], betas[: 2**lvl], theta),
            inplace=True
        )
    return qc
