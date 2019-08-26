# argo.AuthorizationV1beta1Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authorization_v1beta1_namespaced_local_subject_access_review**](AuthorizationV1beta1Api.md#create_authorization_v1beta1_namespaced_local_subject_access_review) | **POST** /apis/authorization.k8s.io/v1beta1/namespaces/{namespace}/localsubjectaccessreviews | 
[**create_authorization_v1beta1_self_subject_access_review**](AuthorizationV1beta1Api.md#create_authorization_v1beta1_self_subject_access_review) | **POST** /apis/authorization.k8s.io/v1beta1/selfsubjectaccessreviews | 
[**create_authorization_v1beta1_self_subject_rules_review**](AuthorizationV1beta1Api.md#create_authorization_v1beta1_self_subject_rules_review) | **POST** /apis/authorization.k8s.io/v1beta1/selfsubjectrulesreviews | 
[**create_authorization_v1beta1_subject_access_review**](AuthorizationV1beta1Api.md#create_authorization_v1beta1_subject_access_review) | **POST** /apis/authorization.k8s.io/v1beta1/subjectaccessreviews | 
[**get_authorization_v1beta1_api_resources**](AuthorizationV1beta1Api.md#get_authorization_v1beta1_api_resources) | **GET** /apis/authorization.k8s.io/v1beta1/ | 

# **create_authorization_v1beta1_namespaced_local_subject_access_review**
> IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview create_authorization_v1beta1_namespaced_local_subject_access_review(body, namespace, dry_run=dry_run, field_manager=field_manager, pretty=pretty)



create a LocalSubjectAccessReview

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
api_instance = argo.AuthorizationV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview() # IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_authorization_v1beta1_namespaced_local_subject_access_review(body, namespace, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1beta1Api->create_authorization_v1beta1_namespaced_local_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview**](IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 

### Return type

[**IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview**](IoK8sApiAuthorizationV1beta1LocalSubjectAccessReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_v1beta1_self_subject_access_review**
> IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview create_authorization_v1beta1_self_subject_access_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)



create a SelfSubjectAccessReview

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
api_instance = argo.AuthorizationV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview() # IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_authorization_v1beta1_self_subject_access_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1beta1Api->create_authorization_v1beta1_self_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview**](IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 

### Return type

[**IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview**](IoK8sApiAuthorizationV1beta1SelfSubjectAccessReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_v1beta1_self_subject_rules_review**
> IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview create_authorization_v1beta1_self_subject_rules_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)



create a SelfSubjectRulesReview

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
api_instance = argo.AuthorizationV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview() # IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_authorization_v1beta1_self_subject_rules_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1beta1Api->create_authorization_v1beta1_self_subject_rules_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview**](IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 

### Return type

[**IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview**](IoK8sApiAuthorizationV1beta1SelfSubjectRulesReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_v1beta1_subject_access_review**
> IoK8sApiAuthorizationV1beta1SubjectAccessReview create_authorization_v1beta1_subject_access_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)



create a SubjectAccessReview

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
api_instance = argo.AuthorizationV1beta1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiAuthorizationV1beta1SubjectAccessReview() # IoK8sApiAuthorizationV1beta1SubjectAccessReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_authorization_v1beta1_subject_access_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1beta1Api->create_authorization_v1beta1_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiAuthorizationV1beta1SubjectAccessReview**](IoK8sApiAuthorizationV1beta1SubjectAccessReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 

### Return type

[**IoK8sApiAuthorizationV1beta1SubjectAccessReview**](IoK8sApiAuthorizationV1beta1SubjectAccessReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_v1beta1_api_resources**
> IoK8sApimachineryPkgApisMetaV1APIResourceList get_authorization_v1beta1_api_resources()



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
api_instance = argo.AuthorizationV1beta1Api(argo.ApiClient(configuration))

try:
    api_response = api_instance.get_authorization_v1beta1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1beta1Api->get_authorization_v1beta1_api_resources: %s\n" % e)
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

