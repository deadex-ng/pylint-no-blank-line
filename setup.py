from setuptools import setup

setup(
    name="pylint_no_blank_line",
    version="0.1",
    description="Plugin for pylint which ensures no blank line after function definition.",
    author="Fumbani Banda",
    license="MIT",
    keywords=["pylint", "blank", "line", "lint"],
    packages=["pylint_no_blank_line"],
    install_requires=["pylint"],
    classifiers=[
        "Development Status :: 4 - Beta ",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    zip_safe=False,
)
