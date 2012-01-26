from distutils.core import setup
import py2exe

setup(name='impactuX',
      version='0.7',
      description='TuX collision game',
      author='Alexander Desyatnichenko',
      author_email='1_0@usa.com',
      url='https://github.com/1-0/impactuX',
      #packages=['impactuX', ],
      #package_dir = {'': 'lib'},
      windows=[{"script":"main.py"}],
      options={"py2exe": {"includes":["pygame",]}},
      package_data={'mypkg': ['fonts/*', 'pic/*']},
      #options={"py2exe": {"includes":["pygame", "libpng", "libogg", "libjpeg"]}},
     )
#setup(console=['main.py'])
