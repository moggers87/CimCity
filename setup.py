from setuptools import setup


setup(
    name="CimCity",
    version="0.0.1",
    description="A city simulator",
    author="Jessica Tallon & Matt Molyneaux",
    license="GPLv3+",
    url="https://github.com/moggers87/CimCity",
    packages=["cim", "cim.items"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Simulation",
    ],
    entry_points={
        "console_scripts": ["cim = cim:run"],
    },
    test_suite="cim.tests",
)
