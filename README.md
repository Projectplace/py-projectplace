py-projectplace
===============

Python wrapper for OAuth2 requests.


Fetching a protected resource after obtaining an access token can be as simple as:

.. code-block:: pycon

    >>> from projectplace import PPClient
    >>> client = PPClient(r'client_id', token=r'token')
    >>> url = '1/user/me/profile.json'
    >>> r = client(url)

Before accessing resources you will need to obtain a few credentials from your us and authorization from the user for whom you wish to retrieve resources for. You can read all about this in the full `OAuth 2 workflow guide on RTD <http://requests-oauthlib.readthedocs.org/en/latest/oauth2_workflow.html>`_.

Installation
-------------

You need requests and requests_oauthlib for this, install using pip:

.. code-block:: bash

    $ pip install requests requests_oauthlib

To run our example with Flask, again use pip:
.. code-block:: bash

    $ pip install flask