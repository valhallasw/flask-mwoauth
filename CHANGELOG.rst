Flask-mwoauth changelog

v0.1.28 (Tue Jan 14 13:40:10 CET 2014)
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
