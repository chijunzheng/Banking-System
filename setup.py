from setuptools import setup, find_packages

setup(
    name='banking-system',
    version='0.1.0',
    description='Banking System project',
    author='Jason Chi',
    author_email='chijunzheng@gmail.com',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_marshmallow',
        'marshmallow-sqlalchemy',
        'bcrypt',
        'pyjwt',
    ],
)

