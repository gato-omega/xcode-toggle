from setuptools import setup

setup(
    name='xcode-toggle',
    version='0.0.2',
    url='https://github.com/schwa/xcode-toggle',
    license='MIT',
    author='Jonathan Wight',
    author_email='schwa@schwa.io',
    description='A better "xcode-select"',
    py_modules=['xcode_toggle'],
    install_requires=['click', 'pathlib', 'blessings'],
    entry_points='''
        [console_scripts]
        xcode-toggle=xcode_toggle:main
    ''',
)

