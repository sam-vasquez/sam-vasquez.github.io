---
collection: notes
title: "Free Energy"
permalink: /note/Free-Energy/
---
Free energy is a thermodynamic potential that is a [[Legendre Transformations|Legendre transformation]] of internal energy $U$ to replace state variables $(S,V,n)$ with conjugate variables $(T,V,n)$.

The motivation is that it is excessively unclear how exactly you're supposed to hold entropy constant while varying volume or particle number. In fact, it's essentially impossible. But controlling temperature is simpler.

The [[Thermodynamic Identity]] for free energy $F(T,V,n)$ is given as
$$
dF = -S dT - p dV + \mu_i \; dn_i.
$$
It therefore provides convenient expressions for [[Entropy]], pressure, and [[Chemical Potential]]:
$$
S = -\left( \frac{\partial F}{\partial T} \right)_{V,n}
$$
$$
p = -\left( \frac{\partial F}{\partial V} \right)_{T,n}
$$
$$
\mu = \left( \frac{\partial F}{\partial n} \right)_{T,V}
$$
Note that when temperature is held constant, $dF|_T = -p dV + \mu_i dn_i = \delta W$. Free energy therefore becomes a convenient way to understand how much work we can extract from a system, hence the name. (Perhaps "freeable" energy is more appropriate?)

Free energy is related to the [[Canonical Ensemble]]:
$$
F = - k_B T \ln Z.
$$

