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
from argo.models.io_k8s_api_admissionregistration_v1beta1_service_reference import IoK8sApiAdmissionregistrationV1beta1ServiceReference  # noqa: F401,E501


class IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig(object):
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
        'ca_bundle': 'str',
        'service': 'IoK8sApiAdmissionregistrationV1beta1ServiceReference',
        'url': 'str'
    }

    attribute_map = {
        'ca_bundle': 'caBundle',
        'service': 'service',
        'url': 'url'
    }

    def __init__(self, ca_bundle=None, service=None, url=None):  # noqa: E501
        """IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig - a model defined in Swagger"""  # noqa: E501
        self._ca_bundle = None
        self._service = None
        self._url = None
        self.discriminator = None
        if ca_bundle is not None:
            self.ca_bundle = ca_bundle
        if service is not None:
            self.service = service
        if url is not None:
            self.url = url

    @property
    def ca_bundle(self):
        """Gets the ca_bundle of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501

        `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used.  # noqa: E501

        :return: The ca_bundle of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501
        :rtype: str
        """
        return self._ca_bundle

    @ca_bundle.setter
    def ca_bundle(self, ca_bundle):
        """Sets the ca_bundle of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.

        `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used.  # noqa: E501

        :param ca_bundle: The ca_bundle of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501
        :type: str
        """

        self._ca_bundle = ca_bundle

    @property
    def service(self):
        """Gets the service of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501


        :return: The service of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501
        :rtype: IoK8sApiAdmissionregistrationV1beta1ServiceReference
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.


        :param service: The service of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501
        :type: IoK8sApiAdmissionregistrationV1beta1ServiceReference
        """

        self._service = service

    @property
    def url(self):
        """Gets the url of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501

        `url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \"https\"; the URL must begin with \"https://\".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \"user:password@\" is not allowed. Fragments (\"#...\") and query parameters (\"?...\") are not allowed, either.  # noqa: E501

        :return: The url of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.

        `url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be \"https\"; the URL must begin with \"https://\".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. \"user:password@\" is not allowed. Fragments (\"#...\") and query parameters (\"?...\") are not allowed, either.  # noqa: E501

        :param url: The url of this IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig, dict):
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
        if not isinstance(other, IoK8sApiAdmissionregistrationV1beta1WebhookClientConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
