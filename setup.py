from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

# if you want to deploy, see here 
# https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/