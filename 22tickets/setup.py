from setuptools import setup

setup(
  name='tickets',
  py_modules=['tickets', 'stations', 'codes'],
  install_requires=['requests', 'docopt', 'prettytable', 'colorama'],
  entry_points={
     'console_scripts': ['tickets=tickets:cli'] 
  }
)