---
tags:
  - Quantum
  - Stat-Mech
collection: notes
title: "Heisenberg XXX Spin Chain"
permalink: /note/Heisenberg-XXX-Spin-Chain/
---
The Heisenber $XXX$ spin chain is a [[Quantum Heisenberg Model]] of quantum spins in a 1 dimensional chain, usually studied with periodic boundary conditions, with Hamiltonian
$$
\mathcal{H} = -J \sum_{i=1}^N (X_iX_{i+1} + Y_iY_{i+1} + Z_iZ_{i+1} + h X_i)
$$
$$
= -\frac{J}{2} \sum_{i=1}^N (S^+_i S^-_{i+1} + S^-_i S^+_{i+1} + 2 Z_i Z_{i+1} + 2 h X_i).
$$
In the absense of the external field, the Hamiltonian commutes with total spin, and so it is invariant under $SU(2)$ rotations, and in the thermodynamic limit is the $O(3)$ non-linear sigma model. In particular, it commutes with the z-component of total spin, and therefore conserves total number of spins down (up).

The zero-field Hamiltonian can be diagonalized by diagonalizing its restriction to invariant subspaces of the Hamiltonian, the subspaces $V_M$ containing states with $M$ spins down. Assuming a ferromagnetic coupling, the diagonalization proceeds as follows:

In the case $M=0$, the ground state is simply $\ket{ 0 } \equiv \ket{ \uparrow \uparrow \ldots \uparrow }$, with energy $-\frac{NJ}{4}$.

In the case $M=1$, the $N$-dimensional subspace is spanned by kets consisting of a single spin down and $N-1$ spins up. These basis vectors are $\ket{ j } = S^-_j \ket{ 0 } = \ket{ \uparrow \ldots \uparrow \downarrow \uparrow \ldots \uparrow }$. 
By translational invariance, the subspace should have energy eigenstates that are simultaneously eigenstates of left- and right-translation operators. On this space, the left- and right-translation operators are $\sum_i S_i^- S_{i+1}^+$ and $\sum_i S_i^+ S_{i+1}^-$ respectively. Their eigenstates are of the form
$$
\ket{ \psi_k } = \frac{1}{\sqrt{ N }} \sum_j e^{ i k j } \ket{ j },
$$
where $k \in \frac{2\pi}{N} \mathbb{Z}/N\mathbb{Z}$ is a conserved momentum. Their eigenvalues are $e^{ ik }$ and $e^{ -ik }$, respectively.

The first term in the Hamiltonian is a right-translation operator, and the second term is a left-translation operator. The third term contributes $-\frac{\hbar^2}{4}$ for each of the two pairs of misaligned neighbors, and $+\frac{\hbar^2}{4}$ for the others, giving $\sum_i 2Z_iZ_j \ket{ \psi_k } = \frac{N-4}{2} \ket{ \psi_k }$.
$$
\mathcal{H} \ket{ j } = -\frac{J}{2} \left(  \ket{ j+1 } + \ket{ j-1 } + \frac{N-4}{2} \ket{ j } \right)
$$
$$
\begin{align}
\mathcal{H} \ket{ \psi_k } &= -\frac{J}{2} \left( e^{ -ik } + e^{ ik } + \frac{N-4}{2} \right) \ket{ \psi_k }  \\
E_k &= J(1 - \cos k) + E_0.
\end{align} 
$$
This is the magnon dispersion relation, the momentum-space dispersion relation for the energy of a quantized spin wave on this chain.

In the case $M \geq 2$, the basis states are $\ket{ n_1,\ldots,n_M } = S^-_{n_1}\ldots S^-_{n_M} \ket{ 0 }$. 
In $M=2$, the Hamiltonian acts on the asis states depending on whether the two spins are independent or adjacent. 
If adjacent, $\sum S^+ S^- \ket{i, i+1} = \ket{ i, i+2 }$,$\sum S^- S^+ \ket{i, i+1} = \ket{ i-1, i+1 }$, and $\sum 2ZZ \ket{ i, i+1 } = \frac{N-4}{2} \ket{ i,i+1 }$.
$$
\mathcal{H} \ket{ i,i+1 } = 
$$
$$
\mathcal{H} \ket{ i, i+1 } = -\frac{J}{2} \left(  \ket{ i, i+2 } + \ket{ i-1, i+1 } + \frac{N-8}{2} \ket{ i, i+1 } \right)
$$
If not adjacent, $\sum S^+ S^- \ket{i, j} = \ket{ i+1, j+1 }$, $\sum S^- S^+ \ket{i, j} = \ket{ i-1, j-1 }$, and $\sum 2ZZ \ket{ i, i+1 } = \frac{N-8}{2} \ket{ i,i+1 }$.
$$
\mathcal{H} \ket{ i, j } = -\frac{J}{2} \left(  \ket{ i+1, j+1 } + \ket{ i-1, j-1 } + \frac{N-8}{2} \ket{ i, i+1 } \right)
$$

The coordinate Bethe ansatz can be used to derive dispersion relations with the form
$$
E_k - E_0 = J \sum_{i=1}^M (1 - \cos k_i).
$$
It might seem as though this is the sum of individual magnon energies, which violates our intuition that they should have interaction energies. But the values of momenta $k_i$ are not necessarily the same as their free values - in general, they are offset by a phase $\theta$ when scattering off of each other. See 
http://andreghenriques.com/Seminars/SpinChainsTalk1.pdf
for a derivation.
See also https://edu.itp.phys.ethz.ch/fs13/int/SpinChains.pdf