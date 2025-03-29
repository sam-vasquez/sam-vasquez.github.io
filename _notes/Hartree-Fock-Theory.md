---
tags:
  - Quantum
collection: notes
title: "Hartree-Fock Theory"
permalink: /note/Hartree-Fock-Theory/
---
Hartree-Fock theory approximates many-electron wavefunctions as a single Slater determinant, and uses that Slater determinant as the ansatz for [[Variational Principle (Quantum Mechanics)|variational energy minimization]]. 

The variational principle applied to Hartree-Fock states can be rewritten in the form 
$$
f(i) \chi(\mathbf{x}_i) = \epsilon \chi(\mathbf{x}_i),
$$
where
$$
f(i) = - \frac{1}{2} \nabla_i^2 - \sum_{A=1}^M \frac{Z_A}{r_{iA}} + v^{HF}(i),
$$
and $v^{HF}(i)$ is the average potential experienced by the $i$th electron due to the presence of the other electrons. Thus, Hartree-Fock is a [[Mean Field Theory]].

This eigenvalue formulation of the Hartree-Fock problem is a nonlinear equation in $\chi(\mathbf{x}_i)$, and is thus solved iteratively. This procedure is called the self-consistent-field (SCF) method.

For a basis set of $K$ spatial functions, and thus $2K$ spin orbitals, the Hartree-Fock solution yields $N$ occupied spin orbitals and $2K - N$ unoccupied "virtual" orbitals.

Expanding the basis set will allow greater flexibility in the variational principle and allow the Hartree-Fock solution to converge more closely to the physical minimum energy, but even this Hartree-Fock limit will not be physical because this is a mean field theory fundamentally inaccurate due to neglected electron correlations.

