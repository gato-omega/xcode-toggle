import re
from setuptools import setup

VERSIONFILE = "_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name='xcode-toggle',
    version=verstr,
    url='https://github.com/schwa/xcode-toggle',
    license='MIT',
    author='Jonathan Wight',
    author_email='schwa@schwa.io',
    description='A better "xcode-select"',
    py_modules=['xcode_toggle',"_version"],
    install_requires=['click', 'pathlib', 'blessings'],
    entry_points='''
        [console_scripts]
        xcode-toggle=xcode_toggle:main
    ''',
)
