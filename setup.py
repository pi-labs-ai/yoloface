from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    requirements = [line for line in lines if line and not line.startswith("#")]
    return requirements

setup(
    name='yoloface',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    url='https://github.com/elyha7/yoloface',
    author='Author Name',
    author_email='author@example.com',
    description='YOLO Face detection package',
    python_requires='>=3.6',
    package_data={
        'yoloface': ['weights/yolov5n_state_dict.pt', 'models/*.yaml'],
    },
)
