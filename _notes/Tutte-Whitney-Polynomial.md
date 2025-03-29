---
tags:
  - Graph-Theory
collection: notes
title: "Tutte-Whitney Polynomial"
permalink: /note/Tutte-Whitney-Polynomial/
---
The Tutte polynomial of a [[Graph]] $G$ is 
$$
T(G,x,y) = \sum_{G' \subseteq G} (x-1)^{k(G')-k(G)}(y-1)^{c(G')} = \sum_{G' \subseteq G} (x-1)^{k(G') - k(G)}(y-1)^{e(G')+k(G')-n(G')},
$$
$G'$ spanning subgraphs of $G$, $k(G')$ the number of components of $G'$, $c(G')$ the number of linearly independent cycles.

Provides a way of counting various types of subgraphs:
Setting $x=1$ restricts to only connected subgraphs, because $k(G') = k(G)$ is necessary for nonzero contributions by $G'$. Similarly, setting $y=1$ restricts to cycle-free subgraphs. Setting $x=y=1$ restricts to spanning trees. Setting $x=2$ and $y=1$ counts the number of spanning forests. Setting $x=1$ and $y=2$ counts the number of connected spanning subgraphs of $G$.

Although always a polynomial, many graphs end up having their Tutte polynomial expressed as a function with a $1/(x-1)$ prefactor, which is sometimes preferable. The prefactor can always be cancelled to get a polynomial. 

The [[Chromatic Polynomial]] is a special case of the Tutte polynomial: 
$$
P(G,q) = (-q)^{k(G)}(-1)^{n(G)}T(G,1-q,0).
$$

The Tutte polynomial is related to the partition function of the [[Potts Model]] as
$$
T\left( G, 1+\frac{q}{v},1+v \right) 
= \left( \frac{q}{v} \right)^{-k(G)} v^{-n(G)} Z(G,q,v), 
$$
$$
Z(G,q,v) = \left( \frac{q}{v} \right)^{k(G)} v^{n(G)} T\left( G,1+\frac{q}{v}, 1+v \right).
$$
This implies that the Tutte polynomial obeys a [[Deletion-Contraction Relation]]:
$$
\begin{align*}
Z(G,q,v) &= Z(G-e,q,v) + vZ(G/e,q,v) \\
\left( \frac{q}{v} \right)^{k(G)} v^{n(G)} T\left( G,1+\frac{q}{v}, 1+v \right) &= \left( \frac{q}{v} \right)^{k(G-e)} v^{n(G-e)} T\left( G-e\right) + v \left( \frac{q}{v} \right)^{k(G/e)} v^{n(G/e)} T\left( G/e\right) \\
T\left( G,1+\frac{q}{v}, 1+v \right) &= \left( \frac{q}{v} \right)^{k(G-e) - k(G)} v^{n(G-e) - n(G)} T(G-e) + \left( \frac{q}{v} \right)^{k(G/e) - k(G)} v^{1 + n(G/e) - n(G)}T(G/e) \\
&= \left( \frac{q}{v} \right)^{k(G-e) - k(G)} T(G-e) + \left( \frac{q}{v} \right)^{k(G/e) - k(G)} T(G/e)
\end{align*}
$$
If $e$ is not a bridge, then $k(G-e) = k(G)$. If $e$ is not a loop, as is usually the case for physical systems, then $k(G/e) = k(G)$. In that case, the relation is simply
$$
T(G,x,y) = T(G-e,x,y) + T(G/e,x,y).
$$
