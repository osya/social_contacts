 # Django-based project for getting contacts from Microsoft Graph created in the scope of the Upwork task [python flask or django](https://www.upwork.com/ab/proposals/923638495980134400)
[![Build Status](https://travis-ci.org/osya/social_contacts.svg?branch=master)](https://travis-ci.org/osya/social_contacts)

Used technologies:
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
