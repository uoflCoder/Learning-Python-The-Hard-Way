try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

	config = {
		'description': 'Exercise 48',
		'author': 'uoflcoder',
		'url': 'URL to get it at.',
		'download_url': 'Where to download it',
		'author_email': 'tylorcornett@gmail.com',
		'version': '0.1',
		'install_requires': ['nose'],
		'packages': ['ex47'],
		'scripts': [],
		'name': 'Exercise 48'

		}

	setup(**config)
