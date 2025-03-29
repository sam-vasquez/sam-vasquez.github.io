---
tags:
  - Complex
collection: notes
title: "Residue"
permalink: /note/Residue/
---
The residue $\textrm{Res}(f,c)$ of a complex function $f$ at $c$, is the coefficient of $(z-c)^{-1}$ in its Laurent series expansion around $c$.

There are various simple ways to calculate the residue.

The analyticity of the function at $c$ may be evaluated through
$$
\lim_{z\rightarrow c} (z-c) f(z).
$$
If the limit exists, then $f$ has a simple pole at $c$ and this limit is its residue. If the limit is 0, then either $f$ is analytic at $c$ or has a removable singularity there, where a function has a removable singularity when it can be analytically continued to a [[Holomorphic Function|holomorphic]] function on the disk $|y-c| < R$. In either case, its residue is 0. If the limit does not exist, then $f$ has an essential singularity at $c$.

If the pole has multiplicity $m$, the residue is instead the limit
$$
\frac{1}{(m-1)!} \lim_{z\rightarrow c} \frac{d^{m-1}}{dz^{m-1}} (z-c)^m f(z).
$$

Computing the residues of poles in $f$ can allow for simple computation of line integrals through the [[Residue Theorem]].