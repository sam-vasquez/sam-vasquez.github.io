---
tags:
  - Stat-Mech
collection: notes
title: "Exact Solution of 2D Ising Model"
permalink: /note/Exact-Solution-of-2D-Ising-Model/
---

(This page assumes the square lattice; the critical behavior is identical for all 2D lattices, which is evident from divergence of the correlation distance and from renormalization group theory.)

Kramers and Wanier first obtained the critical temperature using [[Kramers-Wannier Duality]] between low- and high-temperature expansions of the partition function. Even though it doesn't let us calculate other thermodynamic properties, it is evidently a powerful method to determine critical temperature without much difficulty. 

The critical temperature is $T_c = \frac{2}{\ln(1+\sqrt{ 2 })} \frac{|J|}{k_B} \approx 2.269 \frac{J}{k_B}$, derived from $\sinh^2(2k_C) = 1$. Note that this is lower than [[Curie-Weiss Mean Field Theory]] predicts, $-4$.

Onsager obtained the first expression for the free energy, through a [[Transfer Matrix Derivation of 2D Ising Model|Transfer matrix]] method. This is 
$$
f = \ln 2 + \frac{1}{2} \int_{-\pi}^\pi \frac{d\theta_1}{2\pi} \int_{-\pi}^\pi \frac{d\theta_2}{2\pi} \ln\left[ \cosh^2 (2k) - \sinh(2k) \mathcal{P}(\theta_1, \theta_2) \right],
$$
where $\mathcal{P}(\theta_1,\theta_2) = \cos \theta_1 + \cos \theta_2 \in (-2,2)$.

This free energy is non-analytic when the argument of the logarithm is $0$, which can happen for certain values of $\theta_1$ and $\theta_2$ during integration. In particular, the critical temperature is at the first onset of non-analyticity, and it suffices to find the smallest value
of the logarithm argument in the integration domain, and identify
the value of $k$ for which it vanishes.

When $k > 0$ and the model is ferromagnetic, the logarithm argument is minimized by $\mathcal{P} = 2$. When $k < 0$, the logarithm argument is minimized by $\mathcal{P} = -2$.

Using the ferromagnetic case, the condition that the argument is 0 comes out to 
$$
\begin{align}
\cosh^2(2k) - 2 \sinh(2k) &= 0 \\
\cos(2k) &= 2 \tanh(2k)  \\
\frac{1+z^2}{2z} &= 2 \frac{1-z^2}{1+z^2}  \\
z^4 + 4z^3 + 2z^2 - 4z + 1  &= 0  \\
(z^2 + 2z - 1)^2 &= 0,
\end{align}
$$
where low-temperature expansion variable $z \equiv e^{ -2k }$ was used. See bottom of page for expressions in terms of $z$.
This is solved by $z_C = -1 + \sqrt{ 2 }$, or $k_C = \frac{1}{2} \ln(1 + \sqrt{ 2 })$, as expected.

This is further validated using our knowledge of the critical temperature, $\sinh(2k_C) = \pm1$ depending on whether it is ferromagnetic or antiferromagnetic, $\cosh^2(2k_C) = 2$: the free energy has poles in the logarithm at the critical temperature when
FM: $\mathcal{P} = 2$,
AFM: $\mathcal{P} = -2$.

At high temperature, $\cosh \rightarrow 1$, $\sinh \rightarrow 0$, $f \rightarrow \ln 2$, as expected from effectively freezing out the spin-spin interaction.

At low temperature, assuming FM, the spins approach a completely ordered state, so we would expect $Z \rightarrow 2 e^{ 2kN }$, $f \rightarrow 2k$. Indeed, $\cosh^2(2k) \rightarrow \frac{e^4k}{4}$ dominates $\sinh(2k) \rightarrow \frac{e^{ 2k }}{2}$, $f \rightarrow \ln 2 + \int \ln\left( \frac{e^{ 4k }}{4} \right) = 2k$.

Some expressions are easier to derive by rewriting $f$ in terms of the high-temperature expansion variable $v = \tanh k$ and the low-temperature expansion variable $z = e^{ -2k }$:
$$
f = 2k + \frac{1}{2} \int_{-\pi}^\pi \frac{d^2 \theta}{(2\pi)^2} \ln\left[ (1+z^2)^2 - 2z(1-z^2)\mathcal{P} \right].
$$
One integral can be carried out: (Todo: Derive this.)
$$
f = \ln (2 \cosh(2k)) + \frac{1}{2} \int_0^\pi \frac{d\phi}{\pi} \ln \left[ \frac{1 + \sqrt{ 1 - \kappa^2 \sin^2\phi }}{2} \right],
$$
where $\kappa = \frac{2 \sinh(2k)}{\cosh^2(2k)}$. $\kappa$ is 0 at $k=0$, 0 at $k=\infty$, and 1 at $k_C$. And indeed, there is non-analyticity at $\kappa = 1$.

The energy is
$$
\begin{align}
\bar{U} &= -\frac{\partial f}{\partial \beta} = -J \frac{\partial f}{\partial k} \\
&= -J \coth(2k) \left[ 1 + \frac{2}{\pi} (2 \tanh^2(2k) - 1) K(\kappa) \right],
\end{align}
$$
where $K$ is the [[Elliptic Integrals|complete elliptic integral of the first kind]] with elliptic modulus $\kappa$.
$K$ only depends on $\kappa^2$, so FM and AFM are equivalent. 
Despite logarithmic divergence of $K(\kappa)$ at $\kappa \rightarrow 1$ ($k \rightarrow k_C$), the prefactor $2\tanh^2(2k) - 1$ goes to 0 faster, killing the logarithmic divergence and keeping $\bar{U}$ finite.
As $T \rightarrow 0$ and $\kappa \rightarrow 0$, using the Taylor series of $K$,
$$
\begin{align}
\bar{U} &\rightarrow \frac{-J}{\tanh(2k)} \left[ 1 + \frac{2}{\pi} (2 \tanh^2(2k) - 1)\frac{\pi}{2} \right]\\
&= -2J \tanh(2k)  \\
&= -2J.
\end{align}
$$
In general, on a lattice with coordination number $q$, the energy of the totally ordered state would have $\bar{U}(T=0) \rightarrow -\frac{\Delta}{2} J$, which this result agrees with.

The heat capacity is 
$$
\bar{C} = \frac{\partial \bar{U}}{\partial T} = k_B k^2 \frac{\partial^2 f}{\partial k^2},
$$
which in the $k \rightarrow k_C$ limit comes out to 
$$
C \propto -\ln(|k-k_C|) \sim -\ln|\tau|.
$$
This is critical behavior that corresponds to a power law with $\alpha = \alpha' = 0$.

The spin-spin correlation functions are polynomials in complete elliptic integrals:
$$
\langle \sigma\sigma \rangle =
\begin{cases}
\sqrt{ 1 + k_>^{-1} } \left[ \frac{1}{2} + (k_> - 1) \frac{K(k_>)}{\pi} \right], & T > T_C \\ \\
\sqrt{ 1 + k_< } \left[ \frac{1}{2} - (k_< - 1)\frac{K(k_<)}{\pi} \right], & T < T_C
\end{cases}
$$
where $k_> = \sinh^2(2k)$ for $T > T_C$, and $k_< = [\sinh^2(2k)]^{-1}$ for $T < T_C$.
At $T = T_C$, $k_> = k_< = 1$, and both correlation functions are $\frac{1}{\sqrt{ 2 }}$.

The spontaneous magnetization can be expressed in terms of $k_<$ as $m = (1-k_<^2)^{1/8}$, $\implies \beta = 1/8$. Result by C. N. Yang.

For more details on derivations, see Domb & Green Phase transitions review paper - https://en.wikipedia.org/wiki/Phase_Transitions_and_Critical_Phenomena
Phase transitions Domb Lebowitz


Some helpful expressions using the expansion variables:
$$
\sinh(k) = \frac{v}{\sqrt{ 1-v^2 }} = \frac{1-z}{2\sqrt{ z }}, \cosh(k) = \frac{1}{\sqrt{ 1-v^2 }} = \frac{1+z}{2\sqrt{ z }}, \tanh(k) = \frac{1-z}{1+z}
$$
$$
\sinh(2k) = \frac{2v}{1-v^2} = \frac{1-z^2}{2z}, \cosh(2k) = \frac{1 + z^2}{2z}
$$