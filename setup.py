import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name='fancyname',
    version='x.x',
    description='A package for data-denoising via uncertainty aware Principal ComponentsAnalysis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    keywords=['data-denoising', 'Principal ComponentsAnalysis'],
    author='',
    author_email='',
    packages=setuptools.find_packages(),
    classifiers=[
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)