---
tags:
  - Stat-Mech
  - Quantum
collection: notes
title: "Quantum Heisenberg Model"
permalink: /note/Quantum-Heisenberg-Model/
---
A modification of the [[Heisenberg Model]] ($O(3)$ model) that replaces each classical spin with quantum operators:
$$
\mathcal{H} = \sum_{\langle ij \rangle} (J_x X_i X_j + J_y Y_i Y_j + J_z Z_i Z_j) + \sum_i H X_i,
$$
where $H$ represents the coupling for an external transverse magnetic field.

The model is usually named after the relative values of $J_x$, $J_y$, and $J_z$. The most studied models are the 1D [[Heisenberg XXZ Spin Chain]] ($J = J_x = J_y$, $\Delta = J_z/J \neq 1$) and the 1D [[Heisenberg XXX Spin Chain]] ($\Delta = 1$). These two models can be written with Hamiltonian
$$
\mathcal{H} = -J\sum_{i=1}^N (X_iX_{i+1} + Y_iY_{i+1} + \Delta Z_iZ_{i+1} + h X_i).
$$
The first two terms swap anti-aligned spins, and can be rewritten as 
$$
\mathcal{H} = - \frac{J}{2} \sum_{i=1}^N (S^+_i S^-_{i+1} + S^-_i S^+_{i+1} + 2 \Delta Z_i Z_{i+1} - 2h X_i).
$$
The $ZZ$ term is just the Ising-model, measuring $+1$ if aligned and $-1$ if antialigned.
In this $XXX$-$XXZ$ model, the parameter $\Delta$ is an  anisotropy parameter.