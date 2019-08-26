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
from argo.models.io_k8s_api_core_v1_secret_key_selector import IoK8sApiCoreV1SecretKeySelector  # noqa: F401,E501


class IoArgoprojWorkflowV1alpha1ArtifactoryArtifact(object):
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
        'password_secret': 'IoK8sApiCoreV1SecretKeySelector',
        'url': 'str',
        'username_secret': 'IoK8sApiCoreV1SecretKeySelector'
    }

    attribute_map = {
        'password_secret': 'passwordSecret',
        'url': 'url',
        'username_secret': 'usernameSecret'
    }

    def __init__(self, password_secret=None, url=None, username_secret=None):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1ArtifactoryArtifact - a model defined in Swagger"""  # noqa: E501
        self._password_secret = None
        self._url = None
        self._username_secret = None
        self.discriminator = None
        if password_secret is not None:
            self.password_secret = password_secret
        self.url = url
        if username_secret is not None:
            self.username_secret = username_secret

    @property
    def password_secret(self):
        """Gets the password_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501


        :return: The password_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._password_secret

    @password_secret.setter
    def password_secret(self, password_secret):
        """Sets the password_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.


        :param password_secret: The password_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._password_secret = password_secret

    @property
    def url(self):
        """Gets the url of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501

        URL of the artifact  # noqa: E501

        :return: The url of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.

        URL of the artifact  # noqa: E501

        :param url: The url of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def username_secret(self):
        """Gets the username_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501


        :return: The username_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501
        :rtype: IoK8sApiCoreV1SecretKeySelector
        """
        return self._username_secret

    @username_secret.setter
    def username_secret(self, username_secret):
        """Sets the username_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.


        :param username_secret: The username_secret of this IoArgoprojWorkflowV1alpha1ArtifactoryArtifact.  # noqa: E501
        :type: IoK8sApiCoreV1SecretKeySelector
        """

        self._username_secret = username_secret

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
        if issubclass(IoArgoprojWorkflowV1alpha1ArtifactoryArtifact, dict):
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
        if not isinstance(other, IoArgoprojWorkflowV1alpha1ArtifactoryArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
