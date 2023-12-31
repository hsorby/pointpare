
=========
PointPare
=========

A simple package for paring together points.

Usage
=====

::

  from pointpare import PointPare
  pp = PointPare()
  pp.add_points([... list of point ...])
  pp.pare_points()
  pared_points = pp.get_pared_points()

Points can be provided as a list of lists, like so::

  points = [[-10.4498, 31.1871, 1161.39], [-9.26793, 26.6263, 1162.51], [-8.96271, 27.5622, 1161.49], [-10.4498, 31.1871, 1161.39]]
  pp.add_points(points)

or as a flat list, where the list is divisible by three, like so::

  points = [31.1871, 1161.39, -10.7776, 29.8503, 1162.7, -9.26793, 26.6263, 1162.51, -10.7776]
  pp.add_points(points)

Testing
=======

Tests are written with unittest and can be run like so::

  python -m unittest discover -s tests

Where the working directory is the base directory of the repository.

The coverage analysis can be run with the following command::

  coverage run --source=src/ -m unittest discover -s tests

Where the working directory is the base directory of the repository.

The report should show something like the following::

  Name                        Stmts   Miss  Cover
  -----------------------------------------------
  src/pointpare/__init__.py      54      0   100%
  -----------------------------------------------
  TOTAL                          54      0   100%

from the coverage report command::

  coverage report
