from distutils.core import setup, Extension

setup(name='happyc', version='1.0', ext_modules=[Extension('happyc', ['happyc.c'])])
