---
tags:
  - Stat-Mech
collection: notes
title: "Renormalization Group Derivation of Critical Exponents"
permalink: /note/Renormalization-Group-Derivation-of-Critical-Exponents/
---
The [[Block Spin Renormalization Group]] assumes that the Gibbs free energy of a magnetic system scales under renormalization by factor $b$ as 
$$
G(b^{\gamma_\tau/d} \tau, b^{\gamma_h/d} H) = b G(\tau, H).
$$

The total magnetization of the system is $M = -\left( \frac{\partial G}{\partial H} \right)_T$. Taking the derivative of the left hand side of the Gibbs free energy:
$$
\frac{\partial }{\partial H} G(b^{a_\tau} \tau, b^{a_h} H) = b^{a_h} \frac{\partial }{\partial (b^{a_h} H)} G(b^{a_\tau} \tau, b^{a_h} H) = - b^{a_h} M(b^{a_\tau}\tau, b^{a_h} H).
$$
The derivative of the right hand side is $-b M(\tau, H)$. Equating both sides,
$$
M(b^{a_\tau}\tau, b^{a_h} H) = b^{1 - a_h} M(\tau, H).
$$
Thus magnetization is also a generalized homogenenous function. Now set $H=0$ to study the spontaneous magnetization, and choose to scale by $b = (-\tau)^{-1/a_\tau}$:
$$
M(\tau, 0) = (-\tau)^{\frac{1-a_h}{a_\tau}} M(-1, 0).
$$
Thus the critical exponent beta is 
$$
\beta = \frac{1-a_h}{a_\tau}.
$$
Similar arguments by differentiation of the Gibbs free energy prove the following expressions for other critical exponents:
$$
\delta = \frac{a_h}{1 - a_h},
$$
$$
\gamma = \frac{2a_h - 1}{a_\tau},
$$
$$
\alpha = \frac{2 a_\tau - 1}{a_\tau}.
$$

These can all be put together into the following relations between critical exponents:
$$
\beta \delta = \frac{a_h}{a_\tau} = \frac{\gamma_h}{\gamma_\tau},
$$
$$
\beta (\delta - 1) = \gamma,
$$
$$
\alpha + 2\beta + \gamma = 2.
$$
These relations are all consistent with values of critical exponents determined by mean field theory, Landau-Ginzberg theory, exact solutions, and numerical calculations.

These can be inverted to express the thermal and magnetic critical exponents as $a_h = \frac{\delta}{1+\delta}$, $a_\tau = \frac{1}{\beta(1+\delta)}$.