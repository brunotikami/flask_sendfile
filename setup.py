"""
Flask-SendFile
-------------
Flask extension that enables file transfer control using HTTPheaders
such as X-Sendfile and X-Accel-Redirect
"""
from setuptools import setup


setup(
    name='Flask-SendFile',
    version='0.1',
    url='https://github.com/brunotikami/flask_sendfile'
    license='BSD',
    author='Bruno Tikami',
    author_email='brunotikami@gmail.com',
    description='Flask support for X-Sendfile and X-Accel-Redirect',
    long_description=__doc__,
    py_modules=['flask_sendfile'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
