from setuptools import setup

setup(
    name='nix_currently_building',
    py_modules=['nix_currently_building'],
    entry_points={
        'console_scripts': [
            'nix-currently-building = nix_currently_building:main',
        ],
    }
)
