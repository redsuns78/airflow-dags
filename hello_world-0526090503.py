from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-0526090503",
}

dag = DAG(
    "hello_world-0526090503",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_a6b61b50_0e26_4e23_a2cf_f6b59ddd4881 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0526090503",
    cos_dependencies_archive="hello-a6b61b50-0e26-4e23-a2cf-f6b59ddd4881.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_a6b61b50_0e26_4e23_a2cf_f6b59ddd4881.image_pull_policy = "IfNotPresent"


notebook_op_2a17c78f_7106_418c_8bb8_cfc05d5531ff = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0526090503",
    cos_dependencies_archive="world-2a17c78f-7106-418c-8bb8-cfc05d5531ff.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="https://quay.io/repository/ml-on-k8s/airflowpython-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_2a17c78f_7106_418c_8bb8_cfc05d5531ff
    << notebook_op_a6b61b50_0e26_4e23_a2cf_f6b59ddd4881
)
