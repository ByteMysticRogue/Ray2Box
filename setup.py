from setuptools import setup, find_packages

setup(
    name="Ray2Box",
    version="1.0.0",
    author="ByteMysticRogue",
    author_email="bytemysticrogue@gmail.com",
    url="https://github.com/ByteMysticRogue",
    description="A Command-line Tool to Convert V2ray links to Singbox Configs",
    license="GPLv3",
    license_files=("LICENSE",),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
    ],
    packages=find_packages(exclude=["Parsers*", "singbox*", "template*"]),
    entry_points={
        "console_scripts": [
            "Ray2Box = Cli.Ray2Box:main",
        ]
    }
)
