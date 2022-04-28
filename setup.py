from setuptools import setup, find_packages

setup(
    name="serializer",
    packages=find_packages(),
    version="1.0.0",
    author="Turlay",
    install_requires="toml==0.10.2",
    author_email='turlaymargarita@gmail.com',
    url='https://github.com/margoturlay/ISP-2022-053503',
    scripts=["__main__.py", "tests/tests.py"]
)
