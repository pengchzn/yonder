=======
POPCORN
=======

*A PythOn PaCkage for nOisy data ReductioN*

Main paper：`J-PLUS: A catalogue of globular cluster candidates around the M81/M82/NGC3077 triplet of galaxies <https://arxiv.org/abs/2202.11472>`_

You can get the docs of POPCORN here! [give the link of the docs]

``POPCORN`` is a package that uses singular value decomposition to perform
low-rank data denoising and reconstruction. It takes a tabular
data matrix and an error matrix as input and returns a denoised version
of the original dataset as output. The approach enables a more accurate data analysis with a wide range of uncertainties. 
Consequently, this package can be used as a simple toolbox to perform astronomical data cleaning.


How to install ``POPCORN``
==========================

The ``POPCORN`` can be installed via the PyPI and pip:

::

   pip install popcorn

If you download the repository, you can also install it in the ``popcorn`` directory:

::

   git clone https://github.com/pengchzn/popcorn
   cd popcorn
   python setup.py install

How to use ``POPCORN``
======================

Here is an easy example for the use of ``POPCORN``

::

   import popcorn
   import numpy as np

   #import the data
   X = pd.read_csv('./datasets/Xobs.csv')
   Xsd = pd.read_csv('./datasets/Xsd.csv')

   # put the data into the algorithm
   # Get the value
   U, S, V = popcorn(X, Xsd, 2)
   
   # Get the denoised data
   result = U @ S @ V.T

After the ``POPCORN`` procedure, you can connect any additional algorithms or models to the denoised data.

Here is the distribution of noisy data and the distribution of denoised data in our test case:

.. image:: https://github.com/pengchzn/popcorn/blob/main/tests/figures/Noisy_data.png

.. image:: https://github.com/pengchzn/popcorn/blob/main/tests/figures/Denoised_data.png

We also mimic how the data is used on a daily basis, run the HDBScan on both sets of data, and visualize the findings.

.. image:: https://github.com/pengchzn/popcorn/blob/main/tests/figures/classification.png


You can test the test example in this `notebook <https://github.com/pengchzn/popcorn/blob/main/tests/test_popcorn.ipynb>`_ locally by yourself! If you are new to Python or don't know how to run ``POPCORN`` locally, you can click `here <https://colab.research.google.com/drive/1nT4M90_VE-lX0L9d_XPg70QOTkuVbAZO?usp=sharing>`_ to create a new Colaboratory notebook, so you can run ``POPCORN`` in the cloud!


Requirements
============

-  python 3
-  numpy >= 1.21.0
-  Scipy >= 1.7.0

``Popcorn`` primarily uses the most recent version of ``Scipy`` for single value decomposition. 
Make sure your ``Scipy`` installation is up to date before using ``popcorn``.


Copyright & License
=======
2021 Peng Chen (pengchzn@gmail.com) & Rafael S. de Souza (drsouza@shao.ac.cn)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

References
==========


- Harris, C. R., Millman, K. J., van der Walt, S. J., et al.2020, Nature, 585, 357, doi: `10.1038/s41586-020-2649-2 <http://doi.org/10.1038/s41586-020-2649-2>`_

- Kelly, B. C. 2007, ApJ, 665, 1489, doi: 10.1086/519947

- Virtanen, P., Gommers, R., Oliphant, T. E., et al. 2020,Nature Methods, 17, 261, doi: `10.1038/s41592-019-0686-2 <http://doi.org/10.1038/s41592-019-0686-2>`_

- Wentzell, P. D., & Hou, S. 2012, Journal of Chemometrics,26, 264, doi: https://doi.org/10.1002/cem.2428

- Wentzell, P. D., & Lohnes, M. T. 1999, Chemometrics andIntelligent Laboratory Systems, 45, 65,doi: http://doi.org/https://doi.org/10.1016/S0169-7439(98)00090-2

- Reis, I., Baron, D., & Shahaf, S. 2018, The AstronomicalJournal, 157, 16, doi: `10.3847/1538-3881/aaf101 <http://doi.org/10.3847/1538-3881/aaf101>`_
