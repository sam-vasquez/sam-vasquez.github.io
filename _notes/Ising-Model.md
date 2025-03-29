---
tags:
  - Stat-Mech
collection: notes
title: "Ising Model"
permalink: /note/Ising-Model/
---
The Ising model is the simplest example of an interacting spin model. It models a simple magnetic system as a lattice of classical spins aligned with each other and/or an external magnetic field.

The Ising model has Hamiltonian
$$
\mathcal{H} = - J \sum_{(ij)} s_i s_j - \sum H \mu s_i,
$$
where $J$ is an interaction energy, $(ij)$ denotes a sum over nearest neighbor pairs, $H$ is the external (applied) magnetic field, and $\mu$ is the magnetic moment. When $J > 0$, parallel spins are favored, and this models a ferromagnet. When $J<0$, this models an anti-ferromagnet.

The Hamiltonian has a global $\mathbb{Z}_2$ [[Cyclic Group|symmetry]], which is explicitly broken by the external field. The symmetry is also spontaneously broken as $T \rightarrow T_C$, inducing a spontaneous magnetization:
$$
m(T) = \lim_{H\rightarrow 0} m(T) = \sqrt{ \lim_{|\vec{r}| \rightarrow \infty} \langle \sigma(0) \sigma(\vec{r}) \rangle }
$$

Solutions:
- [[Exact Solutions of 1D Ising Model]]
- [[Exact Solution of 2D Ising Model]]
- [[Curie-Weiss Mean Field Theory]]
- Epsilon-Expansion



In 1D, the Ising model is [[Exact Solutions of 1D Ising Model|exactly solvable]]. However, it fails to exhibit any phase transition at any finite temperature. [[Peierl's Theorem]] explains this - regions of nonzero magnetic moments are unstable in 1 dimension.

In 2D, the Ising model is also [[Exact Solution of 2D Ising Model|exactly solvable]], albeit much more difficultly so. Onsager did this. 

In some sense, the Ising model is already a [[Mean Field Theory]]: its coupling to the external magnetic field is through the mean magnetization $\langle m \rangle = \frac{1}{N} \sum_i s_i$. Its internal interactions in the other term can also be replaced with mean field interaction, yielding the [[Curie-Weiss Mean Field Theory]].

Physically, the Ising model is often used to describe structural phase transitions in binary alloys, eg copper-zinc alloys ($\beta$ brass). These alloys have a bipartite body-centered cubic lattice, with copper and zinc sublattices dual to each other. Increasing temperature to the critical temperature (which is well below the melting temperature, $T_C$ = 742 K), some sites end up randomly swapping, the lattice is no longer bipartite, which introduces disorder. 

Can generalize to take on $q$ values, $\sigma_i \in \{1,2,\ldots,q\}$. This is the $q$-state [Potts model]], where this Ising model is the $q=2$ case.

Can generalize to take on $2s+1$ values, $s \in \left\{ 0,\frac{1}{2},1,\ldots \right\}$, $\sigma_i \in \{-s,-s+1,\ldots,s-1,s\}$. This is the [[Higher Spin Ising Model]], where this Ising model is the $s = \frac{1}{2}$ case. It has the same symmetry and thus the same critical behavior, but there is no known closed-form expression for $f$ for general $s$. See 541 HW Exercise 4 for $s=1$.

Can generalize to $N$-component vector spins, often using an interaction term $\vec{\sigma}_i \cdot \vec{\sigma}_j$ with $O(N)$ symmetry. This Ising model is the $N=1$ case.

In $d \geq 2$, can generalize to have different couplings on different directions, the anisotropic Ising model. Can have ferromagnetic behavior along one axis and antiferromagnetic behavior along another, yet even then it will still have the same critical behavior.

Can generalize to include next-to-nearest neighbor interactions. These interaction terms in general explicitly break the $Z_2$ symmetry and change critical behavior.

Exact Critical Exponents:

| Ising     |       |       |       |
| --------- | ----- | ----- | ----- |
|           | $d=2$ | $d=3$ | $d=4$ |
| $\alpha$  | 0     | 0.110 | 0     |
| $\alpha'$ | 0     | 0.110 | 0     |
| $\beta$   | 1/8   | 0.326 | 1/2   |
| $\gamma$  | 7/4   | 1.237 | 1     |
| $\gamma'$ | 7/4   | 1.237 | 1     |
| $\nu$     | 1     | 0.630 | 1/2   |
| $\nu'$    | 1     | 0.630 | 1/2   |
| $\eta$    | 1/4   | 0.036 | 0     |
| $\delta$  | 15    | 4.790 | 3     |
