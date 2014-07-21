Flask-mwoauth changelog

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
