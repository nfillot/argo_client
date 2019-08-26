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
from argo.models.io_k8s_api_authentication_v1_user_info import IoK8sApiAuthenticationV1UserInfo  # noqa: F401,E501


class IoK8sApiAuthenticationV1TokenReviewStatus(object):
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
        'audiences': 'list[str]',
        'authenticated': 'bool',
        'error': 'str',
        'user': 'IoK8sApiAuthenticationV1UserInfo'
    }

    attribute_map = {
        'audiences': 'audiences',
        'authenticated': 'authenticated',
        'error': 'error',
        'user': 'user'
    }

    def __init__(self, audiences=None, authenticated=None, error=None, user=None):  # noqa: E501
        """IoK8sApiAuthenticationV1TokenReviewStatus - a model defined in Swagger"""  # noqa: E501
        self._audiences = None
        self._authenticated = None
        self._error = None
        self._user = None
        self.discriminator = None
        if audiences is not None:
            self.audiences = audiences
        if authenticated is not None:
            self.authenticated = authenticated
        if error is not None:
            self.error = error
        if user is not None:
            self.user = user

    @property
    def audiences(self):
        """Gets the audiences of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501

        Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is \"true\", the token is valid against the audience of the Kubernetes API server.  # noqa: E501

        :return: The audiences of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this IoK8sApiAuthenticationV1TokenReviewStatus.

        Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is \"true\", the token is valid against the audience of the Kubernetes API server.  # noqa: E501

        :param audiences: The audiences of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :type: list[str]
        """

        self._audiences = audiences

    @property
    def authenticated(self):
        """Gets the authenticated of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501

        Authenticated indicates that the token was associated with a known user.  # noqa: E501

        :return: The authenticated of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :rtype: bool
        """
        return self._authenticated

    @authenticated.setter
    def authenticated(self, authenticated):
        """Sets the authenticated of this IoK8sApiAuthenticationV1TokenReviewStatus.

        Authenticated indicates that the token was associated with a known user.  # noqa: E501

        :param authenticated: The authenticated of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :type: bool
        """

        self._authenticated = authenticated

    @property
    def error(self):
        """Gets the error of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501

        Error indicates that the token couldn't be checked  # noqa: E501

        :return: The error of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this IoK8sApiAuthenticationV1TokenReviewStatus.

        Error indicates that the token couldn't be checked  # noqa: E501

        :param error: The error of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def user(self):
        """Gets the user of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501


        :return: The user of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :rtype: IoK8sApiAuthenticationV1UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this IoK8sApiAuthenticationV1TokenReviewStatus.


        :param user: The user of this IoK8sApiAuthenticationV1TokenReviewStatus.  # noqa: E501
        :type: IoK8sApiAuthenticationV1UserInfo
        """

        self._user = user

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
        if issubclass(IoK8sApiAuthenticationV1TokenReviewStatus, dict):
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
        if not isinstance(other, IoK8sApiAuthenticationV1TokenReviewStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
