from setuptools import setup,find_packages

setup(name='pypugjs',
      version='5.1.0',
      download_url='https://github.com/kakulukia/pypugjs/archive/5.1.0.tar.gz',
      packages=find_packages(),
      author='Andy Grabow',
      author_email='andy@freilandkiwis.de',
      description='PugJS syntax template adapter for Django, Jinja2, Mako and '
                  'Tornado templates - copy of PyJade with the name changed',
      long_description=open('README.rst').read(),
      keywords='pug pugjs template converter',
      url='http://github.com/kakulukia/pypugjs',
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
      ],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ])
