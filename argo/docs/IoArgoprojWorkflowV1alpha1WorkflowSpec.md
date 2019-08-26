# IoArgoprojWorkflowV1alpha1WorkflowSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_deadline_seconds** | **int** | Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the workflow. A value of zero is used to terminate a Running workflow | [optional] 
**affinity** | [**IoK8sApiCoreV1Affinity**](IoK8sApiCoreV1Affinity.md) |  | [optional] 
**arguments** | [**IoArgoprojWorkflowV1alpha1Arguments**](IoArgoprojWorkflowV1alpha1Arguments.md) |  | [optional] 
**dns_config** | [**IoK8sApiCoreV1PodDNSConfig**](IoK8sApiCoreV1PodDNSConfig.md) |  | [optional] 
**dns_policy** | **str** | Set DNS policy for the pod. Defaults to \&quot;ClusterFirst\&quot;. Valid values are &#x27;ClusterFirstWithHostNet&#x27;, &#x27;ClusterFirst&#x27;, &#x27;Default&#x27; or &#x27;None&#x27;. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to &#x27;ClusterFirstWithHostNet&#x27;. | [optional] 
**entrypoint** | **str** | Entrypoint is a template reference to the starting point of the workflow | 
**host_network** | **bool** | Host networking requested for this workflow pod. Default to false. | [optional] 
**image_pull_secrets** | [**list[IoK8sApiCoreV1LocalObjectReference]**](IoK8sApiCoreV1LocalObjectReference.md) | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template. | [optional] 
**on_exit** | **str** | OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary workflow. | [optional] 
**parallelism** | **int** | Parallelism limits the max total parallel pods that can execute at the same time in a workflow | [optional] 
**pod_priority** | **int** | Priority to apply to workflow pods. | [optional] 
**pod_priority_class_name** | **str** | PriorityClassName to apply to workflow pods. | [optional] 
**priority** | **int** | Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first. | [optional] 
**scheduler_name** | **str** | Set scheduler name for all pods. Will be overridden if container/script template&#x27;s scheduler name is set. Default scheduler will be used if neither specified. | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as. | [optional] 
**suspend** | **bool** | Suspend will suspend the workflow and prevent execution of any future steps in the workflow | [optional] 
**templates** | [**list[IoArgoprojWorkflowV1alpha1Template]**](IoArgoprojWorkflowV1alpha1Template.md) | Templates is a list of workflow templates used in a workflow | 
**tolerations** | [**list[IoK8sApiCoreV1Toleration]**](IoK8sApiCoreV1Toleration.md) | Tolerations to apply to workflow pods. | [optional] 
**ttl_seconds_after_finished** | **int** | TTLSecondsAfterFinished limits the lifetime of a Workflow that has finished execution (Succeeded, Failed, Error). If this field is set, once the Workflow finishes, it will be deleted after ttlSecondsAfterFinished expires. If this field is unset, ttlSecondsAfterFinished will not expire. If this field is set to zero, ttlSecondsAfterFinished expires immediately after the Workflow finishes. | [optional] 
**volume_claim_templates** | [**list[IoK8sApiCoreV1PersistentVolumeClaim]**](IoK8sApiCoreV1PersistentVolumeClaim.md) | VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow | [optional] 
**volumes** | [**list[IoK8sApiCoreV1Volume]**](IoK8sApiCoreV1Volume.md) | Volumes is a list of volumes that can be mounted by containers in a workflow. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

