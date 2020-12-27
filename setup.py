from setuptools import setup

setup(
    name='python-ml-dali',
    version='0.0.1',
    url='https://github.com/benoitdepaire/python-ml-dali',
    license='GNU GPLv3',
    author='Benoît Depaire',
    install_requires=[],
    author_email='benoit@depaire.net',
    description='A Python library to communicate with Dali controllers from Ministry of Light',
    long_description='Here comes the long description',
    packages=['python-ml-dali'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)d",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]

)