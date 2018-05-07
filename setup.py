import sys
from distutils.core import setup


setup(name='setdict',
      version='0.0.1',
      author='Arthur Moreno',
      author_email='morenoarthur@gmail.com',
      url='https://github.com/arthurmoreno/setdict/',
      description=(
          'Python dict-like interface '
          'for merging dicts with add to set property'
      ),
      py_modules=['setdict'],
      license='GPL3',
      keywords=['key-value', 'merge', 'set', 'dictionary'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
