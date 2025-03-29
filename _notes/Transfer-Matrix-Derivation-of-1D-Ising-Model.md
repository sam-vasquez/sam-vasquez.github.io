---
tags:
  - Stat-Mech
collection: notes
title: "Transfer Matrix Derivation of 1D Ising Model"
permalink: /note/Transfer-Matrix-Derivation-of-1D-Ising-Model/
---
The [[Exact Solutions of 1D Ising Model|1D Ising model]] can be solved analytically using transfer matrix methods.

Consider the partition function of Ising model with periodic boundary conditions,
$$
\mathcal{H} = -J \sum s_i s_{i+1} - H \mu \sum s_i.
$$

Note that there are four contributions possible per pair of spins $s_i$ and $s_{i+1}$. If both are up, they contribute $e^{ k+h }$ to the partition function. If mixed, $e^{ -k }$. If both down, $e^{ k-h }$. This yields the transfer matrix:
$$
P = \begin{pmatrix} 
e^{ k+h } & e^{ -k } \\
e^{ -k } & e^{ k - h }
\end{pmatrix},
$$
with elements $\bra{ s_i } P \ket{ s_j }$ for each pair of spins in the partition function exponential.
The partition function is rewritten as
$$
Z = \sum_{s_1} \ldots \sum_{s_N} \bra{ s_1 } P \ket{ s_2 } \bra{ s_2 } P \ket{ s_3 } \ldots \bra{ s_N } P \ket{ s_1 }.
$$
All sums aside from $s_1$ can be taken over each resolution of identity to remove each of those sums. 
$$
Z = \sum_{s_1} \bra{ s_1 } P \sum_{s_2} \ket{ s_2 } \bra{ s_2 }\ldots P \ket{ s_1 } = \sum_{s_1} \bra{ s_1 } P^N \ket{ s_1 } = Tr(P^N).
$$
$P$ is real and symmetric, so it can be diagonalized by an orthogonal matrix. The resulting diagonal matrix trivializes the calculation:
$$
Z = \textrm{Tr } D^N = \lambda_+^N + \lambda_-^N.
$$
The eigenvalues of $P$ are $\lambda = e^k \cosh(h) \pm \sqrt{ e^{-2k} + e^{2k} \sinh^2(h) }$.
In the thermodynamic limit, the smaller eigenvalue contributes negligibly, and 
$$
\frac{1}{N} \ln Z \approx \ln \lambda_+.
$$
Pulling out the factor of $e^k$ from $\lambda$, the free energy is
$$
f \equiv \lim_{N\rightarrow\infty} \beta \frac{F}{N} = - \ln \lambda_+ = -J - k_B T \ln \left[  \cosh(h) + \sqrt{ e^{-4k} + \sinh^2(h) } \right].
$$