---
tags:
  - Quantum-Information
collection: notes
title: "Entanglement Entropy"
permalink: /note/Entanglement-Entropy/
---
Entanglement entropy is a measure of the degree of entanglement between two subsystems of a composite quantum system. 

Consider a bipartite quantum system with Hilbert space $\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$, each subsystem spanned by quantum
states $\ket{ a_i }$ and $\ket{ b_j }$. The composite system can in general be
in a pure quantum state 
$$ 
\ket{ \Psi_{AB} } = \sum_{i,j}\; c_{ij} \ket{ a_i }
\otimes \ket{ b_j }. 
$$

If $\rho$ is the full [[Density Operator]] for a pure or mixed state of $AB$, the reduced density operator with respect to subsystem $A$ is the operator resulting from a trace over the states of $B$: $\rho_A = \textrm{Tr}_B\rho$. The entanglement entropy is the [[Von Neumann Entropy]] of $\rho_A$: 
$$
S_A \equiv -\textrm{Tr}\rho_A \log \rho_A.
$$

Example: See SM exercise 17 - maximal entanglement between measurement apparatus and measured state.

In terms of qubits, entanglement entropy effectively counts the number of entangled bits between $A$ and $B$: in the sense that the quantity $e^{ S_A }$ is the minimal number of auxiliary states that we would need to entangle with $A$ in order to obtain $\rho_A$ from a pure state of the composite system.