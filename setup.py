from setuptools import setup

exec([l for l in open("flask_mwoauth/__init__.py")
      if l.startswith('__version__')][0])

setup(name='flask-mwoauth',
      version=__version__,
      description='Flask blueprint to connect to a MediaWiki OAuth server',
      url='http://github.com/valhallasw/flask-mwoauth',
      author='Merlijn van Deen',
      author_email='valhallasw@arctus.nl',
      license='MIT',
      packages=['flask_mwoauth'],
      install_requires=['flask-oauth', 'requests>=2.0.1'],
      zip_safe=True,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Web Environment",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Libraries :: Python Modules"]
      )
