---
tags:
  - Stat-Mech
collection: notes
title: "Block Spin Renormalization Group"
permalink: /note/Block-Spin-Renormalization-Group/
---
Kadanoff's construction of the renormalization group operation for [[Renormalization Group Theory]].

Consider a system undergoing a second order phase transition with correlation length $\xi$ diverging as $T \rightarrow T_C$. There are large domains over which the spins are correlated. For a concrete example, consider a spin model on a simple square lattice with lattice spacing $a$, at its critical temperature where $\xi \gg a$.

Kadanoff's block-spin construction replaces every $b\times b$ block of spins with the average over those spins to define a new lattice $\Lambda_{block}$, where distances $r$ in $\Lambda_{square}$ are said to be renormalized to distances $\frac{r}{b}$ in $\Lambda_{block}$. 

This defines an operator $\mathcal{R}_b$, which can be applied iteratively. If correlation length has truly diverged, then it remains infinite, and the critical temperature thus describes a fixed point of $\mathcal{R}_b$.

Assume that the (total) Gibbs free energy maps to another free energy of the same functional form, up to a factor of $b^d$ for extensivity, but with possibly different values of temperature and couplings. This motivates a Gibbs free energy of the form
$$
\mathcal{R}_b\left[ G(\tau, H) \right] =  b^{-d} G(\phi_\tau(b) \tau, \phi_h(b) H),
$$
where $\tau$ is the reduced temperature. Note that both the original and blocked systems should go critical together, so the transformations of $\tau$ and $H$ are linear. 
Further, assume that the transformations are exponentials of $b$:
$$
\mathcal{R}_b\left[ G(\tau, H) \right] =  b^{-d} G(b^{\gamma_\tau} \tau, b^{\gamma_h} H),
$$
where $\gamma_\tau$ is the thermal exponent, and $\gamma_h$ is the magnetic exponent. This makes the Gibbs free energy a [[Homogeneous Function|generalized homogeneous function]]:
$$
G(b^{\gamma_\tau/d} \tau, b^{\gamma_h/d} H) = b G(\tau, H).
$$
Often define $a \equiv \gamma/d$ for convenience.

From this form of the Gibbs free energy, one can [[Renormalization Group Derivation of Critical Exponents|derive]] all [[Critical Exponents]] in terms of just the thermal and magnetic exponents.