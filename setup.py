import setuptools

setuptools.setup(
    name="hidroteste",
    version="0.0.1",
    url="https://github.com/marcosmlr/hidroteste",

    author="Marcos Rodrigues",
    author_email="marcos_lrodrigues@yahoo.com.br",

    description="A test package to web scraping of weather data",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
