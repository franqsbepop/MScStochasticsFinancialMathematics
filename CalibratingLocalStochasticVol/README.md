# Abstract of master research thesis  titled "Calibration of Local Stochastic Volatility models in a conic finance setting using Artificial Neural Networks"
By Diogo Franquinho

In this thesis, we study the calibration of Local Stochastic Volatility (LSV) models using
artificial neural networks, building upon prior work by C. Cuchiero, W. Khosrawi, and J.
Teichmann. “A generative adversarial network approach to calibration of local stochastic
volatility models”. In: Risks 8.4 (2020), p. 101. The proposed method approximates
the map between market prices and model parameters by using a feed-forward neural
network to approximate the local volatility component in our model. The method allows
us to circumvent the computation of Dupire’s formula and avoid the interpolation of the
volatility surface. We extend the prior work from the one-price setting to the two-
price setting, using the conic finance framework. This allows us to consider only the
information available in the market and derive calibrated bid and ask prices. Our method
is evaluated through a numerical analysis that involves calibrating it with real market
data and comparing the results against a benchmark model and method.


# The code provided builds on the work of "Deep  Calibration of Local Stochastic Volatility models "

Authors: Christa Cuchiero (University of Vienna), [Homepage](https://www.mat.univie.ac.at/~cuchiero/)
Wahid Khosrawi (ETH Zurich), [Homepage](https://people.math.ethz.ch/~kwahid/)
Josef Teichmann (ETH Zurich), [Homepage](https://people.math.ethz.ch/~jteichma/)
This is the repo corresponding to the paper:
[A Generative Adversarial Network Approach to Calibration of Local Stochastic Volatility Models](https://www.mdpi.com/2227-9091/8/4/101)
For citations:\
**MDPI and ACS Style**\
Cuchiero, C.; Khosrawi, W.; Teichmann, J. A Generative Adversarial Network Approach to Calibration of Local Stochastic Volatility Models. Risks **2020**, 8(4), 101.
```
@Article{cuchiero2020generative,
  author    = {Cuchiero, Christa and Khosrawi, Wahid and Teichmann, Josef},
  title     = {A Generative Adversarial Network Approach to Calibration of Local Stochastic Volatility Models},
  journal   = {Risks},
  year      = {2020},
  volume    = {8},
  number    = {4},
  pages     = {101},
  doi       = {10.3390/risks8040101},
  keywords  = {LSV calibration; neural SDEs; generative adversarial networks; deep hedging; variance reduction; stochastic optimization},
  publisher = {MDPI},
  url       = {https://www.mdpi.com/2227-9091/8/4/101},
}
```



## Documentation 
Will follow in the near future (this version requires tensorflow 1.13 and python 3)
If the environment is set up correctly, the following command should start all computations needed for the statistical test described in the paper:
```console
user@host:~$ python3 stat_test.py
```



## License
 
MIT License
Copyright (c) 2020 Christa Cuchiero, Wahid Khosrawi, Josef Teichmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
