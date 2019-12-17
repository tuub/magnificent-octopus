from setuptools import setup, find_packages

setup(
    name = 'octopus',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [
        "Werkzeug==0.16.0",
        "Flask==1.1.1",
        "Flask-Login==0.4.1",
        "requests",
        "esprit",
        "simplejson",
        "lxml==3.8.0",
        "Flask-WTF==0.14.2",
        "nose",
        "Flask-Mail==0.9.1",
        "python-dateutil",
        "unidecode"
    ],
    url = 'http://cottagelabs.com/',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'Magnificent Octopus - Flask application helper library',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
