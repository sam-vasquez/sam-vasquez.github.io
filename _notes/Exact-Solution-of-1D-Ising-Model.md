---
collection: notes
title: "Exact Solution of 1D Ising Model"
permalink: /note/Exact-Solution-of-1D-Ising-Model/
---
In 1D. Consider two cases. One where exactly half are spin up, half are spin down. Without an external field. You have energy contribution $-JN/2$ from both halves, and another $+J$ from the domain wall. Total energy $-JN + J \rightarrow -JN$. Other case, alternating spins. Also get energy $+JN$. It doesn't fully capture the difference, without the external field.

$$
Z = \sum_{s_1} \ldots \sum_{s_N} e^{ \beta \mu H \sum s_i + \beta J \sum s_i s_j }
$$
With periodic BC:
$$
Z = \sum_{s_1} \ldots \sum_{s_N} e^{ \sum k s_i s_{i+1} + 1/2 h (s_i + s_{i+1}) }.
$$
Divide by two to not double count. $k = \beta J$, $h = \beta \mu H$, $\mu$ is magnetic moment.
There are four possible cases of contribution per pair. If both up, $e^{ k+h }$. If mixed, $e^{ -k }$. If both down, $e^{ k-h }$. Introduce transfer matrix:
$$
P = \begin{pmatrix} 
e^{ k+h } & e^{ -k } \\
e^{ -k } & e^{ k - h }
\end{pmatrix} 
$$
$$
Z = \sum_{s_1} \ldots \sum_{s_N} \bra{ s_1 } P \ket{ s_2 } \bra{ s_2 } P \ket{ s_3 } \ldots \bra{ s_N } P \ket{ s_1 }.
$$
Pavlovian bells should be going off in your head now. Start putting identity operator in random places and hope it simplifies your problem.
$$
Z = \sum_{s_1} \bra{ s_1 } P \sum_{s_2} \ket{ s_2 } \bra{ s_2 }\ldots P \ket{ s_1 } = \sum_{s_1} \bra{ s_1 } P^N \ket{ s_1 } = Tr(P^N).
$$
Diagonalize to eigenbasis, power of $N$ is trivial, trace is trivial.
Eigenvalues are $\lambda = e^k \cosh(h) \pm \sqrt{ e^{-2k} + e^{2k} \sinh^2(h) }$.
In thermodynamic limit, throw away the smaller eigenvalue.
$$
1/N \ln Z = \ln \lambda_+.
$$
Pull out $e^k$, write out free energy.
$$
F = -k_B T \ln Z = -NJ - Nk_B T \ln \left[  \cosh(h) + \sqrt{ e^{-4k} + \sinh^2(h) } \right].
$$
Limits: 
Turn off the Hamiltonian, $J$ $h$ and $k$ go to zero, $F = - TS$, expect it goes to $-Nk_BT  \ln(2)$. Indeed, cosh goes to 1, exp goes to 1, sinh goes to 0, get ln2. Yay. 
Turn off just the external field. $h$ to zero. exp survives, get $A = - N k_B T \ln(2 \cosh(k))$.

Get magnetization by $dE = T dS - M dH$ (applying field along magnetic moment lowers energy), $M = - \left( \frac{\partial F}{\partial H} \right)_T$. The derivative is nasty but anyone can do it. $M = \frac{N\mu\sinh(h)}{\sqrt{ e^{ -4k } + \sinh^2(h)} }$.
When external field turned off, if $T$ finite, $k$ finite, $M=0$. It only gets a magnetization at $T=0$, which isn't exactly good for anything. 
It would seem that it's not interesting, but it can still be neat to derive correlation lengths.

When interaction turned off, $M = N \mu \tanh(\beta \mu H)$. See whiteboard for plots.
