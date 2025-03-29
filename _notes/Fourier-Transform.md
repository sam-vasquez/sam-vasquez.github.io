---
tags:
  - Reference
collection: notes
title: "Fourier Transform"
permalink: /note/Fourier-Transform/
---
In terms of the angular frequency $\omega = 2\pi \xi$, the Fourier transform is
$$
\hat{f}(\omega) = \int_{-\infty}^\infty dt \; f(t) e^{ -i \omega t },
$$
$$
f(t) = \frac{1}{2\pi}\int_{-\infty}^\infty d\omega \; \hat{f}(\omega) e^{ i\omega t }.
$$
Sometimes the factor of $2\pi$ is split between $\hat{f}$ and $f$ to restore symmetry and unitarity:
$$
\hat{f}(\omega) = \frac{1}{\sqrt{ 2 \pi}} \int_{-\infty}^\infty dt \; f(t) e^{ -i \omega t },
$$
$$
f(t) = \frac{1}{\sqrt{ 2\pi }}\int_{-\infty}^\infty d\omega \; \hat{f}(\omega) e^{ i\omega t }.
$$

Its discrete version is
$$
\hat{y}_k = \frac{1}{\sqrt{ N }} \sum_{n=0}^{N-1} x_n e^{ i2\pi \frac{nk}{N}},
$$
$$
x_n = \frac{1}{\sqrt{ N }} \sum_{k=0}^{N-1} \hat{y}_k e^{ -i2\pi \frac{nk}{N}}.
$$

See Woit chapter 11 for the representation theory perspective.
This leads to a natural generalization of the Fourier transform to functions on groups, where these Fourier transforms are the $\mathbb{R}$ and $\mathbb{Z}/N$ cases respectively.


Notable properties:
Each derivative $\frac{d}{dt}$ of $f(t)$ multiplies by a factor of $i\omega$: $\dot{f}(t) = i\omega f(t)$.
[[Parseval's Theorem]]
[[Convolution Theorem]]