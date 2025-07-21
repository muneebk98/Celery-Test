import subprocess
import os
from celery import shared_task

@shared_task
def update_code_task():
    try:
        # Fix: Use the correct project path
        project_path = "/home/muneeb-khalid/PycharmProjects/Celery_Practice"
        os.chdir(project_path)
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)

        if result.returncode == 0:
            print("Code updated successfully!")
            print(result.stdout)
            return "Code updated successfully!"
        else:
            print("Git pull failed.")
            print(result.stderr)
            return f"Git pull failed: {result.stderr}"

    except Exception as e:
        print(f"Deployment failed: {e}")
        return f"Deployment failed: {e}"
