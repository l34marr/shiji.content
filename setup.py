from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='shiji.content',
      version=version,
      description="ShiJi Content Types",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://github.com/l34marr/shiji.content',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['shiji'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          'collective.dexteritytextindexer'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
#     setup_requires=["PasteScript"],
#     paster_plugins = ["ZopeSkel"],

      )
