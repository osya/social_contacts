 # Django-based project for getting contacts from Microsoft Graph created in the scope of the Upwork task [python flask or django](https://www.upwork.com/ab/proposals/923638495980134400)
[![Build Status](https://travis-ci.org/osya/social_contacts.svg?branch=master)](https://travis-ci.org/osya/social_contacts)

Used technologies:
- OAuth 2. [`social-app-django`](github.com/python-social-auth/social-app-django) - for authenticate in different social services (Facebook, Microsoft Graph, etc)
- Used SDKs:
    - [`facebook-sdk`](https://github.com/mobolic/facebook-sdk) - for Facebook Graph
    - For Microsoft Graph used Python API https://github.com/microsoftgraph/msgraph-sdk-python
    - [`google-api-python-client`](https://github.com/google/google-api-python-client/). This client in the BaseGoogleOAuth2API for getting user data use Google+ API. So, both Google+ API and Google People API credentials should be granted for this app 
- Assets management: NPM & Webpack
- Travis CI

Installation:
```
    git clone https://github.com/osya/social_contacts
    cd social_contacts
    pip install -r requirements.txt
    npm install
    node node_modules/webpack/bin/webpack.js
    python manage.py collectstatic
    python manage.py runserver
```
