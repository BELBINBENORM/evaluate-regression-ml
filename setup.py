from setuptools import setup

setup(
    name="evaluate_regression_ml",
    version="0.1.0",
    author="BELBIN BENO RM",
    author_email="belbin.datascientist@gmail.com",
    description="An AutoML-lite marathon engine for evaluating 30+ scikit-learn regressors with active resource guarding.",
    long_description="A utility to automate the evaluation of a massive catalog of regression models, featuring active RAM and Time guarding using multiprocessing.",
    url="https://github.com/BELBINBENORM/evaluate-regression-ml",
    py_modules=["Evaluate_Regression"],
    install_requires=[
        "pandas",
        "scikit-learn>=1.4.0",
        "joblib",
        "psutil"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
)
