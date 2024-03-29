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
from argo.models.io_k8s_api_core_v1_object_reference import IoK8sApiCoreV1ObjectReference  # noqa: F401,E501
from argo.models.io_k8s_apimachinery_pkg_apis_meta_v1_time import IoK8sApimachineryPkgApisMetaV1Time  # noqa: F401,E501


class IoK8sApiBatchV2alpha1CronJobStatus(object):
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
        'active': 'list[IoK8sApiCoreV1ObjectReference]',
        'last_schedule_time': 'IoK8sApimachineryPkgApisMetaV1Time'
    }

    attribute_map = {
        'active': 'active',
        'last_schedule_time': 'lastScheduleTime'
    }

    def __init__(self, active=None, last_schedule_time=None):  # noqa: E501
        """IoK8sApiBatchV2alpha1CronJobStatus - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._last_schedule_time = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if last_schedule_time is not None:
            self.last_schedule_time = last_schedule_time

    @property
    def active(self):
        """Gets the active of this IoK8sApiBatchV2alpha1CronJobStatus.  # noqa: E501

        A list of pointers to currently running jobs.  # noqa: E501

        :return: The active of this IoK8sApiBatchV2alpha1CronJobStatus.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1ObjectReference]
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this IoK8sApiBatchV2alpha1CronJobStatus.

        A list of pointers to currently running jobs.  # noqa: E501

        :param active: The active of this IoK8sApiBatchV2alpha1CronJobStatus.  # noqa: E501
        :type: list[IoK8sApiCoreV1ObjectReference]
        """

        self._active = active

    @property
    def last_schedule_time(self):
        """Gets the last_schedule_time of this IoK8sApiBatchV2alpha1CronJobStatus.  # noqa: E501


        :return: The last_schedule_time of this IoK8sApiBatchV2alpha1CronJobStatus.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._last_schedule_time

    @last_schedule_time.setter
    def last_schedule_time(self, last_schedule_time):
        """Sets the last_schedule_time of this IoK8sApiBatchV2alpha1CronJobStatus.


        :param last_schedule_time: The last_schedule_time of this IoK8sApiBatchV2alpha1CronJobStatus.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._last_schedule_time = last_schedule_time

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
        if issubclass(IoK8sApiBatchV2alpha1CronJobStatus, dict):
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
        if not isinstance(other, IoK8sApiBatchV2alpha1CronJobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
