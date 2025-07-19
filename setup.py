from setuptools import setup, find_packages

setup(
    name="pytest_actions_report_demo",
    version="0.1",
    packages=find_packages(),
    package_dir={"": "src"},  # 关键点：指定源码在src目录
    install_requires=[],
)
