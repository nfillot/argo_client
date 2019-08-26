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
from argo.models.io_k8s_apimachinery_pkg_apis_meta_v1_initializers import IoK8sApimachineryPkgApisMetaV1Initializers  # noqa: F401,E501
from argo.models.io_k8s_apimachinery_pkg_apis_meta_v1_managed_fields_entry import IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry  # noqa: F401,E501
from argo.models.io_k8s_apimachinery_pkg_apis_meta_v1_owner_reference import IoK8sApimachineryPkgApisMetaV1OwnerReference  # noqa: F401,E501
from argo.models.io_k8s_apimachinery_pkg_apis_meta_v1_time import IoK8sApimachineryPkgApisMetaV1Time  # noqa: F401,E501


class IoK8sApimachineryPkgApisMetaV1ObjectMeta(object):
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
        'annotations': 'dict(str, str)',
        'cluster_name': 'str',
        'creation_timestamp': 'IoK8sApimachineryPkgApisMetaV1Time',
        'deletion_grace_period_seconds': 'int',
        'deletion_timestamp': 'IoK8sApimachineryPkgApisMetaV1Time',
        'finalizers': 'list[str]',
        'generate_name': 'str',
        'generation': 'int',
        'initializers': 'IoK8sApimachineryPkgApisMetaV1Initializers',
        'labels': 'dict(str, str)',
        'managed_fields': 'list[IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry]',
        'name': 'str',
        'namespace': 'str',
        'owner_references': 'list[IoK8sApimachineryPkgApisMetaV1OwnerReference]',
        'resource_version': 'str',
        'self_link': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'cluster_name': 'clusterName',
        'creation_timestamp': 'creationTimestamp',
        'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',
        'deletion_timestamp': 'deletionTimestamp',
        'finalizers': 'finalizers',
        'generate_name': 'generateName',
        'generation': 'generation',
        'initializers': 'initializers',
        'labels': 'labels',
        'managed_fields': 'managedFields',
        'name': 'name',
        'namespace': 'namespace',
        'owner_references': 'ownerReferences',
        'resource_version': 'resourceVersion',
        'self_link': 'selfLink',
        'uid': 'uid'
    }

    def __init__(self, annotations=None, cluster_name=None, creation_timestamp=None, deletion_grace_period_seconds=None, deletion_timestamp=None, finalizers=None, generate_name=None, generation=None, initializers=None, labels=None, managed_fields=None, name=None, namespace=None, owner_references=None, resource_version=None, self_link=None, uid=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1ObjectMeta - a model defined in Swagger"""  # noqa: E501
        self._annotations = None
        self._cluster_name = None
        self._creation_timestamp = None
        self._deletion_grace_period_seconds = None
        self._deletion_timestamp = None
        self._finalizers = None
        self._generate_name = None
        self._generation = None
        self._initializers = None
        self._labels = None
        self._managed_fields = None
        self._name = None
        self._namespace = None
        self._owner_references = None
        self._resource_version = None
        self._self_link = None
        self._uid = None
        self.discriminator = None
        if annotations is not None:
            self.annotations = annotations
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if deletion_grace_period_seconds is not None:
            self.deletion_grace_period_seconds = deletion_grace_period_seconds
        if deletion_timestamp is not None:
            self.deletion_timestamp = deletion_timestamp
        if finalizers is not None:
            self.finalizers = finalizers
        if generate_name is not None:
            self.generate_name = generate_name
        if generation is not None:
            self.generation = generation
        if initializers is not None:
            self.initializers = initializers
        if labels is not None:
            self.labels = labels
        if managed_fields is not None:
            self.managed_fields = managed_fields
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if owner_references is not None:
            self.owner_references = owner_references
        if resource_version is not None:
            self.resource_version = resource_version
        if self_link is not None:
            self.self_link = self_link
        if uid is not None:
            self.uid = uid

    @property
    def annotations(self):
        """Gets the annotations of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations  # noqa: E501

        :return: The annotations of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations  # noqa: E501

        :param annotations: The annotations of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def cluster_name(self):
        """Gets the cluster_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.  # noqa: E501

        :return: The cluster_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.  # noqa: E501

        :param cluster_name: The cluster_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501


        :return: The creation_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.


        :param creation_timestamp: The creation_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._creation_timestamp = creation_timestamp

    @property
    def deletion_grace_period_seconds(self):
        """Gets the deletion_grace_period_seconds of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.  # noqa: E501

        :return: The deletion_grace_period_seconds of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: int
        """
        return self._deletion_grace_period_seconds

    @deletion_grace_period_seconds.setter
    def deletion_grace_period_seconds(self, deletion_grace_period_seconds):
        """Sets the deletion_grace_period_seconds of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.  # noqa: E501

        :param deletion_grace_period_seconds: The deletion_grace_period_seconds of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: int
        """

        self._deletion_grace_period_seconds = deletion_grace_period_seconds

    @property
    def deletion_timestamp(self):
        """Gets the deletion_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501


        :return: The deletion_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._deletion_timestamp

    @deletion_timestamp.setter
    def deletion_timestamp(self, deletion_timestamp):
        """Sets the deletion_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.


        :param deletion_timestamp: The deletion_timestamp of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """

        self._deletion_timestamp = deletion_timestamp

    @property
    def finalizers(self):
        """Gets the finalizers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed.  # noqa: E501

        :return: The finalizers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: list[str]
        """
        return self._finalizers

    @finalizers.setter
    def finalizers(self, finalizers):
        """Sets the finalizers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed.  # noqa: E501

        :param finalizers: The finalizers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: list[str]
        """

        self._finalizers = finalizers

    @property
    def generate_name(self):
        """Gets the generate_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#idempotency  # noqa: E501

        :return: The generate_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._generate_name

    @generate_name.setter
    def generate_name(self, generate_name):
        """Sets the generate_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#idempotency  # noqa: E501

        :param generate_name: The generate_name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._generate_name = generate_name

    @property
    def generation(self):
        """Gets the generation of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.  # noqa: E501

        :return: The generation of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.  # noqa: E501

        :param generation: The generation of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def initializers(self):
        """Gets the initializers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501


        :return: The initializers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Initializers
        """
        return self._initializers

    @initializers.setter
    def initializers(self, initializers):
        """Sets the initializers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.


        :param initializers: The initializers of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Initializers
        """

        self._initializers = initializers

    @property
    def labels(self):
        """Gets the labels of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels  # noqa: E501

        :return: The labels of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels  # noqa: E501

        :param labels: The labels of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def managed_fields(self):
        """Gets the managed_fields of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object.  This field is alpha and can be changed or removed without notice.  # noqa: E501

        :return: The managed_fields of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: list[IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry]
        """
        return self._managed_fields

    @managed_fields.setter
    def managed_fields(self, managed_fields):
        """Sets the managed_fields of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like \"ci-cd\". The set of fields is always in the version that the workflow used when modifying the object.  This field is alpha and can be changed or removed without notice.  # noqa: E501

        :param managed_fields: The managed_fields of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: list[IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry]
        """

        self._managed_fields = managed_fields

    @property
    def name(self):
        """Gets the name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names  # noqa: E501

        :return: The name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names  # noqa: E501

        :param name: The name of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces  # noqa: E501

        :return: The namespace of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces  # noqa: E501

        :param namespace: The namespace of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def owner_references(self):
        """Gets the owner_references of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.  # noqa: E501

        :return: The owner_references of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: list[IoK8sApimachineryPkgApisMetaV1OwnerReference]
        """
        return self._owner_references

    @owner_references.setter
    def owner_references(self, owner_references):
        """Sets the owner_references of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.  # noqa: E501

        :param owner_references: The owner_references of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: list[IoK8sApimachineryPkgApisMetaV1OwnerReference]
        """

        self._owner_references = owner_references

    @property
    def resource_version(self):
        """Gets the resource_version of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency  # noqa: E501

        :return: The resource_version of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency  # noqa: E501

        :param resource_version: The resource_version of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def self_link(self):
        """Gets the self_link of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        SelfLink is a URL representing this object. Populated by the system. Read-only.  # noqa: E501

        :return: The self_link of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """Sets the self_link of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        SelfLink is a URL representing this object. Populated by the system. Read-only.  # noqa: E501

        :param self_link: The self_link of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._self_link = self_link

    @property
    def uid(self):
        """Gets the uid of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501

        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids  # noqa: E501

        :return: The uid of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.

        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids  # noqa: E501

        :param uid: The uid of this IoK8sApimachineryPkgApisMetaV1ObjectMeta.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(IoK8sApimachineryPkgApisMetaV1ObjectMeta, dict):
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
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1ObjectMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
