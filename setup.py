from setuptools import setup, find_packages

with open("README.md") as readme_file:
    long_description = readme_file.read()

install_requires = ["setuptools", "diceware", "click"]

setup(
    name="gempass",
    packages=find_packages(),
    entry_points={"console_scripts": ["gempass = genpass.__init__:main"]},
    version="0.0.1",
    author="Mayuri Lahane",
    author_email="mayurilahane1998@gmail.com",
    description="Genpass - Command Line Password Manager Tool",
    long_description=long_description,
    license="MIT",
    keywords="genpass manpass gempass passwordmanager manager encryption",
    url="https://github.com/paint-it/genpass",
    py_modules=["genpass.__init__"],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
   # scripts=["test_readit.py"],
)

