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
from argo.models.io_k8s_apimachinery_pkg_api_resource_quantity import IoK8sApimachineryPkgApiResourceQuantity  # noqa: F401,E501
from argo.models.io_k8s_apimachinery_pkg_apis_meta_v1_label_selector import IoK8sApimachineryPkgApisMetaV1LabelSelector  # noqa: F401,E501


class IoK8sApiAutoscalingV2beta1PodsMetricSource(object):
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
        'metric_name': 'str',
        'selector': 'IoK8sApimachineryPkgApisMetaV1LabelSelector',
        'target_average_value': 'IoK8sApimachineryPkgApiResourceQuantity'
    }

    attribute_map = {
        'metric_name': 'metricName',
        'selector': 'selector',
        'target_average_value': 'targetAverageValue'
    }

    def __init__(self, metric_name=None, selector=None, target_average_value=None):  # noqa: E501
        """IoK8sApiAutoscalingV2beta1PodsMetricSource - a model defined in Swagger"""  # noqa: E501
        self._metric_name = None
        self._selector = None
        self._target_average_value = None
        self.discriminator = None
        self.metric_name = metric_name
        if selector is not None:
            self.selector = selector
        self.target_average_value = target_average_value

    @property
    def metric_name(self):
        """Gets the metric_name of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501

        metricName is the name of the metric in question  # noqa: E501

        :return: The metric_name of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this IoK8sApiAutoscalingV2beta1PodsMetricSource.

        metricName is the name of the metric in question  # noqa: E501

        :param metric_name: The metric_name of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def selector(self):
        """Gets the selector of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501


        :return: The selector of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this IoK8sApiAutoscalingV2beta1PodsMetricSource.


        :param selector: The selector of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1LabelSelector
        """

        self._selector = selector

    @property
    def target_average_value(self):
        """Gets the target_average_value of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501


        :return: The target_average_value of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApiResourceQuantity
        """
        return self._target_average_value

    @target_average_value.setter
    def target_average_value(self, target_average_value):
        """Sets the target_average_value of this IoK8sApiAutoscalingV2beta1PodsMetricSource.


        :param target_average_value: The target_average_value of this IoK8sApiAutoscalingV2beta1PodsMetricSource.  # noqa: E501
        :type: IoK8sApimachineryPkgApiResourceQuantity
        """
        if target_average_value is None:
            raise ValueError("Invalid value for `target_average_value`, must not be `None`")  # noqa: E501

        self._target_average_value = target_average_value

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
        if issubclass(IoK8sApiAutoscalingV2beta1PodsMetricSource, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV2beta1PodsMetricSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other