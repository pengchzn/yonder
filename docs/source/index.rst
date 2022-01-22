MLPCA
=====

Fancyname: A package for data-denoising via uncertainty aware Principal
ComponentsAnalysis[the link of the paper]

-  Outperforming the robust Gaussian process with Student-𝑡likelihood
   significantly in many test cases
-  Easy to implement and computationally tractable

``MLPCA`` is a package which can do the data-denoising via uncertainty,
using the singular value decomposition(SVD)

Install
=====
The package can be installed via the PyPI and pip:

::

   pip install mlpca

If you download the repository, you can also install in the mlpca
directory:

::

   python setup.py install

Usage
=====

::

   from mlpca import MlPCA

   # get the denoised data
   data = MLPCA(X,Xsd)

Example
=======

One example can start in this
`notebook <https://github.com/pengchen1019/MLPCA/blob/main/tests/test_mlpca.ipynb>`__.

Requirements
============

-  python 3.7
-  numpy >= 1.21.0
-  Scipy >= 1.7.0
-  scikit_learn >= 1.0.2 

License 
=======

The MIT License

References
==========
