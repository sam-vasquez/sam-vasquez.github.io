---
tags:
  - Quantum-Information
collection: notes
title: "Projection Operator Dynamics"
permalink: /note/Projection-Operator-Dynamics/
---
When studying the dynamics of open quantum systems, the time evolution equation cannot always be described by a [[Markovian Quantum Processes|Markov process]]. 

Projection operator methods provide a framework for non-Markovian processes.

They essentially regard the operation of tracing over the environment as a formal projection on the density matrix in the state space of the total system, $\rho \rightarrow \mathcal{P}\rho$. 

Consider a Hamiltonian of the form
$$
H = H_0 + \alpha V,
$$
$H_0$ the uncoupled time evolution of system $A$ and environment $B$, $V$ their interaction, $\alpha$ an expansion parameter.
In the [[Time Evolution Representations|interaction picture]], their total density matrix evolves as 
$$
i \partial_t \rho_I(t) = \alpha \left[ V_I(t), \rho_I(t) \right] \equiv i \alpha \mathcal{L}(t) \rho_I(t).
$$
(From here on, labels $I$ will be suppressed, implicitly continuing to work with the interaction picture representation of all operators.)

It is customary to introduce a formal operator $\mathcal{P}$ such that $\mathcal{P} \rho = \textrm{Tr}_B(\rho) \otimes \rho_B = \rho_A \otimes \rho_B$. This projection operator traces over the bath's degrees of freedom to yield the reduced density matrix of subsystem $A$, meanwhile assuming that the bath remains in its state $\rho_B$. And it is a projection operator, it can be shown that $\mathcal{P}^2 = \mathcal{P}$.

$\rho_B$ is chosen according to the specific application being studied. To ensure that $\mathcal{P}$ is idempotent, it is assumed that $\rho_B$ is normalized, $\textrm{Tr}_B\rho_B = 1$. It is typically chosen to be the [[Canonical Ensemble]] of the environment, unless there is a better way to model the environment. And it is typically assumed to be time independent.

It is also often assumed that odd moments of the interaction Hamiltonian with respect to $\rho_B$ vanish,
$$
\textrm{Tr}_B \{V(t_1) V(t_2) \ldots V(t_{2n+1}) \rho_B\} = 0.
$$
This isn't necessary, but is justified by most interaction energies being symmetric and the bath states being randomly distributed around zero. This implies that
$$
\mathcal{P} \mathcal{L}(t_1) \mathcal{L}(t_2) \ldots \mathcal{L}(t_{2n+1}) \mathcal{P} = 0.
$$
To see why, consider the single product case.
$$
\mathcal{P} \mathcal{L}(t_1)\mathcal{P} \rho(t) = \textrm{Tr}_B\left( \left[ V(t_1), \textrm{Tr}_B(\rho(t)) \otimes \rho_B \right] \right) \otimes \rho_B = 0.
$$
The outer partial trace clearly involves an odd number of products of $V$ and $\rho_B$ for all odd numbers of commutators, and therefore it vanishes together with the entire tensor product. This assumption will be useful for perturbation expansions.

There are two conventional methods for deriving the equation of motion for $\mathcal{P} \rho(t)$. The [[Nakajima-Zwanzig Equation]], and the [[Time-Convolutionless Projection Operator Method]].

Reference:
[[(2007) The Theory of Open Quantum Systems]] Sec 9.1