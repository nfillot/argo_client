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
from argo.models.io_k8s_api_autoscaling_v2beta2_metric_identifier import IoK8sApiAutoscalingV2beta2MetricIdentifier  # noqa: F401,E501
from argo.models.io_k8s_api_autoscaling_v2beta2_metric_value_status import IoK8sApiAutoscalingV2beta2MetricValueStatus  # noqa: F401,E501


class IoK8sApiAutoscalingV2beta2ExternalMetricStatus(object):
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
        'current': 'IoK8sApiAutoscalingV2beta2MetricValueStatus',
        'metric': 'IoK8sApiAutoscalingV2beta2MetricIdentifier'
    }

    attribute_map = {
        'current': 'current',
        'metric': 'metric'
    }

    def __init__(self, current=None, metric=None):  # noqa: E501
        """IoK8sApiAutoscalingV2beta2ExternalMetricStatus - a model defined in Swagger"""  # noqa: E501
        self._current = None
        self._metric = None
        self.discriminator = None
        self.current = current
        self.metric = metric

    @property
    def current(self):
        """Gets the current of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.  # noqa: E501


        :return: The current of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2MetricValueStatus
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.


        :param current: The current of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2MetricValueStatus
        """
        if current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")  # noqa: E501

        self._current = current

    @property
    def metric(self):
        """Gets the metric of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.  # noqa: E501


        :return: The metric of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2MetricIdentifier
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.


        :param metric: The metric of this IoK8sApiAutoscalingV2beta2ExternalMetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2MetricIdentifier
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

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
        if issubclass(IoK8sApiAutoscalingV2beta2ExternalMetricStatus, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV2beta2ExternalMetricStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
