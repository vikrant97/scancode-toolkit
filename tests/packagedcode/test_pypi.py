#
# Copyright (c) 2015 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function

import os.path
import shutil


from commoncode.testcase import FileBasedTesting
from packagedcode import pypi


class TestPyPi(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_parse(self):
        test_file = self.get_test_loc('pypi/setup.py')
        package = pypi.parse(test_file)
        assert 'scancode-toolkit' == package.name
        assert '1.5.0' == package.version
        assert 'ScanCode' == package.authors[0].name
        assert 'ScanCode is a tool to scan code for license, copyright and other interesting facts.' == package.description
        assert 'https://github.com/nexB/scancode-toolkit' == package.homepage_url

    def test_get_attribute(self):
        test_input = self.get_test_loc('pypi/setup2.py')
        test_file = self.get_temp_file('setup.py')
        shutil.copyfile(test_input, test_file)
        assert 'scancode-toolkit' == pypi.get_attribute(test_file, 'name')
        assert '1.5.0' == pypi.get_attribute(test_file, 'version')
        assert 'ScanCode' == pypi.get_attribute(test_file, 'author')

    def test_parse_metadata(self):
        test_folder = self.get_test_loc('pypi')
        test_file = os.path.join(test_folder, 'metadata.json')
        package = pypi.parse_metadata(test_file)
        assert 'six' == package.name
        assert '1.10.0' == package.version
        assert 'Python 2 and 3 compatibility utilities' == package.summary
        assert 'MIT' == package.asserted_licenses[0].license
        assert 'Benjamin Peterson' == package.authors[0].name
        assert 'http://pypi.python.org/pypi/six/' == package.homepage_url

    def test_parse_pkg_info(self):
        test_file = self.get_test_loc('pypi/PKG-INFO')
        package = pypi.parse_pkg_info(test_file)
        assert 'TicketImport' == package.name
        assert '0.7a' == package.version
        assert 'Import CSV and Excel files' == package.summary
        assert 'BSD' == package.asserted_licenses[0].license
        assert 'http://nexb.com' == package.homepage_url
        assert 'Francois Granade' == package.authors[0].name
