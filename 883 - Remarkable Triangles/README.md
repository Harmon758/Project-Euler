[Problem 883](https://projecteuler.net/problem=883): Remarkable Triangles
=========================================================================

In this problem we consider triangles drawn on a **hexagonal lattice**, where
each lattice point in the plane has six neighbouring points equally spaced
around it, all distance $1$ away.

We call a triangle *remarkable* if

- All three vertices and its **incentre** lie on lattice points
- At least one of its angles is $60^\circ$

<img src="Project%20Euler%20Problem%20883%20Image.png" alt="diagram">

Above are four examples of remarkable triangles, with $60^\circ$ angles
illustrated in red. Triangles A and B have inradius $1$; C has inradius
$\sqrt{3}$; D has inradius $2$.

Define $T(r)$ to be the number of remarkable triangles with inradius $\le r$.
Rotations and reflections, such as triangles A and B above, are counted
separately; however direct translations are not. That is, the same triangle
drawn in different positions of the lattice is only counted once.

You are given $T(0.5) = 2$, $T(2) = 44$, and $T(10) = 1302$.

Find $T(10^6)$.
