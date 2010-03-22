#!/usr/bin/env bash



# Copyright (C) 2009, Mathieu PASQUET <mpa@makina-corpus.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the <ORGANIZATION> nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#
#
#
#
#
ignore="
bin
buildout-buildbot.cfg.before.fixed_version.bak
buildout-dev.cfg.before.fixed_ve
files
buildout-dev.cfg.before.fixed_version.bak
develop-eggs
.directory
downloads
dumps
*.egg-info
eggs
*.env
activate_env.sh
fake-eggs
fake-eggs/*
.installed.cfg
.mr.developer.cfg
old.withfsd.var.20090115.tbz2
parts
phpsite
*.pt.py
src.*
src.mrdeveloper/*
src.others
sys
tags.python
var
"
src="$ignore
        PlominoDoc.egg-info
"
inner="$ignore 
build
_build
"


svn propset -R svn:ignore "$ignore" .
svn propset  svn:ignore "$src" src
svn propset  svn:ignore "$inner" src/PlominoDoc
svn ci -m "resetting svnignore"


# vim:set et sts=4 ts=4 tw=80: