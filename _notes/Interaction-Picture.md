---
tags:
  - Quantum
collection: notes
title: "Interaction Picture"
permalink: /note/Interaction-Picture/
---
When Hamiltonian is written as $H = \bar{H} + V$, $\bar{H}$ a free Hamiltonian and $V$ an interaction term, the interaction picture can be defined such that states evolve according to the interaction term, and operators evolve according to the free term.

The transformation from Schrodinger picture to Heisenberg picture is
$$
\ket{ \psi, t }_I = e^{ i \bar{H} t }\ket{ \psi, t }_S,
$$
$$
\rho_I(t) = e^{ i \bar{H} t } \rho_S e^{ -i \bar{H} t },
$$
$$
\mathcal{O}_I(t) = e^{ i \bar{H} t } \mathcal{O}_S e^{ -i \bar{H} t }.
$$

States evolve as
$$
i \partial_t \ket{ \psi, t }_I = V_I(t) \ket{ \psi, t }_I,
$$
where $V_I(t) = V_I(t) = e^{ i \bar{H} t }V e^{ -i \bar{H} t }$. This can be shown by transforming the time evolution equation in the Schrodinger picture, noting that $\bar{H}$ and $V$ do not necessarily commute.

Density matrices evolve as
$$
i \partial_t \rho_I(t) = \left[ \rho_I(t), \bar{H} \right] + e^{ i \bar{H} t } \left[ \bar{H} + V, \rho_S(t) \right] e^{ -i \bar{H} t } = \left[ V_I(t), \rho_I(t) \right].
$$

Operators evolve as
$$
i \partial_t \mathcal{O}_I(t) = \left[ \mathcal{O}_I(t), \bar{H} \right].
$$

A time evolution equation for states needs to take into account that $V_I$ should commute with each other for $t \neq t'$. Can find that
$$
\ket{ \psi, t }_I = U_I(t,t_0) \ket{ \psi, t_0 }_I,
$$
$$
U_I(t,t_0) = T e^{ -i \int_{t_0}^t dt' V_I(t') }.
$$
The time-ordered product can be expanded into 
$$
U_I(t,t_0) = 1 - i \int_{t_0}^t dt' V_I(t') + (-i)^2 \int_{t_0}^t dt' \int_{t_0}^{t'} t'' V_I(t') V_I(t'') + \ldots
$$

The interaction picture is useful for any kind of perturbation theory - it is encountered in non-relativistic time-dependent perturbation theory, scattering processes in perturbative QFT, and the dynamics of open quantum systems.

Using $\bar{H} = \sum_\alpha E_\alpha a_\alpha^\dagger a_\alpha$ and the that fact that any interaction operator is a linear combination of creation and annihilation operators, can find that 
$$
a_{\alpha, I}(t) = e^{ i \bar{H} t } a_\alpha e^{ -i \bar{H} t } = a_\alpha + it \left[ H, a_\alpha \right] + \frac{1}{2} (it)^2 \left[ H, \left[ H, a_\alpha \right] \right] + \ldots = e^{ -i E_\alpha t } a_\alpha.
$$
Likewise, $a_{\alpha,I}^\dagger(t) = a_\alpha^\dagger e^{ i E_\alpha t }$.

