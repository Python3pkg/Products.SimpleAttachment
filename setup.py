from setuptools import setup, find_packages

version = '4.5.dev0'

setup(
    name='Products.SimpleAttachment',
    version=version,
    description="Simple Attachments for Plone",
    long_description=(open("README.md").read() + '\n' +
                      open('CHANGES.txt').read()),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone attachments RichDocument',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='https://github.com/collective/Products.SimpleAttachment',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'archetypes.schemaextender',
        'plone.app.blob',
    ],
    extras_require={'test': [
        'zope.testing',
        'collective.testcaselayer',
        'Products.RichDocument',
    ]},
)
