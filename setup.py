import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name='popcorn',
    version='0.1',
    description='A PythOn PaCkage for nOisy data ReductioN',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/pengchzn/popcorn',
    keywords=['data-denoising', 'Principal ComponentsAnalysis'],
    author='Rafael S. de Souza, Peng Chen',
    author_email='drsouza@shao.ac.cn, pengchzn@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python :: 3',
    ],
)
