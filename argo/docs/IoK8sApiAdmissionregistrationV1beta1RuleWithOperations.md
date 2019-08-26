# IoK8sApiAdmissionregistrationV1beta1RuleWithOperations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_groups** | **list[str]** | APIGroups is the API groups the resources belong to. &#x27;*&#x27; is all groups. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | [optional] 
**api_versions** | **list[str]** | APIVersions is the API versions the resources belong to. &#x27;*&#x27; is all versions. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | [optional] 
**operations** | **list[str]** | Operations is the operations the admission hook cares about - CREATE, UPDATE, or * for all operations. If &#x27;*&#x27; is present, the length of the slice must be one. Required. | [optional] 
**resources** | **list[str]** | Resources is a list of resources this rule applies to.  For example: &#x27;pods&#x27; means pods. &#x27;pods/log&#x27; means the log subresource of pods. &#x27;*&#x27; means all resources, but not subresources. &#x27;pods/*&#x27; means all subresources of pods. &#x27;*/scale&#x27; means all scale subresources. &#x27;*/*&#x27; means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required. | [optional] 
**scope** | **str** | scope specifies the scope of this rule. Valid values are \&quot;Cluster\&quot;, \&quot;Namespaced\&quot;, and \&quot;*\&quot; \&quot;Cluster\&quot; means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. \&quot;Namespaced\&quot; means that only namespaced resources will match this rule. \&quot;*\&quot; means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is \&quot;*\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

