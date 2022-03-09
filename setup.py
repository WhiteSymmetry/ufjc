from distutils.core import setup


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='ufjc',
    packages=['ufjc'],
    version='1.0.1',
    description='The Python package for the uFJC single-chain model.',
    long_description=read("README.rst"),
    author='Michael R. Buche, Scott J. Grutzik',
    author_email='mrbuche@sandia.gov, sjgrutz@sandia.gov',
    url='https://sandialabs.github.io/ufjc',
    license='BSD-3-Clause',
    keywords=['ufjc', 'polymers', 'statistical mechanics', 'thermodynamics'],
    install_requires=['numpy', 'scipy'],
    extras_require={
      'docs': ['anybadge', 'colorama', 'matplotlib', 'pycodestyle',
               'sphinx', 'sphinx-rtd-theme', 'sphinxcontrib-bibtex'],
      'plotting': ['matplotlib'],
      'testing': ['colorama', 'matplotlib', 'pycodestyle',
                  'pytest', 'pytest-cov']},
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    project_urls={
      'Anaconda': 'https://anaconda.org/mrbuche/ufjc',
      'Documentation': 'https://sandialabs.github.io/ufjc',
      'GitHub': 'https://github.com/sandialabs/ufjc',
      'Issues': 'https://github.com/sandialabs/ufjc/issues',
    },
)