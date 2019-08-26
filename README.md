# Argo Python Client

This Argo Python client includes missing objects (WorkflowStatus, NodeStatus).

## Example

The code snippet is based on the Go example (https://github.com/argoproj/argo/blob/master/docs/example-golang/main.go).

It assumes that you're inside the Kubernetes cluster and thus is using the incluster configuration.

```python
import kubernetes
from argo.models import *

kubernetes.config.load_incluster_config()
api_instance = kubernetes.client.CustomObjectsApi(
        kubernetes.client.ApiClient())

# List Argo Workflows
api_response = api_instance.list_namespaced_custom_object(
        "argoproj.io", version="v1alpha1",
        plural="workflows", namespace="default")

print(api_response)


# Create Workflow based on Go example.
object_meta = io_k8s_apimachinery_pkg_apis_meta_v1_object_meta.\
        IoK8sApimachineryPkgApisMetaV1ObjectMeta(generate_name="hello-whale-")
container_spec = io_k8s_api_core_v1_container.IoK8sApiCoreV1Container(
        image="docker/whalesay:latest", command=['cowsay'],
        args=["hello world"], name="whalesay")
workflow_spec = IoArgoprojWorkflowV1alpha1WorkflowSpec(
        entrypoint="whalesay",
        templates=[IoArgoprojWorkflowV1alpha1Template(
            name="whalesay",
            container=container_spec)])
workflow = IoArgoprojWorkflowV1alpha1Workflow(
        metadata=object_meta,
        kind="Workflow", api_version="argoproj.io/v1alpha1",
        spec=workflow_spec, status=IoArgoprojWorkflowV1alpha1WorkflowStatus())

api_response = api_instance.create_namespaced_custom_object(
        "argoproj.io", version="v1alpha1", plural="workflows",
        namespace="default", body=workflow)

print(api_response)
```
