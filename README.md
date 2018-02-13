# README

## Introduction

[![Build Status](https://travis-ci.org/osya/social_contacts.svg?branch=master)](https://travis-ci.org/osya/social_contacts)

Django-based project for getting contacts from Google, Facebook, Microsoft Graph, Yahoo created in the scope of the Upwork task [python flask or django](https://www.upwork.com/ab/proposals/923638495980134400)

Used technologies:

- Python & Django
- OAuth 2. [`social-app-django`](github.com/python-social-auth/social-app-django) - for authenticate in different social services (Facebook, Microsoft Graph, etc)
- Used SDKs:
  - [`facebook-sdk`](https://github.com/mobolic/facebook-sdk) - for Facebook Graph. For getting user friends permission `user_friends` required
  - For Microsoft Graph used [Python API](https://github.com/microsoftgraph/msgraph-sdk-python)
  - [`google-api-python-client`](https://github.com/google/google-api-python-client/). Google People API is using. This client for getting user data in the BaseGoogleOAuth2API use Google+ API. So, both Google+ API and Google People API credentials should be granted for this app
- Assets management: NPM & Webpack
- Travis CI

## Installation

```shell
    git clone https://github.com/osya/social_contacts
    cd social_contacts
    pip install -r requirements.txt
    npm install
    node node_modules/webpack/bin/webpack.js
    python manage.py collectstatic
    python manage.py runserver
```

## Usage

## Tests

```shell
    python manage.py lint
```
