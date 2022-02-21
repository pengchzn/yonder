=======
POPCORN
=======

*A PythOn PaCkage for nOisy data ReductioN*

You can get the docs of POPCORN here! [give the link of the docs]

``POPCORN`` is a package that uses singular value decomposition to do
low-rank data denoising and reconstruction. ``POPCORN`` takes a tabular
data matrix and an error matrix as input and returns a denoised version
of the original dataset as output. In most test instances, the approach
is more accurate and efficient when used on a wide range of tests with
varying amounts of contamination. As a consequence, it may easily be 
used to astronomical research to help with data cleaning.


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
==================

Here is an easy example for the use of ``POPCORN``

::

   import popcorn
   import numpy as np

   #use numpy to import the data
   X = np.loadtxt('./Xobs.csv',delimiter=",",skiprows=1)
   Xsd = np.loadtxt('./Xsd.csv',delimiter=",",skiprows=1)

   # put the data into the algorithm
   # Get the value
   U, S, V = popcorn(X, Xsd, 2)
   
   # Get the denoised data
   result = U @ S @ V.T

After the "POPCORN" procedure, you can connect any additional algorithms or models to the denoised date.

In our test example, the result of the visualization is shown in the figure below:

<LINK>

You can test the test example in this `notebook <https://github.com/pengchzn/popcorn/blob/main/tests/test_popcorn.ipynb>`_ locally by yourself!

If you are new to Python or don't know how to run ``POPCORN`` locally, you can click `here <https://colab.research.google.com/drive/1nT4M90_VE-lX0L9d_XPg70QOTkuVbAZO?usp=sharing>`_ to create a new Colaboratory notebook, so you can run ``POPCORN`` in the cloud!


Requirements
============

-  python 3
-  numpy >= 1.21.0
-  Scipy >= 1.7.0

``Popcorn`` primarily uses the most recent version of ``Scipy`` for single value decomposition. 
Make sure your ``Scipy`` installation is up to date before using ``popcorn``.


License
=======

The GPL License

References
==========
- Harris, C. R., Millman, K. J., van der Walt, S. J., et al.2020, Nature, 585, 357, doi: `10.1038/s41586-020-2649-2 <http://doi.org/10.1038/s41586-020-2649-2>`_

- Kelly, B. C. 2007, ApJ, 665, 1489, doi: 10.1086/519947

- Virtanen, P., Gommers, R., Oliphant, T. E., et al. 2020,Nature Methods, 17, 261, doi: `10.1038/s41592-019-0686-2 <http://doi.org/10.1038/s41592-019-0686-2>`_

- Wentzell, P. D., & Hou, S. 2012, Journal of Chemometrics,26, 264, doi: https://doi.org/10.1002/cem.2428

- Wentzell, P. D., & Lohnes, M. T. 1999, Chemometrics andIntelligent Laboratory Systems, 45, 65,doi: http://doi.org/https://doi.org/10.1016/S0169-7439(98)00090-2

- Reis, I., Baron, D., & Shahaf, S. 2018, The AstronomicalJournal, 157, 16, doi: `10.3847/1538-3881/aaf101<http://doi.org/10.3847/1538-3881/aaf101>`_
