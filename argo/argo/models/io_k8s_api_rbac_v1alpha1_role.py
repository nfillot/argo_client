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
from argo.models.io_k8s_api_rbac_v1alpha1_policy_rule import IoK8sApiRbacV1alpha1PolicyRule  # noqa: F401,E501
from argo.models.io_k8s_apimachinery_pkg_apis_meta_v1_object_meta import IoK8sApimachineryPkgApisMetaV1ObjectMeta  # noqa: F401,E501


class IoK8sApiRbacV1alpha1Role(object):
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
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'IoK8sApimachineryPkgApisMetaV1ObjectMeta',
        'rules': 'list[IoK8sApiRbacV1alpha1PolicyRule]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'rules': 'rules'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, rules=None):  # noqa: E501
        """IoK8sApiRbacV1alpha1Role - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._kind = None
        self._metadata = None
        self._rules = None
        self.discriminator = None
        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if rules is not None:
            self.rules = rules

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApiRbacV1alpha1Role.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApiRbacV1alpha1Role.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this IoK8sApiRbacV1alpha1Role.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoK8sApiRbacV1alpha1Role.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this IoK8sApiRbacV1alpha1Role.  # noqa: E501


        :return: The metadata of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IoK8sApiRbacV1alpha1Role.


        :param metadata: The metadata of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """

        self._metadata = metadata

    @property
    def rules(self):
        """Gets the rules of this IoK8sApiRbacV1alpha1Role.  # noqa: E501

        Rules holds all the PolicyRules for this Role  # noqa: E501

        :return: The rules of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :rtype: list[IoK8sApiRbacV1alpha1PolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this IoK8sApiRbacV1alpha1Role.

        Rules holds all the PolicyRules for this Role  # noqa: E501

        :param rules: The rules of this IoK8sApiRbacV1alpha1Role.  # noqa: E501
        :type: list[IoK8sApiRbacV1alpha1PolicyRule]
        """

        self._rules = rules

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
        if issubclass(IoK8sApiRbacV1alpha1Role, dict):
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
        if not isinstance(other, IoK8sApiRbacV1alpha1Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
