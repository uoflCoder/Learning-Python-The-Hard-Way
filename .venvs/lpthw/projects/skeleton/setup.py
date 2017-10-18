try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
'description':'My Project',
'author':'Tylor Cornett',
'url':'URL to get the project',
'download_url':'Where to download project.',
'author_email':'tylorcornett@gmail.com',
'version':'0.1',
'install_requires':['nose'],
'packages':['NAME'],
'scripts':[],
'name':'projectname'
}

setup(**config)
