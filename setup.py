# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="fdemmer-django-ace",
    version="1.1.0",
    description="django-ace provides integration for ajax.org ACE with Django",
    long_description=open("README.rst").read(),
    author="Florian Demmer",
    author_email="fdemmer@gmail.com",
    license="Simplified BSD",
    url="https://github.com/fdemmer/django-ace",
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    setup_requires=['wheel'],
    install_requires=["Django>1.11,<4.0"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    options={'bdist_wheel': {'universal': '1'}},
)
