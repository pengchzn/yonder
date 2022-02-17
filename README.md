# POPCORN
A **P**yth**O**n **P**a**C**kage for n**O**isy data **R**eductio**N**

` POPCORN` is a program that uses singular value decomposition to do low-rank data denoising and reconstruction. ` POPCORN` takes a tabular data matrix and an error matrix as input and returns a denoised version of the original dataset as output. In most test instances, the approach is more accurate and efficient when used on a wide range of tests with varying amounts of contamination. As a result, it may simply be applied to astronomical research, assisting in the data cleaning process.

You can get the docs on POPCORN here![give the link of the docs]

# Install

The package can be installed via the PyPI and pip:

    pip install popcorn

If you download the repository, you can also install it in the popcorn directory:

    python setup.py install

# Usage

    import popcorn

    # get the denoised data
    data = popcorn(X,Xsd)


# Example

[take a simple example, easy contamination, add the noise manually and denoise it with the package]

[Put the Code, the plot here]

You can test it in this [notebook](https://github.com/pengchen1019/popcorn/blob/main/tests/test_popcorn.ipynb) by yourself!

# Benchmark

[Compared with the Standard PCA or other algorithms]


# Requirements

- python 3
- numpy >= 1.21.0
- Scipy >= 1.7.0
- scikit_learn >= 1.0.2

# License

The GPL License

# References
