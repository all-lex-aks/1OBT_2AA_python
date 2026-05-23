from setuptools import setup, find_packages

setup(
    name="1OBT_2AA_python_test-task",
    version="1.0.0",
    author="all-lex-aks",
    author_email="alexei.k.aksyutin@gmail.com",
    description="Тестовое задание на старой версии Django",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/all-lex-aks/1OBT_2AA_python",
    packages=find_packages(exclude=["tests*", ".venv*"]),
    
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Framework :: Django :: 2.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    
    install_requires=[
        "Django>=2.2,<3.0",
        "psycopg2-binary>=2.9",
    ],
    
)
