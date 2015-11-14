ipynose
=======

.. image:: https://travis-ci.org/wikibootup/ipynose.svg?branch=master
    :target: https://travis-ci.org/wikibootup/ipynose

print nosetests result in the iPython (notebook)

iPython notebook example `here
<http://wikibootup.github.io/etc/py/ipynose/ipynose_example.html>`_.

Usage
=====

.. code:: python

    from ipynose import ipynose

1. no path
==========

``nosetests without specific path. (-v option default)``

.. code:: python

    ipynose.show_nose_result()

    1) If empty, Error should occur ... SKIP: showing class skipping
    First node should be equal to last node ... SKIP: showing class skipping
    1) Last node should contaions inserted self.item ... SKIP: showing class skipping
    Initial Queue ... SKIP: showing class skipping
    1) 'peek' returns first node item. ... SKIP: showing class skipping
    test_dequeue ... ok
    test_enqueue_when_empty ... ok
    test_enqueue_when_not_empty ... ok
    test_make_queue ... ok
    test_peek ... ok

    ----------------------------------------------------------------------
    Ran 10 tests in 0.014s

    OK (SKIP=5)

2. Specific path
================

``nosetests for specific file. (-v option default)``

.. code:: python

    EXAMPLE_TEST_PATH = "py/queue/tests/test_queue.py"

    ipynose.show_nose_result(EXAMPLE_TEST_PATH)

    test_dequeue ... ok
    test_enqueue_when_empty ... ok
    test_enqueue_when_not_empty ... ok
    test_make_queue ... ok
    test_peek ... ok

    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s

    OK
