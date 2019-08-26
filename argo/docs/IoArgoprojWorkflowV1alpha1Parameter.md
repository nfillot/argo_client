# IoArgoprojWorkflowV1alpha1Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default is the default value to use for an input parameter if a value was not supplied | [optional] 
**global_name** | **str** | GlobalName exports an output parameter to the global scope, making it available as &#x27;{{workflow.outputs.parameters.XXXX}} and in workflow.status.outputs.parameters | [optional] 
**name** | **str** | Name is the parameter name | 
**value** | **str** | Value is the literal value to use for the parameter. If specified in the context of an input parameter, the value takes precedence over any passed values | [optional] 
**value_from** | [**IoArgoprojWorkflowV1alpha1ValueFrom**](IoArgoprojWorkflowV1alpha1ValueFrom.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

