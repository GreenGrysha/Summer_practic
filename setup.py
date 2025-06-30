from setuptools import setup, find_packages
from pathlib import Path


def get_requirements():
    requirements_path = Path(__file__).parent / "requirements.txt"
    with open(requirements_path, encoding="utf-8") as f:
        return [line.strip() for line in f
                if line.strip() and not line.startswith("#")]


setup(
    name="image_redactor",
    version="1.0.0",
    description="Редактор изображений ",
    author="GreenGrysha",
    package_dir={"": "src"},
    packages=find_packages(where="src"),

    install_requires=get_requirements(),
    entry_points={
        "console_scripts": [
            "image-redactor=main:main",
        ],
    },
    python_requires=">=3.8.20",
)