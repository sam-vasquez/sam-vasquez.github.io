---
collection: notes
title: "Chemical Potential"
permalink: /note/Chemical-Potential/
---
The chemical potential is an [[Extensive and Intensive State Variables|extensive]] variable that couples to work done by adding and removing particles from a thermodynamic system. 

In the usual internal energy formulation, this comes up in 
$$
dU = TdS - p dV + \mu dn,
$$
chemical potential $\mu = \left( \frac{\partial U}{\partial n} \right)_{S,V}$.

However, this isn't easy to imagine computing in reality. 

A more useful expression comes from the [[Free Energy]]:
$$
dF = -S dT - p dV+ \mu dn,
$$
$$
\mu = \left( \frac{\partial  F}{\partial n_i} \right)_{T,V}.
$$
And also from the [[Gibbs Free Energy]]:
$$
dG = -S dT + V dp + \mu dn_i,
$$
$$
\mu = \left( \frac{\partial G}{\partial n_i} \right)_{T,p}.
$$
In fact, since $G$ is only extensive in $N$, it can be written as
$$
G = \mu(p,T) N.
$$

When a composite system is not yet in chemical equilibrium, the difference in chemical potentials drives particle number transport:

TODO: why is $\delta U = 0$ if the system is not in equilibrium?

$\delta U = 0$, volume is internally constrained, temperature and pressure are both already equal, entropy can and will still go up.
$$
0 = \Delta U = T \Delta S + \mu_1 \Delta n_1 + \mu_2 \Delta n_2
$$
$$
\Delta S = \left( \frac{\mu_1}{T} - \frac{\mu_2}{T} \right) \Delta n_1 > 0.
$$
If $\mu_1 > \mu_2$, $\Delta n_1 < 0$.
If $\mu_1 < \mu_2$, $\Delta n_1 > 0$.

It is generally observed that at high temperatures, the chemical potential becomes large and negative. This is because $\mu = \frac{G}{N}$, where $G = U + pV - TS$, entropy itself becomes large at high temperatures, and the $TS$ term dominates. 