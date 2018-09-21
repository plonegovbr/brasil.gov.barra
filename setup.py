# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '2.0b1'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='brasil.gov.barra',
      version=version,
      description=".gov.br: Barra de Identidade ",
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='brasil.gov.br barra plone plonegovbr temas ',
      author='PloneGov.Br',
      author_email='gov@plone.org.br',
      url='https://github.com/plonegovbr/brasil.gov.barra',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['brasil', 'brasil.gov'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.api',
          'Products.CMFPlone >=4.3',
          'setuptools',
      ],
      extras_require={
          'develop': [
              'Sphinx',
              'manuel',
              'pep8',
              'setuptools-flakes',
          ],
          'test': [
              'interlude',
              'plone.app.testing',
              'requests',
          ]},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
