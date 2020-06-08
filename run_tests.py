#!/usr/bin/env python3

import os
import sys
import subprocess


cmdline = [sys.executable, '-m', 'unittest', 'discover', 
        '--verbose', '--start-directory=tests/', '--top-level-directory=.']

sys.exit(subprocess.run(cmdline, 
                        stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, 
                        cwd=os.path.dirname(os.path.abspath(__file__))
                        ).returncode)
