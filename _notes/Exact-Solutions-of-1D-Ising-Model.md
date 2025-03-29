---
tags:
  - Stat-Mech
collection: notes
title: "Exact Solutions of 1D Ising Model"
permalink: /note/Exact-Solutions-of-1D-Ising-Model/
---
The [[Ising Model]] has Hamiltonian
$$
\mathcal{H} = - J \sum_{(ij)} s_i s_j - \sum H \mu s_i,
$$
$(ij)$ a sum over nearest neighbors. With periodic boundary conditions on a 1D chain, this becomes 
$$
\mathcal{H} = -J \sum s_i s_{i+1} - H \mu \sum s_i.
$$
(In the thermodynamic limit, the periodic boundary should have vanishing impact, since the domain wall is just a single spin out of $N$ spins.)

The canonical ensemble partition function is 
$$
Z = \sum_{s_1} \ldots \sum_{s_N} e^{ \sum \left[  k s_i s_{i+1} + \frac{1}{2} h (s_i + s_{i+1}) \right]},
$$
where $k \equiv \beta J$ and $h \equiv \beta \mu H$.

In the zero-field limit, its [[Character (Representation Theory)|character]] decomposition is
$$
Z = (\cosh(k))^N \sum_{\{\sigma_i\}} \prod_i (1 + v\sigma_i \sigma_{i+1}),
$$
$v = \tanh(k)$.

Some insight can be gained by studying just 3 spins. For example, see 540 exercise 40, 541 lecture, and [[Partition Function of Three Classical Spins]].

Otherwise, results can be obtained in a number of ways.
- [[Transfer Matrix Derivation of 1D Ising Model|Transfer matrix]]
- [[High Temperature Derivation of 1D Ising Model Correlations|High temperature expansion]]
- [[Notes/Renormalization Group Analysis of 1D Ising Model|Renormalization group]]

The [[Transfer Matrix Derivation of 1D Ising Model|transfer matrix method]] gives the free energy as
$$
f \equiv \lim_{N\rightarrow\infty} \beta \frac{F}{N} = -J - k_B T \ln \left[  \cosh(h) + \sqrt{ e^{-4k} + \sinh^2(h) } \right].
$$

When all interactions are turned off, ($h$ ($H$) and $k$ ($J$) all go to zero), $F/N$ goes to $-k_B T \ln(2)$, as expected from $F(E=0) = -TS$. When only the external field is turned off ($h$ goes to zero), $F/N$ goes to $-k_BT \ln (2 \cosh(k))$.

The energy is 
$$
\begin{align*}
\frac{E}{N} &= \frac{\partial f}{\partial \beta} \\
&= 
\frac{\partial h}{\partial \beta} \frac{\partial
f}{\partial h} + \frac{\partial k}{\partial \beta}
\frac{\partial f}{\partial k} 
\end{align*}
$$
Todo: simplify.
Todo: Heat capacity, derivation in lecture 5/6.

Using convention $dE = TdS + HdM$, the magnetization is $M = -\left( \frac{\partial G}{\partial H} \right)_T = - \mu N \frac{\partial f}{\partial h}$. This derivative comes out to 
$$
m \equiv \frac{M}{N} = - \mu \frac{\partial f}{\partial h} =  \frac{\mu\sinh h}{\sqrt{ e^{ -4k } + \sinh^2 h} },
$$
full derivation is shown in lecture 6. 
When nearest-neighbor interactions are turned off ($k$ goes to zero), $m = \mu \tanh(\beta \mu H)$. This replicates ideal results. Todo: Locate and attach that result. Todo: insert plots. See whiteboard for plots.
When $H$ goes to 0, the zero-field magnetization goes to 0 for all finite $T$. It only has nonzero spontaneous magnetization at $T=0$. This is a discontinuity in a first derivative of free energy.

The [[Magnetic Susceptibility]] is 
$$
\frac{\chi}{N} = \left( \frac{\partial m}{\partial H} \right)_T = \beta \mu \frac{\partial m}{\partial h} = \frac{\mu^2 \beta e^{ -4k} \cosh h}{(e^{ -4k } + \sinh^2 h)^{3/2}}.
$$
When $H$ goes to 0, the zero-field susceptibility is $\chi \sim \beta e^{ 2k }$, which diverges exponentially as $T \rightarrow 0$. This is an essential singularity in a second derivative of free energy.

Together, the spontaneous magnetization and divergent susceptibility at $T=0$ imply a phase transition. Exponential divergence is somewhat peculiar among non-analytic behavior of phase transitions.

When $H \neq 0$, at high temperature, $\bar{\chi} \rightarrow \beta$. This inverse dependence on temperature is known as Curie's law.
When $H \neq 0$, at low temperature, the susceptibility depends on whether the system is ferromagnetic or antiferromagnetic.
Ferromagnetic ($J > 0$): $\bar{\chi} \rightarrow 0$. When the system is completely ordered, increasing the external field can't have any additional effect on ordering, so it makes sense that this derivative is 0.
Antiferromagnetic ($J<0$): Complicated because of frustration. See hw.


Proceed to calculate 2-spin correlation (See lecture 6). $\langle \sigma_0 \sigma_l \rangle = v^l$, $l \geq 0$. $|\langle \sigma_0 \sigma_l \rangle|$ is a monotonically decreasing function of $l$ the distance between the two spins in lattice units, which makes sense that separating the spins decreases mutual influence. Also monotonically decreasing function of temperature.

Correlation length $\xi$. Take $J > 0$ wlog. For $T \neq T_C$, a connected correlation function in general decays exponentially as the distance between spins gets large: $\langle \sigma_0 \sigma_r \rangle \sim e^{ -r/\xi }$. So
$$
v^r = e^{ -r/\xi } \implies \xi = \frac{1}{\ln (1/v)}.
$$
Since $v$ less than 1 and decreases with increasing temperature, $\xi$ decreases. As $T$ increases, there is greater thermal disorder, correlations die off faster at distance. 

As $T$ goes to zero, or $k$ goes to infinity:
Convenient to write 
$$
\frac{1}{v} = \frac{\cosh k}{\sinh k} = \frac{1 + e^{ -2k }}{1 - e^{ -2k }} \approx (1 + e^{ -2k })(1+e^{ -2k }) \approx 1 + 2e^{ -2k }.
$$
$$
\ln(1/v) \approx \ln (1 + 2e^{ -2k }) \approx 2e^{ -2k }
$$
$$
\xi \approx \frac{1}{2} e^{ 2k }.
$$
Correlation length diverges exponentially as $T\rightarrow 0$, an essential singularity.

Another way to calculate $\chi$:
$$
\beta^{-1} \bar{\chi} = \lim \frac{1}{N} \sum_{ij} \langle \sigma_i \sigma_j \rangle,
$$
$ij$ over all sites. Since the lattice is homogeneous, 
$$
\sum_{ij} \langle \sigma_i \sigma_j \rangle = \sum_j \langle \sigma_0 \sigma_j \rangle,
$$
$j \in \mathbb{Z}$.
Since $\langle \sigma_0 \sigma_{j} \rangle = v^{|j|}$, $\beta^{-1} \bar{\chi} = \frac{1+v}{1-v} = e^{ 2k }$, as we derived before. 









