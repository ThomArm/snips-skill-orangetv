from setuptools import setup

setup(
    name='OrangeTV-Skill',
    version='0.0.1',
    description='OrangeTV Skill for Snips',
    url='https://github.com/ThomArm/snips-skill-orangetv',
    download_url='',
    license='MIT',
    install_requires=['requests==2.6.0'],
    test_suite="tests",
    keywords=['snips'],
    packages=['myskill'],
    package_data={'myskill': ['Snipsspec']},
    include_package_data=True,
)
