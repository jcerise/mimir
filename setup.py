from setuptools import setup

setup(name='Mimir',
      version='0.1',
      description='A simple, command line, note taking utility.',
      url='https://github.com/jcerise/mimir',
      author='Jeremy Cerise',
      author_email='jcerise06@gmail.com',
      packages=['Mimir'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['Click',],
      entry_points='''
            [console_scripts]
            mimir=Mimir.mimir:cli
      ''',
      )
