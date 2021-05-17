# Copyright 2021 Abhinav Omprakash. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""A mock of django classes and functions"""

class conf:
    """ A mock of django.conf"""

    class settings:
        DEBUG = True
        ALWAYS_MINIFY = False
    

if __name__=="__main__":
    print(conf.settings.DEBUG)