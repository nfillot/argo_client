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
from api.authentication_v1beta1_api import AuthenticationV1beta1Api  # noqa: E501
from argo.rest import ApiException


class TestAuthenticationV1beta1Api(unittest.TestCase):
    """AuthenticationV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = api.authentication_v1beta1_api.AuthenticationV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_authentication_v1beta1_token_review(self):
        """Test case for create_authentication_v1beta1_token_review

        """
        pass

    def test_get_authentication_v1beta1_api_resources(self):
        """Test case for get_authentication_v1beta1_api_resources

        """
        pass


if __name__ == '__main__':
    unittest.main()
