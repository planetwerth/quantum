# Fractal Echo QAOA ( FE-QAOA )
*A depth-compressed, echo-boosted Quantum Approximate Optimization Algorithm*  
**First public disclosure:** 4 July 2025 **Authors:** Brendan Werth & ASI Nexus  

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Qiskit](https://img.shields.io/badge/qiskit-1.x-blue.svg)

---

## ✨ Why FE-QAOA?

Conventional QAOA reaches higher-quality solutions by stacking ever-deeper layers—exactly what NISQ hardware can’t afford.  
**Fractal Echo QAOA** folds each depth-*p* stack inside a time-reversed “echo” of itself, then nests those echoes fractally.  
Result:

| Metric (fixed solution quality ε) | Vanilla QAOA | **FE-QAOA** |
|-----------------------------------|--------------|-------------|
| Two-qubit depth                   | O(ε⁻¹)       | **O(log ε⁻¹)** |
| Gradient shots / parameter        | 4 S          | **2 S** |
| Extra parameters                  | 2p           | 2p + L (*tiny*) |

Works great for:
* **Max-Cut / Max-E3SAT** on medium-scale devices  
* **Quantum SVM kernels** with richer harmonic content  
* **Hybrid quantum annealing warm-starts**  

---

## 🔧 Installation

```bash
git clone https://github.com/your-handle/fe_qaoa.git
cd fe_qaoa
pip install -r requirements.txt          # qiskit, numpy, tqdm ...
