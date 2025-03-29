---
tags:
  - Quantum
collection: notes
title: "Heisenberg Picture"
permalink: /note/Heisenberg-Picture/
---
In the Heisenberg picture, states do not evolve in time, operators do.
The transformation from the [[Schrodinger Picture]] to the Heisenberg picture is
$$
\ket{ \psi }_H = e^{ iHt }\ket{ \psi,t }_S,
$$
$$
\mathcal{O}_H(t) = e^{ iHt }\mathcal{O}_Se^{ -iHt }.
$$
Operators evolve as
$$
i \partial_t \mathcal{O}_H(t) = \left[ \mathcal{O}_H(t), H \right].
$$
