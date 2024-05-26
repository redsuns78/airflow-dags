from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-0526105751",
}

dag = DAG(
    "model_deploy-0526105751",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_32f76504_a4f4_4a66_ac83_92a0859643ab = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0526105751",
    cos_dependencies_archive="build_push_image-32f76504-a4f4-4a66-ac83-92a0859643ab.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY": "https://lemonyregistry.duckdns.org",
        "CONTAINER_REGISTRY_USER": "root",
        "CONTAINER_REGISTRY_PASSWORD": "!Aa82507602@",
        "CONTAINER_DETAILS": "lemonyregistry.duckdns.org/root/iac_devops/mlflowdemo",
    },
    config_file="None",
    dag=dag,
)

notebook_op_32f76504_a4f4_4a66_ac83_92a0859643ab.image_pull_policy = "IfNotPresent"


notebook_op_1fcdbaa0_939b_40d8_981e_46743086d499 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0526105751",
    cos_dependencies_archive="deploy_model-1fcdbaa0-939b-40d8-981e-46743086d499.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_DETAILS": "lemonyregistry.duckdns.org/root/iac_devops/mlflowdemo",
        "CLUSTER_DOMAIN_NAME": "192.168.0.135.nip.io",
    },
    config_file="None",
    dag=dag,
)

notebook_op_1fcdbaa0_939b_40d8_981e_46743086d499.image_pull_policy = "IfNotPresent"

(
    notebook_op_1fcdbaa0_939b_40d8_981e_46743086d499
    << notebook_op_32f76504_a4f4_4a66_ac83_92a0859643ab
)
