from setuptools import setup

setup(
    name='control_center',
    version='1.0.0',
    install_requires=[
        'paho-mqtt'
    ],
    entry_points="""
         [paste.app_factory]
         """,
    url='',
    license='',
    author='Stephen Goedhart',
    author_email='sdg25@hotmail.com',
    description=''
)
