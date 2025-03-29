---
tags:
  - Reference
  - Quantum-Information
collection: notes
title: "Bell State Measurement"
permalink: /note/Bell-State-Measurement/
---
Measurement of two qubits in a Bell state basis can be implemented through the unitary operator $U_B = (H \otimes I)(CNOT_{12})$ followed by measurement in the computational basis. This operator has the action
$$
\begin{align*}
    \ket{\Phi^+} = \ket{00} +
    \ket{11} 
    &\xmapsto{U_B} \ket{00}\\
    \ket{\Phi^-} = \ket{00} -
    \ket{11}
    &\xmapsto{U_B} \ket{10}\\
    \ket{\Psi_+} = \ket{01} +
    \ket{10}
    &\xmapsto{U_B} \ket{01}\\
    \ket{\Psi_-} = \ket{01} -
    \ket{10}
    &\xmapsto{U_B} \ket{11}. 
\end{align*}
$$
See quantum information exercise 8. 