# argo.AuthenticationV1Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication_v1_token_review**](AuthenticationV1Api.md#create_authentication_v1_token_review) | **POST** /apis/authentication.k8s.io/v1/tokenreviews | 
[**get_authentication_v1_api_resources**](AuthenticationV1Api.md#get_authentication_v1_api_resources) | **GET** /apis/authentication.k8s.io/v1/ | 

# **create_authentication_v1_token_review**
> IoK8sApiAuthenticationV1TokenReview create_authentication_v1_token_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)



create a TokenReview

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
api_instance = argo.AuthenticationV1Api(argo.ApiClient(configuration))
body = argo.IoK8sApiAuthenticationV1TokenReview() # IoK8sApiAuthenticationV1TokenReview | 
dry_run = 'dry_run_example' # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
field_manager = 'field_manager_example' # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_authentication_v1_token_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationV1Api->create_authentication_v1_token_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IoK8sApiAuthenticationV1TokenReview**](IoK8sApiAuthenticationV1TokenReview.md)|  | 
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional] 
 **pretty** | **str**| If &#x27;true&#x27;, then the output is pretty printed. | [optional] 

### Return type

[**IoK8sApiAuthenticationV1TokenReview**](IoK8sApiAuthenticationV1TokenReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_v1_api_resources**
> IoK8sApimachineryPkgApisMetaV1APIResourceList get_authentication_v1_api_resources()



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
api_instance = argo.AuthenticationV1Api(argo.ApiClient(configuration))

try:
    api_response = api_instance.get_authentication_v1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationV1Api->get_authentication_v1_api_resources: %s\n" % e)
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

