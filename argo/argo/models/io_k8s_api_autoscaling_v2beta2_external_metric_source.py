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
from argo.models.io_k8s_api_autoscaling_v2beta2_metric_target import IoK8sApiAutoscalingV2beta2MetricTarget  # noqa: F401,E501


class IoK8sApiAutoscalingV2beta2ExternalMetricSource(object):
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
        'metric': 'IoK8sApiAutoscalingV2beta2MetricIdentifier',
        'target': 'IoK8sApiAutoscalingV2beta2MetricTarget'
    }

    attribute_map = {
        'metric': 'metric',
        'target': 'target'
    }

    def __init__(self, metric=None, target=None):  # noqa: E501
        """IoK8sApiAutoscalingV2beta2ExternalMetricSource - a model defined in Swagger"""  # noqa: E501
        self._metric = None
        self._target = None
        self.discriminator = None
        self.metric = metric
        self.target = target

    @property
    def metric(self):
        """Gets the metric of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.  # noqa: E501


        :return: The metric of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2MetricIdentifier
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.


        :param metric: The metric of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2MetricIdentifier
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def target(self):
        """Gets the target of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.  # noqa: E501


        :return: The target of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2beta2MetricTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.


        :param target: The target of this IoK8sApiAutoscalingV2beta2ExternalMetricSource.  # noqa: E501
        :type: IoK8sApiAutoscalingV2beta2MetricTarget
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if issubclass(IoK8sApiAutoscalingV2beta2ExternalMetricSource, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV2beta2ExternalMetricSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
