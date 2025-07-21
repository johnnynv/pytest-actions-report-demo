from setuptools import setup, find_packages

setup(
    name="pytestshow",
    packages=find_packages(where="src"),  # 自动发现src下的包
    package_dir={"": "src"},  # 关键：指定包根目录为src
)
