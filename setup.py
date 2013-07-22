# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages

version = '1.0a2.dev0'
long_description = (open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "INSTALL.txt")).read() + "\n" +
                    open(os.path.join("docs", "CREDITS.txt")).read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read())


setup(name='brasil.gov.barra',
      version=version,
      description="Brasil.gov.br: Barra de Identidade ",
      long_description=long_description,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.2",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Libraries :: Python Modules"],
      keywords='brasil.gov.br barra plone plonegovbr temas ',
      author='PloneGov.Br',
      author_email='gov@plone.org.br',
      url='http://www.plone.org.br/gov/',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['brasil', 'brasil.gov'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools'],
      extras_require={
          'develop': [
              'Sphinx',
              'manuel',
              'pep8',
              'setuptools-flakes',
          ],
          'test': [
              'interlude',
              'plone.app.testing'
          ]},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
