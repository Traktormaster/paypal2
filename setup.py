import os
import shutil
from collections import defaultdict

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = "0.2.2"

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = defaultdict(list)
for name in os.listdir(os.path.join(HERE, "requirements")):
    if name not in ("base.in", "test.in"):
        continue
    reqs = requirements[name.rpartition(".")[0]]
    with open(os.path.join(HERE, "requirements", name)) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line.startswith("-r"):
                continue
            reqs.append(line)
install_requirements = requirements.pop("base")


# Manually cleaning before build is required.
for p in [os.path.join(HERE, "build"), os.path.join(HERE, "dist"), os.path.join(HERE, "paypal2.egg-info")]:
    if os.path.exists(p):
        shutil.rmtree(p)

setup(
    name="paypal2",
    version=VERSION,
    description="Opinionated asyncio Paypal server-side integration SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Traktormaster/paypal2",
    author="Nándor Mátravölgyi",
    author_email="nandor.matra@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=[
        p for p in find_packages(where=HERE, include=["paypal2*"]) if not p.startswith("paypal2_")
    ],
    # package_data=package_data,
    install_requires=install_requirements,
    # entry_points={"console_scripts": console_scripts},
    extras_require=dict(requirements),
    python_requires=">=3.10",
)
