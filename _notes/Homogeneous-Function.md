---
tags:
  - Math
  - Reference
collection: notes
title: "Homogeneous Function"
permalink: /note/Homogeneous-Function/
---
A function $f(x_1,\ldots,x_n)$ is homogeneous with degree $p$ if 
$$
f(\lambda x_1,\ldots,\lambda x_n) = \lambda^p f(x_1,\ldots,x_n).
$$
$f(x_1,\ldots,x_n)$ is generalized homogeneous if there exist powers $a_1,\ldots,a_n$, $b$, such that
$$
f(\lambda^{a_1}x_1, \ldots, \lambda^{a_n}x_n) = \lambda^b f(x_1,\ldots,x_n).
$$
The exponent $b$ can be absorbed into the exponents $a_i$.

An important property of a generalized homogeneous function of two variables $f(x,y)$ is as follows:
Given that $f(\lambda^a x, \lambda^b y) = \lambda f(x,y)$, choose $\lambda = y^{-1/b}$:
$$
f(y^{-a/b}x, 1) = y^{-1/b} f(x,y).
$$
This implies 
$$
f(x,y) = y^{1/b} f\left( \frac{x}{y^{a/b}}, 1 \right) \equiv y^{1/b} g(z).
$$
By a similar construction,
$$
f(x,y) = x^{1/a} f\left( 1, \frac{y}{x^{b/a}} \right).
$$

So any generalized homogeneous function of two variables can be rewritten as a prefactor times a function of one variable. This has the following important implication for differential equations: For equation
$$
f(x,y) \frac{dy}{dx} + g(x,y) = 0,
$$
if both $f$ and $g$ have the same degrees $a$ and $b$, then the equation becomes 
$$
x^{1/a} f\left( 1, \frac{y}{x^{b/a}} \right) \frac{dy}{dx} + x^{1/a} g\left( 1, \frac{y}{x^{b/a}} \right) = 0,
$$
and the substitution $v = \frac{y}{x^{b/a}}$ yields
$$
x^{(b+1)/a} f(1,v) \frac{dv}{dx} + x^{1/a} g(1,v) = 0,
$$
or equivalently,
$$
\frac{f(1,v)}{g(1,v)} \frac{dv}{dx} = -x^{-b/a}.
$$
So generalized homogeneous functions yield separable differential equations.