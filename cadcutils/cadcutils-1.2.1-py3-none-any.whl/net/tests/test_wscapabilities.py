# -*- coding: utf-8 -*-
# ***********************************************************************
# ******************  CANADIAN ASTRONOMY DATA CENTRE  *******************
# *************  CENTRE CANADIEN DE DONNÉES ASTRONOMIQUES  **************
#
#  (c) 2017.                            (c) 2017.
#  Government of Canada                 Gouvernement du Canada
#  National Research Council            Conseil national de recherches
#  Ottawa, Canada, K1A 0R6              Ottawa, Canada, K1A 0R6
#  All rights reserved                  Tous droits réservés
#
#  NRC disclaims any warranties,        Le CNRC dénie toute garantie
#  expressed, implied, or               énoncée, implicite ou légale,
#  statutory, of any kind with          de quelque nature que ce
#  respect to the software,             soit, concernant le logiciel,
#  including without limitation         y compris sans restriction
#  any warranty of merchantability      toute garantie de valeur
#  or fitness for a particular          marchande ou de pertinence
#  purpose. NRC shall not be            pour un usage particulier.
#  liable in any event for any          Le CNRC ne pourra en aucun cas
#  damages, whether direct or           être tenu responsable de tout
#  indirect, special or general,        dommage, direct ou indirect,
#  consequential or incidental,         particulier ou général,
#  arising from the use of the          accessoire ou fortuit, résultant
#  software.  Neither the name          de l'utilisation du logiciel. Ni
#  of the National Research             le nom du Conseil National de
#  Council of Canada nor the            Recherches du Canada ni les noms
#  names of its contributors may        de ses  participants ne peuvent
#  be used to endorse or promote        être utilisés pour approuver ou
#  products derived from this           promouvoir les produits dérivés
#  software without specific prior      de ce logiciel sans autorisation
#  written permission.                  préalable et particulière
#                                       par écrit.
#
#  This file is part of the             Ce fichier fait partie du projet
#  OpenCADC project.                    OpenCADC.
#
#  OpenCADC is free software:           OpenCADC est un logiciel libre ;
#  you can redistribute it and/or       vous pouvez le redistribuer ou le
#  modify it under the terms of         modifier suivant les termes de
#  the GNU Affero General Public        la “GNU Affero General Public
#  License as published by the          License” telle que publiée
#  Free Software Foundation,            par la Free Software Foundation
#  either version 3 of the              : soit la version 3 de cette
#  License, or (at your option)         licence, soit (à votre gré)
#  any later version.                   toute version ultérieure.
#
#  OpenCADC is distributed in the       OpenCADC est distribué
#  hope that it will be useful,         dans l’espoir qu’il vous
#  but WITHOUT ANY WARRANTY;            sera utile, mais SANS AUCUNE
#  without even the implied             GARANTIE : sans même la garantie
#  warranty of MERCHANTABILITY          implicite de COMMERCIALISABILITÉ
#  or FITNESS FOR A PARTICULAR          ni d’ADÉQUATION À UN OBJECTIF
#  PURPOSE.  See the GNU Affero         PARTICULIER. Consultez la Licence
#  General Public License for           Générale Publique GNU Affero
#  more details.                        pour plus de détails.
#
#  You should have received             Vous devriez avoir reçu une
#  a copy of the GNU Affero             copie de la Licence Générale
#  General Public License along         Publique GNU Affero avec
#  with OpenCADC.  If not, see          OpenCADC ; si ce n’est
#  <http://www.gnu.org/licenses/>.      pas le cas, consultez :
#                                       <http://www.gnu.org/licenses/>.
#
#
# ***********************************************************************

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import unittest
import pytest
from six import assertRaisesRegex

from cadcutils.net import wscapabilities


class TestWsCapabilities(unittest.TestCase):
    def test_parsing(self):
        # tests some error cases
        cr = wscapabilities.CapabilitiesReader()
        with self.assertRaises(ValueError):
            cr.parsexml('blah')

        with assertRaisesRegex(
                self, ValueError,
                'BUG reading remote service info '
                r'\(capabilities\) - No actual capabilities found'):
            cr.parsexml('<capabilities></capabilities>')

        with assertRaisesRegex(self, ValueError,
                               r'Cannot read service info \(capabilities\). '
                               'Capability standard ID is invalid URL: None'):
            cr.parsexml(
                '<capabilities><capability></capability></capabilities>')

        with assertRaisesRegex(self, ValueError,
                               r'Cannot read service info \(capabilities\). '
                               'Capability standard ID is invalid URL: abc'):
            cr.parsexml(
                '<capabilities><capability '
                'standardID="abc"></capability></capabilities>')

        with assertRaisesRegex(self, ValueError,
                               r'BUG reading service info \(capabilities\). '
                               'No interfaces found for capability '
                               'ivo://provider/service'):
            cr.parsexml(
                '<capabilities><capability '
                'standardID="ivo://provider/service">'
                '</capability></capabilities>')

        with assertRaisesRegex(
            self, ValueError,
                r'Cannot read service info \(capabilities\). '
                'No accessURL for ivo://provider/service'):
            cr.parsexml(
                '<capabilities '
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                '<capability standardID="ivo://provider/service">'
                '<interface xsi:type="vs:ParamHTTP">'
                '</interface></capability></capabilities>')

        with assertRaisesRegex(
                self, ValueError,
                r'Cannot read service info \(capabilities\). '
                'No accessURL for ivo://provider/service'):
            cr.parsexml(
                '<capabilities xmlns:xsi="ns"><capability '
                'standardID="ivo://provider/service">'
                '<interface></interface><accessURL>'
                '</accessURL></capability></capabilities>')

        with assertRaisesRegex(self, ValueError,
                               r'Cannot read service info \(capabilities\). '
                               'No accessURL for ivo://provider/service'):
            cr.parsexml(
                '<capabilities '
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                '<capability '
                'standardID="ivo://provider/service">'
                '<interface xsi:type="vs:ParamHTTP">'
                '<accessURL standardID="abc">'
                '</accessURL></interface></capability></capabilities>')

        # simplest capabilities document that parses successfully
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath'
            '</accessURL></interface></capability></capabilities>')

        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service', None)

        # multiple interfaces => go to the first one
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>https://someurl/somepath'
            '</accessURL></interface>'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath'
            '</accessURL></interface></capability></capabilities>')

        assert 'https://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service', None)

        # multiple interfaces => https url preferred even when change order
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface  xsi:type="vs:ParamHTTP">'
            '<accessURL>https://someurl/somepath'
            '</accessURL></interface>'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath'
            '</accessURL></interface></capability></capabilities>')

        assert 'https://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service', None)

        # multipel interfaces => first one chosen when both http or first one
        # is already https
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface  xsi:type="vs:ParamHTTP">'
            '<accessURL>https://someurl1/somepath'
            '</accessURL></interface>'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>https://someurl2/somepath'
            '</accessURL></interface></capability></capabilities>')

        assert 'https://someurl1/somepath' == \
               caps.get_access_url('ivo://provider/service', None)

        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl1/somepath'
            '</accessURL></interface><interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl2/somepath'
            '</accessURL></interface></capability></capabilities>')

        assert 'http://someurl1/somepath' == \
               caps.get_access_url('ivo://provider/service', None)

        # add security method
        caps = cr.parsexml(
                '<capabilities '
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                '<capability '
                'standardID="ivo://provider/service">'
                '<interface xsi:type="vs:ParamHTTP">'
                '<accessURL>http://someurl/somepath'
                '</accessURL><securityMethod></securityMethod>'
                '</interface></capability></capabilities>')

        assert 'http://someurl/somepath' == \
            caps.get_access_url('ivo://provider/service', None)

        # multiple security methods TAP1.0 style
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath1'
            '</accessURL><securityMethod standardID="ivo://cadc/mymethod1">'
            '</securityMethod></interface>'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath2'
            '</accessURL><securityMethod standardID="ivo://cadc/mymethod2">'
            '</securityMethod></interface>'
            '</capability></capabilities>')
        assert 'http://someurl/somepath1' == \
               caps.get_access_url('ivo://provider/service',
                                   ['ivo://cadc/mymethod1'])
        assert 'http://someurl/somepath2' == \
               caps.get_access_url('ivo://provider/service',
                                   ['ivo://cadc/mymethod2'])
        with pytest.raises(ValueError):
            assert caps.get_access_url('ivo://provider/service', None)

        # multiple security methods TAP1.1 style
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath'
            '</accessURL>'
            '<securityMethod standardID="ivo://cadc/mymethod1">'
            '</securityMethod>'
            '<securityMethod standardID="ivo://cadc/mymethod2">'
            '</securityMethod></interface>'
            '</capability></capabilities>')
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service',
                                   ['ivo://cadc/mymethod1'])
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service',
                                   ['ivo://cadc/mymethod2'])
        with pytest.raises(ValueError):
            assert caps.get_access_url('ivo://provider/service', None)

        # similar with the above test except anonymous security method
        # accepted
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath'
            '</accessURL>'
            '<securityMethod standardID="ivo://cadc/mymethod1">'
            '</securityMethod>'
            '<securityMethod/>'
            '<securityMethod standardID="ivo://cadc/mymethod2">'
            '</securityMethod></interface>'
            '</capability></capabilities>')
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service',
                                   ['ivo://cadc/mymethod1'])
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service',
                                   ['ivo://cadc/mymethod2'])
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service', None)
        # unlisted security method would be treated as anonymous
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service',
                                   ['ivo://cadc/mymethod3'])

        # test only anonymous TAP1.0 style
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath'
            '</accessURL>'
            '</interface>'
            '</capability></capabilities>')
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service', None)
        with pytest.raises(ValueError):
            assert caps.get_access_url('ivo://provider/service', "anymethod")

        # test only anonymous TAP1.1 style
        caps = cr.parsexml(
            '<capabilities '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<capability standardID="ivo://provider/service">'
            '<interface xsi:type="vs:ParamHTTP">'
            '<accessURL>http://someurl/somepath'
            '</accessURL>'
            '<securityMethod />'
            '</interface>'
            '</capability></capabilities>')
        assert 'http://someurl/somepath' == \
               caps.get_access_url('ivo://provider/service', None)
        with pytest.raises(ValueError):
            assert caps.get_access_url('ivo://provider/service', "anymethod")
