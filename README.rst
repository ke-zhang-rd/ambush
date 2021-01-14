======
ambush
======

.. image:: https://img.shields.io/travis/ke-zhang-rd/ambush.svg
        :target: https://travis-ci.org/ke-zhang-rd/ambush

.. image:: https://img.shields.io/pypi/v/ambush.svg
        :target: https://pypi.python.org/pypi/ambush


This is a debug toolbox.

* Free software: 3-clause BSD license
* Documentation: (COMING SOON!) https://ke-zhang-rd.github.io/ambush.

Features
--------

**Example:**

.. code:: python
  :caption: main.py
  :linenos:

  from sub import Member


  class Primary:

      def foo(self):
          a = 1
          a = a + 1
          m = Member()
          m.bar()
          a = a + 1
          a = a + 1


  p = Primary()
  p.foo()

.. code:: python
  :caption: sub.py
  :linenos:

  class Member:


      def bar(self):
          from ambush import detector
          detector()

**Output:**

.. code:: none

  Who is calling current function
  =========================================================
  In file:
  /Users/kz2249/tmp/main.py

  class Primary:
      # by caller function:
      def foo in line 6
          ...
          # actually call:
          m.bar() # in line 10
          ...

  Peek:
  ---------------------------------------------------------
      def foo(self):
          a = 1
          a = a + 1
          m = Member()
          m.bar()
          a = a + 1
          a = a + 1

  =========================================================
