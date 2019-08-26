# IoArgoprojWorkflowV1alpha1DAGTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**IoArgoprojWorkflowV1alpha1Arguments**](IoArgoprojWorkflowV1alpha1Arguments.md) |  | [optional] 
**continue_on** | [**IoArgoprojWorkflowV1alpha1ContinueOn**](IoArgoprojWorkflowV1alpha1ContinueOn.md) |  | [optional] 
**dependencies** | **list[str]** | Dependencies are name of other targets which this depends on | [optional] 
**name** | **str** | Name is the name of the target | 
**template** | **str** | Name of template to execute | 
**when** | **str** | When is an expression in which the task should conditionally execute | [optional] 
**with_items** | [**list[IoArgoprojWorkflowV1alpha1Item]**](IoArgoprojWorkflowV1alpha1Item.md) | WithItems expands a task into multiple parallel tasks from the items in the list | [optional] 
**with_param** | **str** | WithParam expands a task into multiple parallel tasks from the value in the parameter, which is expected to be a JSON list. | [optional] 
**with_sequence** | [**IoArgoprojWorkflowV1alpha1Sequence**](IoArgoprojWorkflowV1alpha1Sequence.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

