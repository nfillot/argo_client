# coding: utf-8

"""
    Argo

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class IoArgoprojWorkflowV1alpha1RetryStrategy(object):
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
        'limit': 'int'
    }

    attribute_map = {
        'limit': 'limit'
    }

    def __init__(self, limit=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1RetryStrategy - a model defined in Swagger"""  # noqa: E501
        self._limit = None
        self.discriminator = None
        if limit is not None:
            self.limit = limit

    @property
    def limit(self):
        """Gets the limit of this IoArgoprojWorkflowV1alpha1RetryStrategy.  # noqa: E501

        Limit is the maximum number of attempts when retrying a container  # noqa: E501

        :return: The limit of this IoArgoprojWorkflowV1alpha1RetryStrategy.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this IoArgoprojWorkflowV1alpha1RetryStrategy.

        Limit is the maximum number of attempts when retrying a container  # noqa: E501

        :param limit: The limit of this IoArgoprojWorkflowV1alpha1RetryStrategy.  # noqa: E501
        :type: int
        """

        self._limit = limit

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
        if issubclass(IoArgoprojWorkflowV1alpha1RetryStrategy, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1RetryStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other