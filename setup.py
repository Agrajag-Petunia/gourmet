#!/bin/env python
#
# setup.py for Gourmet

import sys
import glob
import os.path
import os
import fileinput
import string
from types import StringType, ListType, TupleType

from distutils.core import setup
from distutils.command.build_py import build_py as _build_py
from distutils.command.build_scripts import build_scripts as _build_scripts
from distutils.util import convert_path
from DistUtilsExtra.command import *

# grab the version from our "version" module
# first we have to extend our path to include gourmet/
sys.path.append(os.path.join(os.path.split(__file__)[0],'gourmet'))
import version

class build_py(_build_py):
    """build_py command
    
    This specific build_py command will modify module 'build_config' so that it
    contains information on installation prefixes afterwards.
    """

    def build_module (self, module, module_file, package):
        _build_py.build_module(self, module, module_file, package)

        if type(package) is StringType:
            package = string.split(package, '.')
        elif type(package) not in (ListType, TupleType):
            raise TypeError, \
                  "'package' must be a string (dot-separated), list, or tuple"

        if ( module == 'settings' and len(package) == 1
             and package[0] == 'gourmet'
             and 'install' in self.distribution.command_obj):
            outfile = self.get_module_outfile(self.build_lib, package, module)

            iobj = self.distribution.command_obj['install']
            lib_dir = iobj.install_lib
            base = iobj.install_data
            if (iobj.root):
                lib_dir = lib_dir[len(iobj.root):]
                base = base[len(iobj.root):]
            base = os.path.join(base, 'share')
            data_dir = os.path.join(base, 'gourmet')

            # abuse fileinput to replace two lines in bin/gourmet
            for line in fileinput.input(outfile, inplace = 1):
                if "base_dir = " in line:
                    line = "base_dir = '%s'\n" % base
                elif "lib_dir = " in line:
                    line = "lib_dir = '%s'\n" % lib_dir
                elif "data_dir = " in line:
                    line = "data_dir = '%s'\n" % data_dir
                elif "doc_base = " in line:
                    line = "doc_base = '%s'\n" % \
                        os.path.join(base, 'doc', 'gourmet')
                elif "icon_base = " in line:
                    line = "icon_base = '%s'\n" % \
                        os.path.join(base, 'icons', 'hicolor')
                elif "locale_base = " in line:
                    line = "locale_base = '%s'\n" % \
                        os.path.join(base, 'locale')
                elif "plugin_base = " in line:
                    line = "plugin_base = data_dir\n"

                print line,

class build_scripts(_build_scripts):
    """build_scripts command

    This specific build_scripts command will modify the bin/gourmet script
    so that it contains information on installation prefixes afterwards.
    """

    def copy_scripts(self):
        _build_scripts.copy_scripts(self)

        if "install" in self.distribution.command_obj:
            iobj = self.distribution.command_obj["install"]
            lib_dir = iobj.install_lib
            data_dir = iobj.install_data

            if iobj.root:
                lib_dir = lib_dir[len(iobj.root):]
                data_dir = data_dir[len(iobj.root):]

            script = convert_path("bin/gourmet")
            outfile = os.path.join(self.build_dir, os.path.basename(script))

            # abuse fileinput to replace two lines in bin/gourmet
            for line in fileinput.input(outfile, inplace = 1):
                if "lib_dir = '.'" in line:
                    line = "lib_dir = '%s'\n" % lib_dir
                elif "data_dir = '.'" in line:
                    line = "data_dir = '%s'\n" % data_dir

                print line,

def data_files():
    '''Build list of data files to be installed'''
    data_files = []

    for root, dirs, files in os.walk('data'):
        if files:
            files = [os.path.join(root, f) for f in files]
            data_files.append((os.path.join('share','gourmet', root[len('data')+1:]), files))

    # files in /usr/share/X/ (not gourmet)
    files = []
    base = os.path.join('share','gourmet')

    files.extend(data_files)
    files.extend([(os.path.join(base,'ui'), glob.glob(os.path.join('ui','*.ui')))])
    files.extend([(os.path.join('share','doc','gourmet'), ['FAQ', 'LICENSE'])])
    #print 'DATA FILES:',files
    return files

if os.name == 'nt':
    script = [os.path.join('windows','Gourmet.pyw'),
              os.path.join('windows','GourmetDebug.pyw')]
else:
    script = [os.path.join('bin','gourmet')]
    # Run upgrade pre script
    # Importing runs the actual script...
    #import tools.upgrade_pre_script
    #tools.upgrade_pre_script.dump_old_data()

plugins = []

def crawl (base, basename):
    bdir = base
    subdirs = filter(lambda x: os.path.isdir(os.path.join(bdir,x)), os.listdir(bdir))
    for subd in subdirs:
        name = basename + '.' + subd
        plugins.append(name)
        crawl(os.path.join(bdir,subd),name)

crawl('gourmet/plugins', 'gourmet.plugins')

result = setup(
    name = version.name,
    version = version.version,
    #windows = [ {'script':os.path.join('bin','gourmet'),
    #             }],
    description = version.description,
    author = version.author,
    author_email = version.author_email,
    url = version.website,
    license = version.license,
    data_files = data_files(),
    packages = ['gourmet',
                'gourmet.backends',
                'gourmet.defaults',
                'gourmet.gtk_extras',
                'gourmet.importers',
                'gourmet.exporters',
                'gourmet.legacy_db',
                'gourmet.legacy_db.db_085',
                'gourmet.legacy_db.db_09',
                'gourmet.plugins',
                ] + plugins,
    package_data = {'gourmet': ['plugins/*/*.ui', 'plugins/*/images/*.png','plugins/*/*/images/*.png']},
    scripts = script,
    cmdclass={'build' : build_extra.build_extra,
              'build_i18n' :  build_i18n.build_i18n,
              'build_icons' :  build_icons.build_icons,
              'build_py' : build_py,
              'build_scripts' : build_scripts,
             },
    )

