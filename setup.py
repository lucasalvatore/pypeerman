from setuptools import find_packages, setup

setup(
    name="pypeerman",
    description="Peering Manager API client library",
    url="",
    author="Luca Salvatore",
    author_email="",
    license="Apache2",
    include_package_data=True,
    setup_requires=["setuptools_scm"],
    install_requires=["requests>=2.31.0,<3.0", "packaging"],
)