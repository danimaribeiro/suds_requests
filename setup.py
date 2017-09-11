from setuptools import setup, find_packages


setup(
    name='suds-jurko-requests',
    version='1.0',
    description=open('README.rst').read(),
    author='Jason Michalski',
    author_email='armooo@armooo.net',
    packages=find_packages(exclude=['*test*']),
    install_requires=['requests', 'suds-jurko'],
    keywords=['suds', 'jurko'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
