---
tags:
  - QFT
collection: notes
title: "Mermin-Wagner Theorem"
permalink: /note/Mermin-Wagner-Theorem/
---
Sometimes also called the Mermin-Wagner-Coleman theorem, the Mermin-Wagner theorem states that it is impossible to spontaneously break a continous gobal symmetry in $d = 2$ dimensions at finite temperature.

This comes from the [[Nambu-Goldstone Theorem]]: breaking a continuous global symmetry yields massless Nambu-Goldstone bosons. 

In field theory on Minkowski spacetime, the propagator (2-point correlation function) of a particle with mass $m$ is $\frac{1}{k_\mu k_\nu \eta^{\mu\nu} - m^2}$. Its Fourier transform is 
$$
\langle \phi(0) \phi(x) \rangle = \int \frac{d^d k}{(2\pi)^d} \frac{e^{ i k\cdot x }}{k^2 - m^2}.
$$
A [[Wick rotation]] to the Euclidean metric allows writing the integrand in terms of the hyperspherical radial coordinate $k^2 \rightarrow \sum_{i=1}^d k_i^2$: In the massless limit,
$$
\langle \phi(0) \phi(x) \rangle = \int_{S^{d-1}} d\Omega_k \int_0^{\infty} \frac{(k^{d-1} dk) e^{ i k \cdot x }}{k^2} \propto \int_0^\infty k^{d-3} dk.
$$
For $d > 2$, this is finite as $k \rightarrow 0$ at the lower limit of integration. But for $d = 2$, this is logarithmically divergent. Physically, massless Goldstone modes would destabilize any magnetically ordered states.

Continuous spin systems can still have a finite temperature phase transition, they just can't break the global symmetry. For example, the [[XY Model]] has a phase transition, but it does not involve magnetization in the low temperature phase and does not break the $O(2)$ invariance. 
