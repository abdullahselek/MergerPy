.. mergerpy documentation master file, created by

Contents:
 
Welcome to mergerpy's documentation!
====================================
**A library that provides text concatenation from given files.**

Author: Abdullah Selek


Contents:

.. toctree::
   :maxdepth: 1

   installation.rst
   mergerpy.rst

Introduction
------------

This library provides a fast text concatenation from files. It works with Python versions from Python 3.x.
The main aim to create this library is to create new passwords from given files which contain tokens. Then you can 
use `btcrecover <https://github.com/gurnec/btcrecover>`_ to get your password back.

Sample:

tokens.txt

+------------+
| A 1 e 2 a 3|
+------------+
| B s h i r  | 
+------------+
| E i 34 26 s|
+------------+

New created passwords.txt

+------+
| ABE  |
+------+
| ABi  |
+------+
| AB34 |
+------+
| AB26 |
+------+
| ABs  |
+------+
| ...  |
+------+

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
