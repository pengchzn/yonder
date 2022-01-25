XX
=====

XX: A package for data-denoising via uncertainty aware singular value decomposition[the link of the paper]

-  Outperforming the robust Gaussian process with Student-𝑡likelihood
   significantly in many test cases
-  Easy to implement and computationally tractable

``XX`` is a package which can do the data-denoising via uncertainty, using the singular value decomposition(SVD). It iteratively does the SVD with the errors-in-measurements, thus denoising the data, and can avoid the bias during the data processing. Applied to a wide range of experiments with different contamination levels, the method is more accurate and efficient in most test cases. So it also can be easily applied to astrophysical study, helping clean the data.

Install
=======
The package can be installed via the PyPI and pip:

::

   pip install XX

If you download the repository, you can also install it in the XX directory:

::

   python setup.py install

Usage
=====

::

   from XX import XX

   # get the denoised data
   data = MLPCA(X,Xsd)

Example
=======

[take a simple example, easy contamination, add the noise manually and denoise it with the package]

[Put the Code, the plot here]

You can test it in this `notebook <https://github.com/pengchen1019/MLPCA/blob/main/tests/test_mlpca.ipynb>`__ by yourself!


Benchmark
=========

[Compared with the Standard PCA or other algorithms]

Requirements
============

-  python 3.7
-  numpy >= 1.21.0
-  Scipy >= 1.7.0
-  scikit_learn >= 1.0.2 

License 
============

The MIT License

References
==========
