# POPCORN

*A **P**yth**O**n **P**a**C**kage for n**O**isy data **R**eductio****N***

` POPCORN` is a program that uses singular value decomposition to do low-rank data denoising and
reconstruction. ` POPCORN` takes a tabular data matrix and an error matrix as input and returns a denoised version of
the original dataset as output. In most test instances, the approach is more accurate and efficient when used on a wide
range of tests with varying amounts of contamination. As a result, it may simply be applied to astronomical research,
assisting in the data cleaning process.

Get the docs of POPCORN here![give the link of the docs]

# How to install POPCORN

The `POPCORN` can be installed via the PyPI and pip:

```
pip install popcorn
```

If you download the repository, you can also install it in the popcorn directory:

```
git clone https://github.com/pengchen1019/popcorn
cd popcorn
python setup.py install
```

# How to use POPCORN

```
import popcorn

# get the denoised data
data = popcorn(X,Xsd)
```

# Example

[take a simple example, easy contamination, add the noise manually and denoise it with the package]

[Put the Code, the plot here]

You can test it in this [notebook](https://github.com/pengchen1019/popcorn/blob/main/tests/test_popcorn.ipynb) by
yourself!

# Requirements

- python 3
- numpy >= 1.21.0
- Scipy >= 1.7.0

# License

The GPL License

# References
