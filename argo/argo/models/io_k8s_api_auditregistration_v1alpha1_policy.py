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


class IoK8sApiAuditregistrationV1alpha1Policy(object):
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
        'level': 'str',
        'stages': 'list[str]'
    }

    attribute_map = {
        'level': 'level',
        'stages': 'stages'
    }

    def __init__(self, level=None, stages=None):  # noqa: E501
        """IoK8sApiAuditregistrationV1alpha1Policy - a model defined in Swagger"""  # noqa: E501
        self._level = None
        self._stages = None
        self.discriminator = None
        self.level = level
        if stages is not None:
            self.stages = stages

    @property
    def level(self):
        """Gets the level of this IoK8sApiAuditregistrationV1alpha1Policy.  # noqa: E501

        The Level that all requests are recorded at. available options: None, Metadata, Request, RequestResponse required  # noqa: E501

        :return: The level of this IoK8sApiAuditregistrationV1alpha1Policy.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this IoK8sApiAuditregistrationV1alpha1Policy.

        The Level that all requests are recorded at. available options: None, Metadata, Request, RequestResponse required  # noqa: E501

        :param level: The level of this IoK8sApiAuditregistrationV1alpha1Policy.  # noqa: E501
        :type: str
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def stages(self):
        """Gets the stages of this IoK8sApiAuditregistrationV1alpha1Policy.  # noqa: E501

        Stages is a list of stages for which events are created.  # noqa: E501

        :return: The stages of this IoK8sApiAuditregistrationV1alpha1Policy.  # noqa: E501
        :rtype: list[str]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this IoK8sApiAuditregistrationV1alpha1Policy.

        Stages is a list of stages for which events are created.  # noqa: E501

        :param stages: The stages of this IoK8sApiAuditregistrationV1alpha1Policy.  # noqa: E501
        :type: list[str]
        """

        self._stages = stages

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
        if issubclass(IoK8sApiAuditregistrationV1alpha1Policy, dict):
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
        if not isinstance(other, IoK8sApiAuditregistrationV1alpha1Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
