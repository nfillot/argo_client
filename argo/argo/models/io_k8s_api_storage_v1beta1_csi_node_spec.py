# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from argo.models.io_k8s_api_storage_v1beta1_csi_node_driver import IoK8sApiStorageV1beta1CSINodeDriver  # noqa: F401,E501


class IoK8sApiStorageV1beta1CSINodeSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'drivers': 'list[IoK8sApiStorageV1beta1CSINodeDriver]'
    }

    attribute_map = {
        'drivers': 'drivers'
    }

    def __init__(self, drivers=None):  # noqa: E501
        """IoK8sApiStorageV1beta1CSINodeSpec - a model defined in Swagger"""  # noqa: E501
        self._drivers = None
        self.discriminator = None
        self.drivers = drivers

    @property
    def drivers(self):
        """Gets the drivers of this IoK8sApiStorageV1beta1CSINodeSpec.  # noqa: E501

        drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.  # noqa: E501

        :return: The drivers of this IoK8sApiStorageV1beta1CSINodeSpec.  # noqa: E501
        :rtype: list[IoK8sApiStorageV1beta1CSINodeDriver]
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this IoK8sApiStorageV1beta1CSINodeSpec.

        drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.  # noqa: E501

        :param drivers: The drivers of this IoK8sApiStorageV1beta1CSINodeSpec.  # noqa: E501
        :type: list[IoK8sApiStorageV1beta1CSINodeDriver]
        """
        if drivers is None:
            raise ValueError("Invalid value for `drivers`, must not be `None`")  # noqa: E501

        self._drivers = drivers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IoK8sApiStorageV1beta1CSINodeSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApiStorageV1beta1CSINodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
