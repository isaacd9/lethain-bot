from distutils.core import setup

setup(
    name='lethain-bot',
    version='0.1dev',
    packages=[
        'generate',
        'post',
    ],
    license='ISC License',
    long_description=open('README.md').read(),
)
