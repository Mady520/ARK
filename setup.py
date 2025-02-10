import os
import shutil
from setuptools import setup, find_packages

def post_install():
    bin_path = "/usr/local/bin/ark"
    script_path = os.path.expanduser("~/.local/bin/ark")
    if os.path.exists(script_path):
        shutil.copy(script_path, bin_path)
        os.chmod(bin_path, 0o755)  # Make it executable

setup(
    name="ark",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["ark=ark.main:main"],
    },
    include_package_data=True,
)

post_install()  # Run post-install script
