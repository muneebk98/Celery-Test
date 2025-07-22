from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Celery_app.tasks import update_code_task
import json

@csrf_exempt
def github_webhook(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            update_code_task.delay()
            return JsonResponse({"status": "success", "message": "Deployment triggered."}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"message": "Only POST requests allowed"}, status=400)


