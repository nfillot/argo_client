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
from api.autoscaling_v2beta1_api import AutoscalingV2beta1Api  # noqa: E501
from argo.rest import ApiException


class TestAutoscalingV2beta1Api(unittest.TestCase):
    """AutoscalingV2beta1Api unit test stubs"""

    def setUp(self):
        self.api = api.autoscaling_v2beta1_api.AutoscalingV2beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for create_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_autoscaling_v2beta1_collection_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_autoscaling_v2beta1_collection_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_get_autoscaling_v2beta1_api_resources(self):
        """Test case for get_autoscaling_v2beta1_api_resources

        """
        pass

    def test_list_autoscaling_v2beta1_horizontal_pod_autoscaler_for_all_namespaces(self):
        """Test case for list_autoscaling_v2beta1_horizontal_pod_autoscaler_for_all_namespaces

        """
        pass

    def test_list_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for list_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for patch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for patch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_read_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for read_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_read_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for read_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_replace_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for replace_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_replace_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for replace_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_watch_autoscaling_v2beta1_horizontal_pod_autoscaler_list_for_all_namespaces(self):
        """Test case for watch_autoscaling_v2beta1_horizontal_pod_autoscaler_list_for_all_namespaces

        """
        pass

    def test_watch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler(self):
        """Test case for watch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_watch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_list(self):
        """Test case for watch_autoscaling_v2beta1_namespaced_horizontal_pod_autoscaler_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
