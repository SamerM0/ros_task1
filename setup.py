from setuptools import find_packages, setup

package_name = 'multi_sensor_validator'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='samer',
    maintainer_email='samer@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "ultrasonic_node = multi_sensor_validator.ultrasonic_node:main",
            "infrared_node = multi_sensor_validator.infrared_node:main",
            "validator_node = multi_sensor_validator.validator_node:main",
            "logger_node = multi_sensor_validator.logger_node:main"
        ],
    },
)
