from setuptools import setup

setup(name='flask-mwoauth',
      version='0.1.1',
      description='Flask blueprint to connect to a MediaWiki OAuth server',
      url='http://github.com/valhallasw/flask-mwoauth',
      author='Merlijn van Deen',
      author_email='valhallasw@arctus.nl',
      license='MIT',
      packages=['flask_mwoauth'],
      install_requires=['flask-oauth'],
      zip_safe=True,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Web Environment",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ]
)
