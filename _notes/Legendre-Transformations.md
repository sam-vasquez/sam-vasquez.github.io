---
collection: notes
title: "Legendre Transformations"
permalink: /note/Legendre-Transformations/
---
For canonical momenta $p_i = \frac{\partial \mathcal{L}}{\partial \dot{q_i}}$, 
$$
\mathcal{H}(p_i,q_i,t) = \sum_i p_i \dot{q}^i - \mathcal{L}.
$$
Legendre transform of convex function is also convex.

Efficient calculation process:
- Calculate canonical momenta $p(q,\dot{q},t)$.
- Solve for $\dot{q}(p,q,t)$.
- Solve for $\mathcal{L}(p,q,t)$.
- Plug $q(p,q,t)$ and $\mathcal{L}(p,q,t)$ into definition of $\mathcal{H}$.
