louvain-communities
===================

Python implementation of the Louvain method for detecting communities
introduced in [#]_ built on top of the NetworkX framework with support for
randomizing node order.

Requirements
------------

* Python 3
* NetworkX 1.11

Usage
-----
First install the package using::

    python setup.py install

Then import the package and use on a NetworkX graph:

.. code:: python

    import networkx as nx
    from louvain import detect_communities


    G = nx.karate_club_graph()
    partition = detect_communities(G)

See the Jupyter notebook for an example of visualising with matplotlib.

References
----------

.. [#] Blondel V.D., Guillaume J.-L., Lambiotte R., Lefebvre E. (2008) Fast
   unfolding of communities in large networks. J. Stat. Mech. P10008
   (https://arxiv.org/abs/0803.0476)
