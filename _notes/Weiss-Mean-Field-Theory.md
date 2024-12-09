---
collection: notes
title: "Weiss Mean Field Theory"
permalink: /note/Weiss-Mean-Field-Theory/
---
[[Mean Field Theory]] of the [[Ising Model]].

Writing the Hamiltonian as 
$$
\mathcal{H}_{MF} = -\mu \sum_i H_i(m) s_i, 
$$
the coefficients are determined by 
$$
H_i = -\frac{1}{\mu} \frac{\partial }{\partial s_i} \left( \mathcal{H}_{IM} \right) = H + \frac{J}{\mu} \sum_{\textrm{nearest neighbors}}^q s_j.
$$
The approximation is to replace the value of all $q$ nearest neighbors with $\langle s_i \rangle \equiv m$:
$$
H_i = H + \frac{J}{\mu} q m.
$$
$$
m = \langle s_i \rangle = \sum_{s_i} \frac{1}{Z} e^{ -\beta (-\mu H_i s_i) } s_i
$$
$$
m = \frac{e^{ \beta (\mu H + J q m) } - e^{ - \beta (\mu H + Jqm) }}{e^{ \beta(\mu H + Jqm) } + e^{ -\beta (\mu H + Jqm) }}.
$$
$$
m = \tanh (\beta \mu H + \beta J qm).
$$
See plot in whiteboard. (Also Pathria Figure 12.6)3

Mean field theory predicts a spontaneous magnetization.
Considering the case of $H=0$:
$$
m = \tanh(\beta J q m).
$$
Using the plot as guidance, it has solutions when the lines $y = m$ and $y = \tanh(\beta J q m)$ intersect. This is only when $\beta J q > 1$. So the critical temperature is $T_c = \frac{Jq}{k_B}$.

In 2D, $q=4$. $T_C = 4 \frac{J}{k_B}$. The actual solution is $2.269 \frac{J}{k_B}$. In general dimensions:
1D: 0 vs 2
2D: 2.269 vs 4
3D: $\sim$ 4.513 vs 6
4D actually gives the exact critical exponents for deep reasons. This is why you get sketchy $4-\epsilon$ expansions.
In the limit of high dimension, the result for critical temperature becomes exact.

Very close to and below the critical temperature, the magnetization is small and the tanh can be expanded to third order in $\beta$:
$$
m \approx \beta J qm - \frac{1}{3} (\beta J q m)^3 = \frac{T_c}{T} m - \frac{1}{3} \left( \frac{T_c}{T} \right)^3 m^3.
$$
$$
m = \left[ 3 \left( \frac{T_c}{T} \right)^3 \left( 1 - \frac{T}{T_c} \right) \right]^{1/2}.
$$
$$\implies \beta = 1/2.$$
