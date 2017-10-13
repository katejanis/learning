### Square 2.0 

This document describes Square 2.0 software.


#### Feature: Quadratic equation

Square 2.0 solves quadratic equations having the following form:
```
ax2 + bx + c = 0
```
where x represents an unknown, and a, b, and c represent known numbers such that a is not equal to 0.

Three separate values should be provided (a, b, c) as input. 
Square.py accepts only integer and/or float values.
Any values containing heading dots (e.g '.20') are converted to a float value ('0.20').
Any tailing dots ('20.') are truncated.


##### CLI
```
usage: square.py [-h] [-v] a b c

Script to solve quadratic equation. ax2 + bx + c = 0

positional arguments:
  a              Quadratic coefficient 'a'. Non-zero value.
  b              Linear coefficient 'b'
  c              Coefficient 'c'

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  Show program's version number and exit.
```
