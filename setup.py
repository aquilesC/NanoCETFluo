from setuptools import setup, find_packages

setup(
    name='DisperFluo',
    version='1.0',
    url='https://www.dispertech.com',
    license='MIT',
    author='Aquiles Carattino',
    author_email='carattino@dispertech.com',
    description='Software to control the Fluorescence-based nanoCET',
    include_package_data=True,
    packages=find_packages('.'),
    package_data={
        "": ['GUI/*.ui', 'GUI/Icons/*.svg', 'GUI/Icons/*.png']
        },
    entry_points = {
        "console_scripts": [
            "DisperFluo=fluorescence.__main__:main"
        ]
    }
    )