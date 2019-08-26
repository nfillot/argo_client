# IoK8sApiAutoscalingV2beta1MetricSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external** | [**IoK8sApiAutoscalingV2beta1ExternalMetricSource**](IoK8sApiAutoscalingV2beta1ExternalMetricSource.md) |  | [optional] 
**object** | [**IoK8sApiAutoscalingV2beta1ObjectMetricSource**](IoK8sApiAutoscalingV2beta1ObjectMetricSource.md) |  | [optional] 
**pods** | [**IoK8sApiAutoscalingV2beta1PodsMetricSource**](IoK8sApiAutoscalingV2beta1PodsMetricSource.md) |  | [optional] 
**resource** | [**IoK8sApiAutoscalingV2beta1ResourceMetricSource**](IoK8sApiAutoscalingV2beta1ResourceMetricSource.md) |  | [optional] 
**type** | **str** | type is the type of metric source.  It should be one of \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each mapping to a matching field in the object. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

