from setuptools import setup

setup(
    name='xcode-toggle',
    version='0.0.1',
    # packages=[''],
    # url='',
    license='MIT',
    author='Jonathan Wight',
    author_email='jwight@mac.com',
    description='A better "xcode-select"',
    py_modules=['xcode_toggle'],
    install_requires=['click', 'pathlib', 'blessings'],
    entry_points='''
        [console_scripts]
        xcode_toggle=xcode_toggle:main
    ''',
)

