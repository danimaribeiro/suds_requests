from setuptools import setup


setup(
    name='suds-jurko-requests',
    version='0.1',
    description=open('README.rst').read(),
    author='Jason Michalski',
    author_email='armooo@armooo.net',
    py_modules=['suds_requests'],
    install_requires=['requests', 'suds-jurko'],
)
