---
collection: notes
title: "Collapse-to-a-Block Corrected Ehrenfest Dynamics"
permalink: /note/Collapse-to-a-Block-Corrected-Ehrenfest-Dynamics/
---
[[Non-Adiabatic Molecular Dynamics]] method.
Extension of [[Ehrenfest Molecular Dynamics]] to support decoherence.

Traditional approach:
Assume that pairwise electron coherences decay as a Gaussian with rate
$$
\tau_{ij}^{-2} = \sum_\eta \frac{(F_{i,\eta} - F_{j,\eta})^2}{8\hbar^2\alpha_\eta},
$$
$\eta$ indexes vibrational degrees of freedom, $F_{i,\eta}$ is the force on state $i$, and $\alpha_\eta$ represents the width of a Gaussian vibrational wave packet. This is derived by [[(1996) Quantum decoherence and the isotope effect in condensed phase nonadiabatic molecular dynamics simulations]]. This has been used for nonadiabatic simulations such as 20,21,33-38. TAB introduces an independent decoherence time for each state pair for greater accuracy in systems in more than two states.

At the end of each nuclear time step $t + \Delta t$, build the fully coherent electronic density matrix $\rho^c(t + \Delta t) = \ket{ \psi(t) }\bra{ \psi(t) }$ in the basis of adiabatic electronic states. Form a target density matrix $\rho^d(t+\Delta t)$ with off-diagonal elements scaled by $0 \leq \omega_{ij} \leq 1$ such that $\rho_{ij}^d = \omega_{ij}(\tau_{ij},\dot{\rho}_{ii},\dot{\rho}_{jj})\rho_{ij}^c(t + \Delta t)$. This is derived in full definition in [[(2020) Decoherence-corrected Ehrenfest molecular dynamics on many electronic states]]. The diagonal elements are not scaled.
Having $\rho^d(t + \Delta t)$, decompose it into density matrices representing pure superpositions of subsets of the adiabatic states: $\rho^d = \sum_a P_a^{block}\rho_a^{block}$. [[(2020) Decoherence-corrected Ehrenfest molecular dynamics on many electronic states]] describes the algorithms used to determine these blocks. 
Stochastically decide whether the wavefunction will collapse into one of these block states. 


References: Introduced in [[(2020) State-pairwise decoherence times for nonadiabatic dynamics on more than two electronic states]]. Extended by [[(2020) Decoherence-corrected Ehrenfest molecular dynamics on many electronic states]]. Applied in [[(2025) Long-Lived Electronic Coherences from First Principles]].

See also [[(2020) State-pairwise decoherence times for nonadiabatic dynamics on more than two electronic states]], and ref 23 in [[(2025) Long-Lived Electronic Coherences from First Principles]]. 