from setuptools import setup, find_packages
import subprocess


def get_version():
    process = subprocess.Popen(["git", "describe", "--always", "--tags"], stdout=subprocess.PIPE, stderr=None)
    last_tag = process.communicate()[0].decode('ascii').strip()
    if '-g' in last_tag:
        return last_tag.split('-g')[0].replace('-', '.')
    else:
        return last_tag


with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()

setup(
    name='devdeck_hijri',
    version=get_version(),
    description="Displays Date on Hijri with Decimal Time.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='dysbulic and tenfinney',
    url='https://github.com/dhappy/devdeck_hijri_date_and_decimal_time',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_reqs
)
