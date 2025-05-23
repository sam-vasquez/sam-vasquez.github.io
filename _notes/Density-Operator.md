---
tags:
  - Quantum
collection: notes
title: "Density Operator"
permalink: /note/Density-Operator/
---
Quantum mechanical states assume complete knowledge over the entire physical system described by those states, they describe so-called *pure states*. But that's rare. The density operator compensates for this by formalizing the concept of statistical ensembles of multiple interacting quantum systems to describe **mixed states**.

For an ensemble of systems each described by the same quantum system $A$, with classical probability $p_n$ of being in the pure state $\ket{ \psi_n }$, its density operator is
$$
\rho = \sum_n p_n \ket{ \psi_n } \bra{ \psi_n }.
$$
Measurement of an observable in this ensemble is given by an average of expectation values over all pure states, 
$$
\begin{align}
\langle \mathcal{O} \rangle &= \sum_n p_n \bra{ \psi_n } \mathcal{O} \ket{ \psi_n } \\
&= \sum_n p_n \textrm{Tr}(\bra{ \psi_n }\mathcal{O}\ket{ \psi_n }) \\
&= \sum_n p_n \textrm{Tr}(\ket{ \psi_n }\bra{ \psi_n }\mathcal{O}) \\
&= \textrm{Tr}\left( \sum_n p_n \ket{ \psi_n }\bra{ \psi_n }\mathcal{O} \right) \\
&= \textrm{Tr} (\rho \mathcal{O}).
\end{align}
$$
(Divide by $\textrm{Tr} \rho$ if the density operator wasn't normalized.)

The [[Canonical Ensemble]] for quantum systems assigns the probability $e^{-\beta E}$ to each pure state describing the ensemble at a given temperature $\beta$. That is to say, the canonical ensemble has density operator
$$
\rho =\frac{1}{Z} \sum_i e^{-\beta E_i} \ket{ \psi_i } \bra{ \psi_i },
$$
where $\ket{ \psi_i }$ are specifically the energy eigenstates. 
See problem 16 of stat mech hw for an example of thermodynamics of particles with their spins coupled to a magnetic field.

The density operator can be applied to 


In deriving the perturbative expansion for the time-convolutionless projection operator, it is assumed that odd moments of the interaction Hamiltonian with respect to the reference state vanish: that \mathcal{P} \mathcal{L}(t_1) \mathcal{L}(t_2) \ldots \mathcal{L}(t_{2n+1}) \mathcal{P} = 0. Where \mathcal{L}(t) \rho(t) = -i [V_I(t), \rho(t)], V_I(t) is the interaction picture representation of the interaction Hamiltonian in H = H_0 + \alpha V, \mathcal{P} is a projection of the density matrix onto the desired subsystem, \mathcal{P} \rho = \textrm{Tr}_B(\rho) \otimes \rho_B for some bath states \rho_B. For one example, \mathcal{P} \mathcal{L}(t_1) \mathcal{P} \rho(t) = -i \mathcal{P} [V_I(t_1), \mathcal{P} \rho(t)] = i \mathcal{P} V_I(t_1) \mathcal{Q} \rho(t). Where \mathcal{Q} = 1 - \mathcal{P} is the rejection of the projection operator. So I can imagine that the spirit of this assumption that "odd moments of the interaction Hamiltonian with respect to the reference state vanish" is that