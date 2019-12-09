from setuptools import setup, find_packages

setup(
    name='logbook',
    version='1.0.1',
    description='A simple logbook made with python',
    url='https://github.com/lukew3/logbook',
    author='Luke Weiler',
    author_email='lukew25073@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
	   'console_scripts': [
            'newlog=logbook.addentry', #add combine logs later
	   ],
    },
)
