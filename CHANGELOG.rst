Flask-mwoauth changelog

v0.4.81 (Fri Apr  3 16:02:43 DST 2020)
========================================
========================================
- Fix mwoauth.request (Martin Urbanec)

v0.4.76 (Wed Dec 18 09:49:00 CEST 2019)
========================================
========================================
- Add get_user_identity returning full identity object for current user (Martin Urbanec)
- Add get_user_identity_from_token returning full identity object
  for token-identified user (Martin Urbanec)

v0.4.75 (Sat Jul 27 22:23:13 CEST 2019)
========================================
- Fix content type in description to allow pypi upload

v0.4.74 (Sat Jul 27 22:18:07 CEST 2019)
========================================
- [backwards incompatible] use url_for to resolve target URL in logout sequence (Martin Urbanec)

v0.3.70 (Mon Oct 29 20:41:06 CET 2018)
========================================
- Return to main page instead of showing a blank 'logged out' page (Martin Urbanec)
- Make sure small requests are also sent authenticated (Martin Urbanec)
- Allow retrieving JSON from a request directly instead of returning text (Martin Urbanec)

v0.3.61 (Sat Feb 11 21:31:49 CET 2017)
========================================
- Full rewrite of backend to use the mwoauth library directly (Aaron Halfaker)
- Improvements of demo scripts to use credentials JSON file (Aaron Halfaker)

v0.2.54 (Mon Aug  1 22:30:29 CEST 2016)
=======================================
- Changed documentation from rst to markdown

v0.2.51 (Mon Aug  1 21:53:43 CEST 2016)
========================================
- Updated documentation of OAuth registration URL (Robin Krahl)
- Use POST form data instead of GET parameters (Cristian Consonni)

v0.2.46 (Sat Jul 25 20:57:31 CEST 2015)
========================================
- Python 3.3+ support (thanks, Jan Lebert)
  - This required a switch to flask-oauthlib

- Doc fixes

v0.1.37 (Sat Mar 21 17:48:31 CET 2015)
========================================
Feature: allow user to specify App name, which is also used for naming
         session variables.


v0.1.35 (Wed Jul 23 05:29:00 CEST 2014)
========================================
Bugfix: Added README.rst to source package to fix pip install.
General: Added several other files to the source package too (license,
         contributors, demo.py, etc.)

v0.1.34 (Mon Jul 21 06:15:42 CEST 2014)
========================================
New feature:
  - /logout will now also accept a 'next' parameter to forward the user to
    a nicer 'You have been logged out' page.

v0.1.31 (Tue Jan 14 13:46:10 CET 2014)
========================================
New features:
  - Allow MWOAuth.request to take an optional url parameter.
    This allows requests to a different wiki than the one where the OAuth
    authorization was performed, as long as the same OAuth headers are
    accepted (e.g. wikimedia foundation wikis)

v0.1.25 (Sat Jan 11 14:48:26 CET 2014)
========================================
New features:
  - handling of login?next=.... via cookies (by Cristian Consonni)
  - more efficient handling of big POST requests using the Requests library (by Cristian Consonni)

Bugfixes:
  - demo app now has correct index url
  - demo app now warns for using a random (thanks, again, Cristian!)

Also thanks to:
  - Kunal Mehta for a minor PEP8 fix
