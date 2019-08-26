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


class IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale(object):
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
        'label_selector_path': 'str',
        'spec_replicas_path': 'str',
        'status_replicas_path': 'str'
    }

    attribute_map = {
        'label_selector_path': 'labelSelectorPath',
        'spec_replicas_path': 'specReplicasPath',
        'status_replicas_path': 'statusReplicasPath'
    }

    def __init__(self, label_selector_path=None, spec_replicas_path=None, status_replicas_path=None):  # noqa: E501
        """IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale - a model defined in Swagger"""  # noqa: E501
        self._label_selector_path = None
        self._spec_replicas_path = None
        self._status_replicas_path = None
        self.discriminator = None
        if label_selector_path is not None:
            self.label_selector_path = label_selector_path
        self.spec_replicas_path = spec_replicas_path
        self.status_replicas_path = status_replicas_path

    @property
    def label_selector_path(self):
        """Gets the label_selector_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501

        LabelSelectorPath defines the JSON path inside of a CustomResource that corresponds to Scale.Status.Selector. Only JSON paths without the array notation are allowed. Must be a JSON Path under .status. Must be set to work with HPA. If there is no value under the given path in the CustomResource, the status label selector value in the /scale subresource will default to the empty string.  # noqa: E501

        :return: The label_selector_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501
        :rtype: str
        """
        return self._label_selector_path

    @label_selector_path.setter
    def label_selector_path(self, label_selector_path):
        """Sets the label_selector_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.

        LabelSelectorPath defines the JSON path inside of a CustomResource that corresponds to Scale.Status.Selector. Only JSON paths without the array notation are allowed. Must be a JSON Path under .status. Must be set to work with HPA. If there is no value under the given path in the CustomResource, the status label selector value in the /scale subresource will default to the empty string.  # noqa: E501

        :param label_selector_path: The label_selector_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501
        :type: str
        """

        self._label_selector_path = label_selector_path

    @property
    def spec_replicas_path(self):
        """Gets the spec_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501

        SpecReplicasPath defines the JSON path inside of a CustomResource that corresponds to Scale.Spec.Replicas. Only JSON paths without the array notation are allowed. Must be a JSON Path under .spec. If there is no value under the given path in the CustomResource, the /scale subresource will return an error on GET.  # noqa: E501

        :return: The spec_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501
        :rtype: str
        """
        return self._spec_replicas_path

    @spec_replicas_path.setter
    def spec_replicas_path(self, spec_replicas_path):
        """Sets the spec_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.

        SpecReplicasPath defines the JSON path inside of a CustomResource that corresponds to Scale.Spec.Replicas. Only JSON paths without the array notation are allowed. Must be a JSON Path under .spec. If there is no value under the given path in the CustomResource, the /scale subresource will return an error on GET.  # noqa: E501

        :param spec_replicas_path: The spec_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501
        :type: str
        """
        if spec_replicas_path is None:
            raise ValueError("Invalid value for `spec_replicas_path`, must not be `None`")  # noqa: E501

        self._spec_replicas_path = spec_replicas_path

    @property
    def status_replicas_path(self):
        """Gets the status_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501

        StatusReplicasPath defines the JSON path inside of a CustomResource that corresponds to Scale.Status.Replicas. Only JSON paths without the array notation are allowed. Must be a JSON Path under .status. If there is no value under the given path in the CustomResource, the status replica value in the /scale subresource will default to 0.  # noqa: E501

        :return: The status_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501
        :rtype: str
        """
        return self._status_replicas_path

    @status_replicas_path.setter
    def status_replicas_path(self, status_replicas_path):
        """Sets the status_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.

        StatusReplicasPath defines the JSON path inside of a CustomResource that corresponds to Scale.Status.Replicas. Only JSON paths without the array notation are allowed. Must be a JSON Path under .status. If there is no value under the given path in the CustomResource, the status replica value in the /scale subresource will default to 0.  # noqa: E501

        :param status_replicas_path: The status_replicas_path of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale.  # noqa: E501
        :type: str
        """
        if status_replicas_path is None:
            raise ValueError("Invalid value for `status_replicas_path`, must not be `None`")  # noqa: E501

        self._status_replicas_path = status_replicas_path

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
        if issubclass(IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale, dict):
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
        if not isinstance(other, IoK8sApiextensionsApiserverPkgApisApiextensionsV1beta1CustomResourceSubresourceScale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
