import setuptools

with open('README.rst', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name='yonder',
    version='1.0',
    description='A python package for data denoising and reconstruction',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/pengchzn/yonder',
    keywords=['Astrostatistics techniques', 'Astronomy software', 'Astronomy data analysis'],
    author='Peng Chen',
    author_email='pengchzn@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3',
    ],
)
