# Copyright (c) 2015 Canonical Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

""" Charm utilities

Api for the charmstore:
https://github.com/juju/charmstore/blob/v4/docs/API.md
"""
import yaml
import requests
import os.path as path

cs = 'https://api.jujucharms.com/v4'


class CharmStoreException(Exception):
    """ CharmStore exception """


def get_bundle(bundle):
    """ Attempts to grab the bundle.yaml

    Arguments:
    bundle: name of bundle

    Returns:
    Dictionary of bundle's yaml
    """
    bundle = path.join(cs, bundle, 'archive/bundle.yaml')
    req = requests.get(bundle)
    if not req.ok:
        raise CharmStoreException("Problem getting bundle: {}".format(req))
    return yaml.safe_load(req.text)
