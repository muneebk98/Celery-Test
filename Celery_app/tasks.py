import subprocess
import os
from celery import shared_task

@shared_task
def update_code_task():
    try:
        project_path = "/PycharmProjects/Celery_Practice/Celery_Project"
        os.chdir(project_path)
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)

        if result.returncode == 0:
            print("Code updated successfully!")
            print(result.stdout)
        else:
            print("Git pull failed.")
            print(result.stderr)

    except Exception as e:
        print(f"Deployment failed: {e}")
