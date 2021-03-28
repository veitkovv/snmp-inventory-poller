import pathlib

from setuptools import find_packages
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='snmp-inventory-poller',
    version=(here / 'VERSION').read_text(),
    description='Poll network devices over SNMP and save some inventory information about device',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/veitkovv/snmp-inventory-poller',
    author='Viktor Veitko',
    author_email='veitko.vv@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='network automation, network development',
    packages=find_packages(),
    python_requires='>=3.9, <4',
    install_requires=['aiosnmp', 'netaddr'],
    extras_require={
        'test': ['pytest-cov', 'pytest', 'PyYAML'],
        'doc': ['sphinx', 'sphinx-autobuild', 'sphinxemoji'],
    },
    project_urls={
        'Source': 'https://github.com/veitkovv/snmp-inventory-poller/',
        'Bug Reports': 'https://github.com/veitkovv/snmp-inventory-poller/issues',
    },
    entry_points={'console_scripts': [
        'snmp-inventory-poller = snmp_inventory_poller.__main__:main'
    ]}
)
