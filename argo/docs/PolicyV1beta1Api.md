# argo.PolicyV1beta1Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_v1beta1_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#create_policy_v1beta1_namespaced_pod_disruption_budget) | **POST** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets | 
[**create_policy_v1beta1_pod_security_policy**](PolicyV1beta1Api.md#create_policy_v1beta1_pod_security_policy) | **POST** /apis/policy/v1beta1/podsecuritypolicies | 
[**delete_policy_v1beta1_collection_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#delete_policy_v1beta1_collection_namespaced_pod_disruption_budget) | **DELETE** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets | 
[**delete_policy_v1beta1_collection_pod_security_policy**](PolicyV1beta1Api.md#delete_policy_v1beta1_collection_pod_security_policy) | **DELETE** /apis/policy/v1beta1/podsecuritypolicies | 
[**delete_policy_v1beta1_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#delete_policy_v1beta1_namespaced_pod_disruption_budget) | **DELETE** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**delete_policy_v1beta1_pod_security_policy**](PolicyV1beta1Api.md#delete_policy_v1beta1_pod_security_policy) | **DELETE** /apis/policy/v1beta1/podsecuritypolicies/{name} | 
[**get_policy_v1beta1_api_resources**](PolicyV1beta1Api.md#get_policy_v1beta1_api_resources) | **GET** /apis/policy/v1beta1/ | 
[**list_policy_v1beta1_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#list_policy_v1beta1_namespaced_pod_disruption_budget) | **GET** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets | 
[**list_policy_v1beta1_pod_disruption_budget_for_all_namespaces**](PolicyV1beta1Api.md#list_policy_v1beta1_pod_disruption_budget_for_all_namespaces) | **GET** /apis/policy/v1beta1/poddisruptionbudgets | 
[**list_policy_v1beta1_pod_security_policy**](PolicyV1beta1Api.md#list_policy_v1beta1_pod_security_policy) | **GET** /apis/policy/v1beta1/podsecuritypolicies | 
[**patch_policy_v1beta1_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#patch_policy_v1beta1_namespaced_pod_disruption_budget) | **PATCH** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**patch_policy_v1beta1_namespaced_pod_disruption_budget_status**](PolicyV1beta1Api.md#patch_policy_v1beta1_namespaced_pod_disruption_budget_status) | **PATCH** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets/{name}/status | 
[**patch_policy_v1beta1_pod_security_policy**](PolicyV1beta1Api.md#patch_policy_v1beta1_pod_security_policy) | **PATCH** /apis/policy/v1beta1/podsecuritypolicies/{name} | 
[**read_policy_v1beta1_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#read_policy_v1beta1_namespaced_pod_disruption_budget) | **GET** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**read_policy_v1beta1_namespaced_pod_disruption_budget_status**](PolicyV1beta1Api.md#read_policy_v1beta1_namespaced_pod_disruption_budget_status) | **GET** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets/{name}/status | 
[**read_policy_v1beta1_pod_security_policy**](PolicyV1beta1Api.md#read_policy_v1beta1_pod_security_policy) | **GET** /apis/policy/v1beta1/podsecuritypolicies/{name} | 
[**replace_policy_v1beta1_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#replace_policy_v1beta1_namespaced_pod_disruption_budget) | **PUT** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**replace_policy_v1beta1_namespaced_pod_disruption_budget_status**](PolicyV1beta1Api.md#replace_policy_v1beta1_namespaced_pod_disruption_budget_status) | **PUT** /apis/policy/v1beta1/namespaces/{namespace}/poddisruptionbudgets/{name}/status | 
[**replace_policy_v1beta1_pod_security_policy**](PolicyV1beta1Api.md#replace_policy_v1beta1_pod_security_policy) | **PUT** /apis/policy/v1beta1/podsecuritypolicies/{name} | 
[**watch_policy_v1beta1_namespaced_pod_disruption_budget**](PolicyV1beta1Api.md#watch_policy_v1beta1_namespaced_pod_disruption_budget) | **GET** /apis/policy/v1beta1/watch/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**watch_policy_v1beta1_namespaced_pod_disruption_budget_list**](PolicyV1beta1Api.md#watch_policy_v1beta1_namespaced_pod_disruption_budget_list) | **GET** /apis/policy/v1beta1/watch/namespaces/{namespace}/poddisruptionbudgets | 
[**watch_policy_v1beta1_pod_disruption_budget_list_for_all_namespaces**](PolicyV1beta1Api.md#watch_policy_v1beta1_pod_disruption_budget_list_for_all_namespaces) | **GET** /apis/policy/v1beta1/watch/poddisruptionbudgets | 
[**watch_policy_v1beta1_pod_security_policy**](PolicyV1beta1Api.md#watch_policy_v1beta1_pod_security_policy) | **GET** /apis/policy/v1beta1/watch/podsecuritypolicies/{name} | 
[**watch_policy_v1beta1_pod_security_policy_list**](PolicyV1beta1Api.md#watch_policy_v1beta1_pod_security_policy_list) | **GET** /apis/policy/v1beta1/watch/podsecuritypolicies | 

# **create_policy_v1beta1_namespaced_pod_disruption_budget**
> IoK8sApiPolicyV1beta1PodDisruptionBudget create_policy_v1beta1_namespaced_pod_disruption_budget(body, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager)



create a PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiPolicyV1beta1PodDisruptionBudget() # IoK8sApiPolicyV1beta1PodDisruptionBudget | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

try:
    api_response = api_instance.create_policy_v1beta1_namespaced_pod_disruption_budget(body, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->create_policy_v1beta1_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_v1beta1_pod_security_policy**
> IoK8sApiPolicyV1beta1PodSecurityPolicy create_policy_v1beta1_pod_security_policy(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)



create a PodSecurityPolicy

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiPolicyV1beta1PodSecurityPolicy() # IoK8sApiPolicyV1beta1PodSecurityPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

try:
    api_response = api_instance.create_policy_v1beta1_pod_security_policy(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->create_policy_v1beta1_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiPolicyV1beta1PodSecurityPolicy**](IoK8sApiPolicyV1beta1PodSecurityPolicy.md)|  | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodSecurityPolicy**](IoK8sApiPolicyV1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_v1beta1_collection_namespaced_pod_disruption_budget**
> IoK8sApimachineryPkgApisMetaV1Status delete_policy_v1beta1_collection_namespaced_pod_disruption_budget(namespace, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.delete_policy_v1beta1_collection_namespaced_pod_disruption_budget(namespace, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->delete_policy_v1beta1_collection_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1Status**](IoK8sApimachineryPkgApisMetaV1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_v1beta1_collection_pod_security_policy**
> IoK8sApimachineryPkgApisMetaV1Status delete_policy_v1beta1_collection_pod_security_policy(pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of PodSecurityPolicy

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.delete_policy_v1beta1_collection_pod_security_policy(pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->delete_policy_v1beta1_collection_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1Status**](IoK8sApimachineryPkgApisMetaV1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_v1beta1_namespaced_pod_disruption_budget**
> IoK8sApimachineryPkgApisMetaV1Status delete_policy_v1beta1_namespaced_pod_disruption_budget(name, namespace, body=body, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = argo.IoK8sApimachineryPkgApisMetaV1DeleteOptions() # IoK8sApimachineryPkgApisMetaV1DeleteOptions |  (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try:
    api_response = api_instance.delete_policy_v1beta1_namespaced_pod_disruption_budget(name, namespace, body=body, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->delete_policy_v1beta1_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**IoK8sApimachineryPkgApisMetaV1DeleteOptions**](IoK8sApimachineryPkgApisMetaV1DeleteOptions.md)|  | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#x27;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#x27;Orphan&#x27; - orphan the dependents; &#x27;Background&#x27; - allow the garbage collector to delete the dependents in the background; &#x27;Foreground&#x27; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1Status**](IoK8sApimachineryPkgApisMetaV1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_v1beta1_pod_security_policy**
> IoK8sApimachineryPkgApisMetaV1Status delete_policy_v1beta1_pod_security_policy(name, body=body, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a PodSecurityPolicy

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
name = 'name_example' # str | name of the PodSecurityPolicy
body = argo.IoK8sApimachineryPkgApisMetaV1DeleteOptions() # IoK8sApimachineryPkgApisMetaV1DeleteOptions |  (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try:
    api_response = api_instance.delete_policy_v1beta1_pod_security_policy(name, body=body, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->delete_policy_v1beta1_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodSecurityPolicy | 
 **body** | [**IoK8sApimachineryPkgApisMetaV1DeleteOptions**](IoK8sApimachineryPkgApisMetaV1DeleteOptions.md)|  | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#x27;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#x27;Orphan&#x27; - orphan the dependents; &#x27;Background&#x27; - allow the garbage collector to delete the dependents in the background; &#x27;Foreground&#x27; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1Status**](IoK8sApimachineryPkgApisMetaV1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_v1beta1_api_resources**
> IoK8sApimachineryPkgApisMetaV1APIResourceList get_policy_v1beta1_api_resources()



get available resources

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))

try:
    api_response = api_instance.get_policy_v1beta1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->get_policy_v1beta1_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IoK8sApimachineryPkgApisMetaV1APIResourceList**](IoK8sApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policy_v1beta1_namespaced_pod_disruption_budget**
> IoK8sApiPolicyV1beta1PodDisruptionBudgetList list_policy_v1beta1_namespaced_pod_disruption_budget(namespace, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.list_policy_v1beta1_namespaced_pod_disruption_budget(namespace, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->list_policy_v1beta1_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudgetList**](IoK8sApiPolicyV1beta1PodDisruptionBudgetList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policy_v1beta1_pod_disruption_budget_for_all_namespaces**
> IoK8sApiPolicyV1beta1PodDisruptionBudgetList list_policy_v1beta1_pod_disruption_budget_for_all_namespaces(_continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.list_policy_v1beta1_pod_disruption_budget_for_all_namespaces(_continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->list_policy_v1beta1_pod_disruption_budget_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudgetList**](IoK8sApiPolicyV1beta1PodDisruptionBudgetList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policy_v1beta1_pod_security_policy**
> IoK8sApiPolicyV1beta1PodSecurityPolicyList list_policy_v1beta1_pod_security_policy(pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind PodSecurityPolicy

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.list_policy_v1beta1_pod_security_policy(pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->list_policy_v1beta1_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodSecurityPolicyList**](IoK8sApiPolicyV1beta1PodSecurityPolicyList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_policy_v1beta1_namespaced_pod_disruption_budget**
> IoK8sApiPolicyV1beta1PodDisruptionBudget patch_policy_v1beta1_namespaced_pod_disruption_budget(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)



partially update the specified PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = NULL # object | 
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
force = true # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

try:
    api_response = api_instance.patch_policy_v1beta1_namespaced_pod_disruption_budget(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->patch_policy_v1beta1_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional] 
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_policy_v1beta1_namespaced_pod_disruption_budget_status**
> IoK8sApiPolicyV1beta1PodDisruptionBudget patch_policy_v1beta1_namespaced_pod_disruption_budget_status(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)



partially update status of the specified PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = NULL # object | 
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
force = true # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

try:
    api_response = api_instance.patch_policy_v1beta1_namespaced_pod_disruption_budget_status(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->patch_policy_v1beta1_namespaced_pod_disruption_budget_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional] 
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_policy_v1beta1_pod_security_policy**
> IoK8sApiPolicyV1beta1PodSecurityPolicy patch_policy_v1beta1_pod_security_policy(body, name, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)



partially update the specified PodSecurityPolicy

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = NULL # object | 
name = 'name_example' # str | name of the PodSecurityPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
force = true # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

try:
    api_response = api_instance.patch_policy_v1beta1_pod_security_policy(body, name, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->patch_policy_v1beta1_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **name** | **str**| name of the PodSecurityPolicy | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional] 
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodSecurityPolicy**](IoK8sApiPolicyV1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_policy_v1beta1_namespaced_pod_disruption_budget**
> IoK8sApiPolicyV1beta1PodDisruptionBudget read_policy_v1beta1_namespaced_pod_disruption_budget(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

try:
    api_response = api_instance.read_policy_v1beta1_namespaced_pod_disruption_budget(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->read_policy_v1beta1_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#x27;Namespace&#x27;. Deprecated. Planned for removal in 1.18. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_policy_v1beta1_namespaced_pod_disruption_budget_status**
> IoK8sApiPolicyV1beta1PodDisruptionBudget read_policy_v1beta1_namespaced_pod_disruption_budget_status(name, namespace, pretty=pretty)



read status of the specified PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.read_policy_v1beta1_namespaced_pod_disruption_budget_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->read_policy_v1beta1_namespaced_pod_disruption_budget_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_policy_v1beta1_pod_security_policy**
> IoK8sApiPolicyV1beta1PodSecurityPolicy read_policy_v1beta1_pod_security_policy(name, pretty=pretty, exact=exact, export=export)



read the specified PodSecurityPolicy

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
name = 'name_example' # str | name of the PodSecurityPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

try:
    api_response = api_instance.read_policy_v1beta1_pod_security_policy(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->read_policy_v1beta1_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodSecurityPolicy | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#x27;Namespace&#x27;. Deprecated. Planned for removal in 1.18. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodSecurityPolicy**](IoK8sApiPolicyV1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_policy_v1beta1_namespaced_pod_disruption_budget**
> IoK8sApiPolicyV1beta1PodDisruptionBudget replace_policy_v1beta1_namespaced_pod_disruption_budget(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager)



replace the specified PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiPolicyV1beta1PodDisruptionBudget() # IoK8sApiPolicyV1beta1PodDisruptionBudget | 
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

try:
    api_response = api_instance.replace_policy_v1beta1_namespaced_pod_disruption_budget(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->replace_policy_v1beta1_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)|  | 
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_policy_v1beta1_namespaced_pod_disruption_budget_status**
> IoK8sApiPolicyV1beta1PodDisruptionBudget replace_policy_v1beta1_namespaced_pod_disruption_budget_status(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager)



replace status of the specified PodDisruptionBudget

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiPolicyV1beta1PodDisruptionBudget() # IoK8sApiPolicyV1beta1PodDisruptionBudget | 
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

try:
    api_response = api_instance.replace_policy_v1beta1_namespaced_pod_disruption_budget_status(body, name, namespace, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->replace_policy_v1beta1_namespaced_pod_disruption_budget_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)|  | 
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodDisruptionBudget**](IoK8sApiPolicyV1beta1PodDisruptionBudget.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_policy_v1beta1_pod_security_policy**
> IoK8sApiPolicyV1beta1PodSecurityPolicy replace_policy_v1beta1_pod_security_policy(body, name, pretty=pretty, dry_run=dry_run, field_manager=field_manager)



replace the specified PodSecurityPolicy

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiPolicyV1beta1PodSecurityPolicy() # IoK8sApiPolicyV1beta1PodSecurityPolicy | 
name = 'name_example' # str | name of the PodSecurityPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

try:
    api_response = api_instance.replace_policy_v1beta1_pod_security_policy(body, name, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->replace_policy_v1beta1_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiPolicyV1beta1PodSecurityPolicy**](IoK8sApiPolicyV1beta1PodSecurityPolicy.md)|  | 
 **name** | **str**| name of the PodSecurityPolicy | 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 

### Return type

[**IoK8sApiPolicyV1beta1PodSecurityPolicy**](IoK8sApiPolicyV1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_policy_v1beta1_namespaced_pod_disruption_budget**
> IoK8sApimachineryPkgApisMetaV1WatchEvent watch_policy_v1beta1_namespaced_pod_disruption_budget(name, namespace, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.watch_policy_v1beta1_namespaced_pod_disruption_budget(name, namespace, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->watch_policy_v1beta1_namespaced_pod_disruption_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1WatchEvent**](IoK8sApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_policy_v1beta1_namespaced_pod_disruption_budget_list**
> IoK8sApimachineryPkgApisMetaV1WatchEvent watch_policy_v1beta1_namespaced_pod_disruption_budget_list(namespace, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.watch_policy_v1beta1_namespaced_pod_disruption_budget_list(namespace, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->watch_policy_v1beta1_namespaced_pod_disruption_budget_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1WatchEvent**](IoK8sApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_policy_v1beta1_pod_disruption_budget_list_for_all_namespaces**
> IoK8sApimachineryPkgApisMetaV1WatchEvent watch_policy_v1beta1_pod_disruption_budget_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.watch_policy_v1beta1_pod_disruption_budget_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->watch_policy_v1beta1_pod_disruption_budget_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1WatchEvent**](IoK8sApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_policy_v1beta1_pod_security_policy**
> IoK8sApimachineryPkgApisMetaV1WatchEvent watch_policy_v1beta1_pod_security_policy(name, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind PodSecurityPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
name = 'name_example' # str | name of the PodSecurityPolicy
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.watch_policy_v1beta1_pod_security_policy(name, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->watch_policy_v1beta1_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodSecurityPolicy | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1WatchEvent**](IoK8sApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_policy_v1beta1_pod_security_policy_list**
> IoK8sApimachineryPkgApisMetaV1WatchEvent watch_policy_v1beta1_pod_security_policy_list(_continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of PodSecurityPolicy. deprecated: use the 'watch' parameter with a list operation instead.

### Example
```python
from __future__ import print_function
import time
import argo
from argo.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = argo.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = argo.PolicyV1beta1Api(argo.ApiClient(configuration))
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try:
    api_response = api_instance.watch_policy_v1beta1_pod_security_policy_list(_continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyV1beta1Api->watch_policy_v1beta1_pod_security_policy_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#x27;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**IoK8sApimachineryPkgApisMetaV1WatchEvent**](IoK8sApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

