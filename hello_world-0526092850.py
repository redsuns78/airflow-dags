from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-0526092850",
}

dag = DAG(
    "hello_world-0526092850",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_13b9b37c_9f27_4ebc_95e0_1a1e004e3065 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0526092850",
    cos_dependencies_archive="hello-13b9b37c-9f27-4ebc-95e0-1a1e004e3065.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    resources={
        "request_cpu": "1",
        "request_memory": "1",
    },
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_13b9b37c_9f27_4ebc_95e0_1a1e004e3065.image_pull_policy = "IfNotPresent"


notebook_op_a0e9607d_099a_4d98_a24b_8e8b938fc051 = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0526092850",
    cos_dependencies_archive="world-a0e9607d-099a-4d98-a24b-8e8b938fc051.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    resources={
        "request_cpu": "1",
        "request_memory": "1",
    },
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_a0e9607d_099a_4d98_a24b_8e8b938fc051.image_pull_policy = "IfNotPresent"

(
    notebook_op_a0e9607d_099a_4d98_a24b_8e8b938fc051
    << notebook_op_13b9b37c_9f27_4ebc_95e0_1a1e004e3065
)
