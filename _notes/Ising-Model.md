---
collection: notes
title: "Ising Model"
permalink: /note/Ising-Model/
---
The Ising model is the simplest example of an interacting spin model. It models a simple magnetic system as a lattice of classical spins aligned with each other and/or an external magnetic field. It's use as a toy model is that it hopefully exhibits a spontaneous magnetization as a phase transition.

The Ising model has Hamiltonian
$$
\mathcal{H} = - J \sum_{(ij)} s_i s_j - \sum H \mu s_i,
$$
where $J$ is an interaction energy, $(ij)$ denotes a sum over nearest neighbor pairs, $H$ is the external (applied) magnetic field, and $\mu$ is the magnetic moment.


In 1D, the Ising model is exactly solvable. However, it fails to exhibit any phase transition at any finite temperature.


In 2D, the Ising model is also exactly solvable, albeit much more difficultly so. 