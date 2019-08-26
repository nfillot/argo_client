# IoK8sApiAuthorizationV1SubjectRulesReviewStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_error** | **str** | EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn&#x27;t support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. | [optional] 
**incomplete** | **bool** | Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn&#x27;t support rules evaluation. | 
**non_resource_rules** | [**list[IoK8sApiAuthorizationV1NonResourceRule]**](IoK8sApiAuthorizationV1NonResourceRule.md) | NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn&#x27;t significant, may contain duplicates, and possibly be incomplete. | 
**resource_rules** | [**list[IoK8sApiAuthorizationV1ResourceRule]**](IoK8sApiAuthorizationV1ResourceRule.md) | ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn&#x27;t significant, may contain duplicates, and possibly be incomplete. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

