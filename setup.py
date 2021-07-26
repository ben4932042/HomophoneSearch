from setuptools import setup
setup(
    name = "HomophoneSearch",
    version = "0.0.0",
    description = "coustom packages install",

    author = "Ben Liu",

    packages = [
        'HomophoneSearch',
        'HomophoneSearch/Chinese',
        'HomophoneSearch/English',
        'HomophoneSearch/Pinyin2Hanzi',
        ],
    include_package_data = True,
    platforms = "any",
    install_requires = [],

    scripts = [],
)
