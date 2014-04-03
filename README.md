py-projectplace
===============

Python wrapper accessing Projectplace's OAuth2 API.

Fetching a protected resource after obtaining an access token can be as simple as:

```pycon
    >>> from projectplace import PPClient
    >>> client = PPClient(r'client_id', token=r'token')
    >>> url = '1/user/me/profile.json'
    >>> r = client(url)
```
Before accessing resources you will need to obtain a few credentials from your us and authorization from the user for whom you wish to retrieve resources for. You can read all about this in the full [OAuth 2 workflow guide on RTD]( http://requests-oauthlib.readthedocs.org/en/latest/oauth2_workflow.html).

Installation
-------------

You need requests and requests_oauthlib for this, install using pip:

```bash
    $ pip install requests requests_oauthlib
```

Try it out with Flask
---------------------

We've added a simple Flask app for you to try it out. 

First, install Flask, again use pip:
```bash
    $ pip install flask
```

Insert your client_id and client_secret. To run this locally you need to register an API app with the callback 'https://localhost:8100'

GLHF
