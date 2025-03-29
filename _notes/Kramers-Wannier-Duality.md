---
tags:
  - Stat-Mech
collection: notes
title: "Kramers-Wannier Duality"
permalink: /note/Kramers-Wannier-Duality/
---
The Kramers-Wannier duality is a duality in statistical mechanics between the high-temperature and low-temperature expansions of a lattice spin model. In particular, a duality between loops on the lattice (low temp) and loops on the dual lattice (high temp). 

For example, recall the character decomposition of the zero-field Ising model.
$$
Z = (\cosh(k))^{e(\Lambda)} \sum_{\{\sigma_i\}} \prod_{e_{ij}} (1 + v\sigma_i \sigma_j),
$$
$v = \tanh(k)$, $e(\Lambda)$ is the number of edges on the lattice. Square 2D lattice has $e(\Lambda) = 2N$.

As $T\rightarrow\infty$, $k\rightarrow 0$, $v\rightarrow 0$, $v$ is a high temperature expansion variable. We previously used this in 1D to get the correlation function, and by summing over all $N$ cycles of length 4 on the lattice, we got
$$
\begin{align}
Z_H &= (\cosh k)^{2N} \sum_{\sigma_i} \left[ 1 + N v^4 + \ldots \right] \\
&= 2^N (\cosh k)^{2N} \left[ 1 + N v^4 + \ldots \right].
\end{align}
$$
For large $N$, $2^N (\cosh k)^{2N} \approx 2^N e^{ 2Nk } 2^{-2N} = e^{ 2Nk } 2^{-N}$.

For a low temperature expansion, start at $T=0$ with a completely ordered phase. This contributes $2e^{ke(\Lambda)}$ to $Z$.
For a first correction term, consider flipping a single spin. This contributes $2e^{ke(\Lambda)-2kq}$. Define $z\equiv e^{ -2k }$. As $T\rightarrow 0$, $k\rightarrow \infty$, $z \rightarrow 0$, $z$ is a low temperature expansion variable. 
There are $N$ choices of spin to flip, so this gives
$$
Z_L = 2 e^{2Nk} \left[ 1 + N z^4 + \ldots \right].
$$

There's a correspondance between high temperature and low temperature expansions: each term in the high temp expansion only came from joining edges with a common vertex. This suggests that the high temp expansion lives on the dual lattice, and $z^4 \leftrightarrow v^4$ through self-duality. Can see the duality pictorally by drawing loops around spins. Next leading terms are larger loops, with the next largest a loop of length 6 enclosing two neighboring spins.

So the critical temperature occurs at the point where high and low temp expansions coincide:
$$
\frac{Z_L}{2e^{ 2Nk }} = \frac{Z_H}{2^N (\cosh k)^{2N}}
$$
$$
f_L = -\frac{1}{\beta}\lim_{N\rightarrow\infty} \frac{\ln Z_L}{N}
$$
$$
= -\frac{1}{\beta} \lim_{N\rightarrow\infty} \frac{\ln Z_H}{N} - \frac{1}{\beta} \lim_{N\rightarrow \infty} \frac{\ln \left[ \frac{2e^{ 2Nk }}{2^N (\cosh k)^{2N}} \right]}{N} 
$$
$$
= f_H - \frac{1}{\beta} \lim_{N\rightarrow\infty} \frac{\frac{\partial }{\partial N} \left[ \frac{2e^{ 2Nk }}{2^N (\cosh k)^{2N}} \right]}{\left[ \frac{2e^{ 2Nk }}{2^N (\cosh k)^{2N}} \right]}
$$
$$
= f_H - \frac{1}{\beta} \lim_{N\rightarrow\infty} \frac{ 2k \left[ \frac{2e^{2Nk}}{2^N (\cosh k)^{2N}} \right] - \ln 2 \left[ \frac{2 e^{2Nk}}{2^N (\cosh k)^{2N}} \right] - 2 \ln(\cosh k) \left[ \frac{2 e^{2Nk}}{2^N (\cosh k)^{2N}} \right] }{\left[ \frac{2e^{ 2Nk }}{2^N (\cosh k)^{2N}} \right]}
$$
$$
= f_H - \frac{1}{\beta} \lim_{N\rightarrow\infty} (2k - \ln 2  - 2 \ln(\cosh k) )
$$
$$
= f_H + \frac{1}{\beta} (\ln 2  + 2 \ln(\cosh k) - 2k).
$$

By continuity of the free energy between the high and low temperature phases, the right term vanishes at the critical point. Aside from $T = 0$, this occurs at $k^* = \frac{1}{2} \ln(\pm 1 + \sqrt{ 2 }) \approx \pm 0.44$. 

When $J > 0$ and the system is ferromagnetic, the physical solution is $k_C = \frac{1}{2}\ln(1 + \sqrt{ 2 })$. When $J < 0$ and the system is antiferromagnetic, the physical solution is $k_C = \frac{1}{2}\ln (-1 + \sqrt{ 2 })$.

In either case, the critical temperature is $T_C = \frac{2}{\ln(1+\sqrt{ 2 })} \frac{|J|}{k_B}$, matching the result of Onsager's solution.

Reference:
https://paramekanti.weebly.com/uploads/1/1/2/8/11287579/sreekar_voleti_asm_term_paper_-_kramers_wannier_duality.pdf

Lecture 19