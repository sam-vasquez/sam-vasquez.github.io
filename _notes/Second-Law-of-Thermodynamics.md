---
collection: notes
title: "Second Law of Thermodynamics"
permalink: /note/Second-Law-of-Thermodynamics/
---
The second law of thermodynamics has many equivalent statements.

From the [[State Variable]] point of view, one statement is that there exists an [[Extensive and Intensive State Variables|extensive]] function $S$ of all other state variables, such that:
1. $S$ is monotonically increasing with energy $U$.
2. Whenever equilibrium state $B$ is [[Adiabatic Process|adiabatically accessible]] from equilibrium state $A$, $S(B) \geq S(A)$.
We call this function $S$ [[Entropy|entropy]].

In particular, during a process that is both [[Reversible Thermodynamic Process|reversible]] and adiabatic, we would have that $S(B) \geq S(A)$ and $S(A) \geq S(B)$, and therefore $S(A) = S(B)$. This fact that no change in heat results in no change in entropy for reversible processes, would be suggestive of a connection between changes in heat and changes in entropy.

Indeed, [[Heat-Entropy Relation|it can be shown]] using the [[Notes/First Law of Thermodynamics]] that during reversible processes, $S$ must be related to heat by $\delta Q|_{rev} = T dS$, where $\frac{1}{T} = \left( \frac{\partial S}{\partial U} \right)_{\mathbf{X}} > 0$ is a parameter called [[Temperature]]. Therefore, the first and second laws combine to give the [[Thermodynamic Identity]], $dU = T dS + f \cdot dX$, justifying $U$ as a proper state variable.

However, it must be stressed that heat does not necessarily need to be expressed as a differential of entropy for non-reversible processes. This is what allows for the second axiom of the second law to be an inequality instead of an equality.

This statement of the second law is also equivalent to the [[Entropy Maximization Principle]], and by corollary, the [[Energy Minimization Principles]]. This statement would be that with energy and all other extensive variables equal, the equilibrium state of a thermodynamic system is the state with all internal configurations such that entropy is maximized. 

From the statistical point of view, an equivalent statement of the second law is that all state variables of a given equilibrium state are given by an average over all microscopic states on the energy surface.

On the dynamical energy surface, single points refer to different arrangements of particle positions and momenta, but almost every point is macroscopically indistinguishable, and almost every point has the macroscopic properties of thermal equilibrium. This motivates the interpretation 

This law is the foundation for defining a [[Density of States]] that characterizes the number of microstates at a given energy and allow to compute averages over these microstates to get macroscopic properties. It also connects [[Entropy]] to its interpretation as a measure of statistical information entropy.