from setuptools import setup, find_packages

setup(
    name='gitpulse',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here:
        'gitpython',
        'jinja2',
        'python-dateutil',
    ],
    entry_points={
        'console_scripts': [
            'gitpulse = gitpulse.gitpulse_cli:main',
        ],
    }
)
