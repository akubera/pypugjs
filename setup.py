from setuptools import setup,find_packages

setup(name='pypugjs',
      version='4.2.2',
      download_url='https://github.com/matannoam/mypackage/pypugjs/4.2.2.tar.gz',
      packages=find_packages(),
      author='Matan Noam Shavit',
      author_email='matannoam@gmail.com',
      description='PugJS syntax template adapter for Django, Jinja2, Mako and '
                  'Tornado templates - copy of PyJade with the name changed',
      long_description=open('README.rst').read(),
      keywords='pug pugjs template converter',
      url='http://github.com/matannoam/pypugjs',
      license='MIT',
      entry_points={
          'console_scripts' : ['pypugjs = pypugjs.convert:convert_file',]
      },
      install_requires=['six'],
      tests_require=[
            'nose',
            'django',
            'jinja2',
            'tornado',
            'pyramid >= 1.4, <= 1.4.99',
            'mako',
      ])
