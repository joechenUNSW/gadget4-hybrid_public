

GADGET-4-hybrid
========

Standard GADGET-4
========

![](documentation/img/top.jpg)

GADGET-4 is a massively parallel code for N-body/hydrodynamical
cosmological simulations. It is a flexible code that can be applied to
a variety of different types of simulations, offering a number of
sophisticated simulation algorithms.  An account of the numerical
algorithms employed by the code is given in the original code paper,
subsequent publications, and this documentation.

GADGET-4 was written mainly by
[Volker Springel](mailto:vspringel@mpa-garching.mpg.de), with
important contributions and suggestions being made by numerous people,
including [Ruediger Pakmor](mailto:rpakmor@mpa-garching.mpg.de),
[Oliver Zier](mailto:ozier@mpa-garching.mpg.de), and
[Martin Reinecke](mailto:martin@mpa-garching.mpg.de).

For documentation of the code as well as the code paper, please refer
to the [code's web-site](https://wwwmpa.mpa-garching.mpg.de/gadget4).


Neutrinos
=============
Hybrid neutrinos are implemented by Joe Zhiyu Chen. Linear response neutrinos implemented as described in papers [arXiv:2011.12503](https://arxiv.org/abs/2011.12503) and [arXiv:2011.12504](https://arxiv.org/abs/2011.12504). Paper to describe the hybrid implementation is in preparation.

To generate accurate initial conditions for neutrino linear response, a scaled-back input power spectrum taking neutrinos into account is necessary. This can be obtained with the [MuFLR code](https://github.com/upadhye/MuFLR).

Input files for restarting can be prepared easily with the restart\_preparation.py (when converting a single stream) and restart\_preparation\_multi.py (when converting multiple streams) scripts. Scripts prepared by Markus Mosbech.

Fully updated documentation for the changes to base Gadget parameters is in the works.
