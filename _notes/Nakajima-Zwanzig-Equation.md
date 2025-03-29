---
tags:
  - Quantum
collection: notes
title: "Nakajima-Zwanzig Equation"
permalink: /note/Nakajima-Zwanzig-Equation/
---
Closed equation for the time evolution of an open system. Following the discussion in [[Projection Operator Dynamics]].

Definitions of density matrix operators:
$$
\mathcal{L}(t) (\cdot) \equiv -i \left[ V_I(t), \cdot \right]
$$
$$
\mathcal{P}(\cdot) \equiv \textrm{Tr}_B(\cdot) \otimes \rho_B.
$$

In the interaction picture, the density matrix evolves as
$$
i \partial_t \rho_I(t) = i \alpha \left[ V_I(t), \rho_I(t) \right] = i \alpha \mathcal{L}(t) \rho_I(t).
$$
From now on, suppress interaction picture label $I$.

Project both sides of the time evolution equation with $\mathcal{P}$ and $1 - \mathcal{P} \equiv \mathcal{Q}$:

$$
\mathcal{P} \partial_t \rho(t) = \alpha \mathcal{P} \mathcal{L}(t) \rho(t),
$$
$$
\mathcal{Q} \partial_t \rho(t) = \alpha \mathcal{Q} \mathcal{L}(t) \rho(t).
$$
Note that when the reference state $\rho_B$ is time independent, projection and time derivative commute:
$$
\partial_t (\mathcal{P} \rho(t)) = \alpha \mathcal{P} \mathcal{L}(t) \mathcal{\rho}(t),
$$
$$
\partial_t (\mathcal{Q} \rho(t)) = \alpha \mathcal{Q} \mathcal{L}(t) \rho(t).
$$
Insert $\mathcal{P} + \mathcal{Q} = I$ between $\mathcal{L}$ and $\rho$ to separate the equations:
$$
\partial_t (\mathcal{P} \rho(t)) = \alpha \mathcal{P} \mathcal{L}(t) (\mathcal{P} \rho(t)) + \alpha \mathcal{P} \mathcal{L}(t) (\mathcal{Q} \rho(t)) ,
$$
$$
\partial_t (\mathcal{Q} \rho(t)) = \alpha \mathcal{Q} \mathcal{L}(t) (\mathcal{P}\rho(t)) + \alpha \mathcal{Q} \mathcal{L}(t) (\mathcal{Q}\rho(t)).
$$
Now that we have differential equations for $\mathcal{P}\rho$ and $\mathcal{Q}\rho$, we can solve for $(\mathcal{Q}\rho)(t)$ and use that solution to solve for $(\mathcal{P}\rho)(t)$. 

The formal solution for $\mathcal{Q}\rho$ is
$$
\mathcal{Q}\rho(t) = \mathcal{G}(t,t_0) \mathcal{Q}\rho(t_0) + \alpha \int_{t_0}^t dt' \mathcal{G}(t,t') \mathcal{Q} \mathcal{L}(t') \mathcal{P}\rho(t'),
$$
where $\mathcal{G}$ is the [[Green's Function]] of $\partial_t - \alpha \mathcal{Q} \mathcal{L}(t)$:
$$
\mathcal{G}(t,t') \equiv \mathcal{T} \exp \left[ \alpha \int_{t'}^t dt'' \mathcal{Q} \mathcal{L}(t'') \right],
$$
or explicitly,
$$
\mathcal{G}(t,t')(\cdot) = \mathcal{T} \exp \left[ -i \alpha \int_{t'}^t dt'' \left( \left[ V(t''), \cdot \right] - \textrm{Tr}_B\left( \left[ V(t''), \cdot \right] \right) \otimes \rho_B \right) \right]
$$
$$
= \mathcal{T} \exp \left[ -i \alpha \int_{t'}^t  dt'' \left[ V(t''), \cdot \right] \right],
$$
by assumption that odd moments of the interaction energy in the bath vanish. 
The propagator satisfies
$$
\partial_t \mathcal{G}(t,t') = \alpha \mathcal{Q} \mathcal{L}(t) \mathcal{G}(t,t'),
$$
with initial condition $\mathcal{G}(t,t) = I$.
(Todo: better understand the boundary conditions of this differential equation for $\mathcal{Q}\rho$.)

The differential equation for $\mathcal{P}\rho$ becomes
$$
\partial_t (\mathcal{P}\rho)(t) = \alpha \mathcal{P} \mathcal{L}(t) \mathcal{G}(t,t_0) \mathcal{Q} \rho(t_0) + \alpha \mathcal{P} \mathcal{L}(t) (\mathcal{P}\rho)(t)
$$
$$
+ \alpha^2 \int_{t_0}^t dt' \mathcal{P} \mathcal{L}(t) \mathcal{G}(t,t') \mathcal{Q} \mathcal{L}(t') \mathcal{P} \rho(t').
$$
The first term is an inhomogeneous term depending on initial conditions at time $t_0$.
By assumption that odd moments of the interaction energy in the bath vanish, the second term vanishes. 
The third term is an integral over the past history of the system, encoding the non-Markovian memory of the dynamics. It can be rewritten using a memory kernel $\mathcal{K}$,
$$
\partial_t (\mathcal{P}\rho)(t) = \alpha \mathcal{P} \mathcal{L}(t) \mathcal{G}(t,t_0) \mathcal{Q} \rho(t_0) + \int_{t_0}^t dt' \mathcal{K}(t, t') \mathcal{P} \rho(t'),
$$
$$
\mathcal{K}(t,t') \equiv \alpha^2 \mathcal{P} \mathcal{L}(t) \mathcal{G}(t,t') \mathcal{Q} \mathcal{L}(t') \mathcal{P}.
$$
This is the Nakajima-Zwanzig equation.

It usually has to be solved by expanding $\mathcal{K}$ either in powers of $\alpha$ or in powers of $t-t'$. The former is traditional perturbation theory of the interaction Hamiltonian with weak coupling, the latter is an expansion for short memory time around $\mathcal{K}(t,t') \approx \delta(t - t')$, where the system is nearly memoryless.

An initial condition $\rho(t_0) = \rho_A(t_0) \otimes \rho_B \implies \mathcal{P}\rho(t_0) = \rho(t_0) \implies \mathcal{Q}\rho(t_0) = 0$ removes the inhomogeneous term, leaving just
$$
\partial_t (\mathcal{P}\rho)(t) = \int_{t_0}^t dt' \mathcal{K}(t, t') \mathcal{P} \rho(t').
$$
To second order in $\alpha$, this becomes 
$$
\partial_t \rho_A(t) = -\alpha^2 \int_{t_0}^t dt' \textrm{Tr}_B \left[ V(t), \left[ V(t'), \rho_A(t') \otimes \rho_B \right] \right],
$$
which matches the Born approximation. See [[Open Quantum Systems]] eqn 3.116.

The [[Time-Convolutionless Projection Operator Method]] method uses perturbation theory in $\alpha$ to remove dependence on the memory kernel and get an expression that is local in time.