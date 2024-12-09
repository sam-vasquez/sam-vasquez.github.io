---
collection: notes
title: "Energy Minimization Principles"
permalink: /note/Energy-Minimization-Principles/
---
The [[Entropy Maximization Principle]] implies an energy minimization principle. Maximizing entropy for fixed energy is equivalent to minimizing energy for fixed entropy.
TODO: How?

The free energy is also minimized. If a system is placed in thermal equilbrium with a large bath, we have
$$
\Delta S_{\textrm{bath}} = \frac{\Delta E_{\textrm{bath}}}{T} = \frac{- \Delta E_{\textrm{sys}}}{T}.
$$
The composite system would maximize its entropy, so change in total entropy $\Delta S_{\textrm{sys}} + \Delta S_{\textrm{bath}}$ is positive. So this implies that 
$$
\Delta S_{\textrm{sys}} - \frac{\Delta E_{\textrm{sys}}}{T} \geq 0,
$$
which rearranges to $\Delta F \leq 0$.
A similar construction shows that Gibbs free energy is minimized, $\Delta G|_{T,p} \leq 0$.

Correlary:
Minimized free energy implies isothermal compressibility is positive. 