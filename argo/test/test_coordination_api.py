# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import argo
from api.coordination_api import CoordinationApi  # noqa: E501
from argo.rest import ApiException


class TestCoordinationApi(unittest.TestCase):
    """CoordinationApi unit test stubs"""

    def setUp(self):
        self.api = api.coordination_api.CoordinationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_coordination_api_group(self):
        """Test case for get_coordination_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
