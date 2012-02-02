from distutils.core import setup
import py2exe,sys,os

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in ("msvcp71.dll", "dwmapi.dll"):
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL
setup(name='impactuX',
      version='0.7',
      description='TuX collision game',
      author='Alexander Desyatnichenko',
      author_email='1_0@usa.com',
      url='https://github.com/1-0/impactuX',
      #packages=['impactuX', ],
      #package_dir = {'': 'lib'},
      windows=[{"script":"impactuX.py"}],
      options={"py2exe": {"includes":["pygame",]}},
      package_data={'mypkg': ['fonts/*', 'pic/*']},
      #options={"py2exe": {"includes":["pygame", "libpng", "libogg", "libjpeg"]}},
     )
#setup(console=['main.py'])
