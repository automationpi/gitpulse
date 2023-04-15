from setuptools import setup, find_packages

setup(
    name='gitpulse',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here, for example:
        # 'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'gitpulse = gitpulse.gitpulse_cli:main',
        ],
    }
)
