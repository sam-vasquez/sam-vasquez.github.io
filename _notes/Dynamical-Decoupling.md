---
tags:
  - Quantum-Information
collection: notes
title: "Dynamical Decoupling"
permalink: /note/Dynamical-Decoupling/
---
Dynamical decoupling is an approach to error mitigation that applies a control on the system to average out errors introduced by the surrounding environment.

Consider a qubit coupled to a thermal bath of harmonic oscillators with states $k$, creation/annihilation operators $b_k^\dagger$, $b_k$, through a purely dephasing channel. The Hamiltonian is
$$
\mathcal{H} = \mathcal{H}_Q + \mathcal{H}_B + \mathcal{H}_I
$$
$$
= \frac{1}{2} \hbar \omega_0 Z + \sum_k \hbar \omega_k b_k^\dagger b_k + \sum_k \hbar Z (g_k b_k^\dagger + g_k^* b_k).
$$
Assume that at initial time $t_0$, the total density matrix $\rho$ is separable (unentangled),
$$
\rho = \rho_Q(t_0) \otimes \rho_B(t_0),
$$
and the bath's initial state is a thermal state with density matrix
$$
\rho_B(t_0) = \prod_k \left( 1 - e^{ -\beta \hbar \omega_k } \right) e^{-\beta \hbar \omega_k b_k^\dagger b_k}.
$$
Tracing over the bath states, their reduced density matrix is
$$
\rho_Q(t) = \textrm{Tr}_B \left[ e^{ -i \mathcal{H} t /\hbar } \rho(0) e^{ i \mathcal{H} t/\hbar } \right],
$$
and its coherence between the qubit's $\ket{ 0 }$ and $\ket{ 1 }$ states is represented through its off-diagonal term $\rho_{01}(t)$.
Under these assumptions, the time evolution can be analytically carried out in the interaction picture, and it is found that the (Schrodinger picture) density matrix has coherence
$$
\rho_{01}(t) = e^{-i \omega_0 (t-t_0)} e^{ -\Gamma(t, t_0) } \rho_{01}(t_0),
$$
where
$$
\Gamma(t,t_0) = \sum_k \frac{4|g_k|^2}{\omega_k^2} (1 - \cos\left[ \omega_k (t - t_0) \right]) \coth \left( \frac{\beta \hbar \omega_k}{2} \right),
$$
or in terms of the spectral density
$$
I(\omega) = \sum_k \delta(\omega - \omega_k) |g_k|^2,
$$
$$
\Gamma(t,t_0) = 4 \int_0^\infty d\omega \; I(\omega) \frac{1 - \cos\left[ \omega(t - t_0) \right]}{\omega^2} \coth\left( \frac{\beta \hbar \omega}{2} \right).
$$
The first factor, representing the coupling strength between the system and the bath modes, is manifestly positive. Cosine is in the range -1 to 1, so the second factor is positive. And the third factor is $2\langle n(\omega) \rangle + 1$, $\langle n(\omega) \rangle$ the occupation number of mode $\omega$, and therefore positive. So $\Gamma$ is positive, and it is seen that the interaction with the environment causes qubit coherence to decay exponentially in time.

Dynamical decoupling counters this bath-system interaction by intentionally inducing spin-flip transitions. The idea is that, since $\mathcal{H}_I$ is proportional to $Z$, then the bath will have an equal and opposite contribution when the spin is flipped, since $XZX = -Z$. By making the system flip back and forth quickly, one essentially averages out the contributions from $\mathcal{H}_I$, effectively decoupling the system from the environment. This is considered a pulse sequence of $XX$.

An alternative pulse sequence $YY$ can handle dissipative error channels, since in those cases the interaction is proportional to $X$, and $YXY = -X$.

Todo: How does this actually kill decoherence?