from setuptools import setup, find_packages

setup(
    name='metodosINE',
    version='1.0',
    description='Funciones regularmente utilizadas en los respectivos programas realizados para el INE.',
    author='Diego Sarceño',
    author_email='dsarceno68@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pyodbc==4.0.39',
        'pandas==2.0.2',
        'SQLAlchemy==2.0.16'
    ],
    include_package_data=True,
    package_data={
        'metodosINE' : ['metodosINE/credenciales.json']
    }
)