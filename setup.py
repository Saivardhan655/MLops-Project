from setuptools import setup, find_packages

setup(
    name="MLops project",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'seaborn',
        'flask',
        'mlflow==2.2.2',
        'dvc',
        'ipykernel',
        'xgboost',
    ],
    extras_require={
        'dev': [
            'pytest==7.1.3',
            'tox==3.25.1',
            'black==22.8.0',
            'flake8==5.0.4',
            'mypy==0.971',
        ],
    },
)
