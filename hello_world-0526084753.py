from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-0526084753",
}

dag = DAG(
    "hello_world-0526084753",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_9426d557_d9d9_4c1a_98ef_e427c05a6ecf = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0526084753",
    cos_dependencies_archive="hello-9426d557-d9d9-4c1a-98ef-e427c05a6ecf.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="https://quay.io/repository/ml-on-k8s/kanikocontainer-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)


notebook_op_e4f52b87_650e_42cd_ba68_5adb082772a5 = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0526084753",
    cos_dependencies_archive="world-e4f52b87-650e-42cd-ba68-5adb082772a5.tar.gz",
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
    notebook_op_e4f52b87_650e_42cd_ba68_5adb082772a5
    << notebook_op_9426d557_d9d9_4c1a_98ef_e427c05a6ecf
)
