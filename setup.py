#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    with open('README.rst') as readme_file:
        readme = readme_file.read()

        with open('HISTORY.rst') as history_file:
            history = history_file.read()

        requirements = []

        test_requirements = []

    setup(
        author='Brian Clauser',
        author_email='pzljug@hotmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: Implementation',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing',
            'Topic :: Text Processing :: Linguistic',
        ],
        description='Generator for random Klingon test.',
        include_package_data=True,
        install_requirements=requirements,
        keywords='lorem ipsum klingon random text',
        license='MIT',
        long_description=readme + '\n\n' + history,
        name='lorem',
        package_dir={'lorem': 'lorem'},
        packages=['lorem'],
        python_requries='>=3.3',
        tests_require=test_requirements,
        url='https://github.com/bdclauser/lorem',
        version='0.1',
        zip_safe=False)