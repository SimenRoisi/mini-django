import time
from celery import shared_task
from .models import Note

@shared_task
def simulate_note_processing_task(note_id):
    """
    Simulates a long-running background task (e.g., sending an email or generating a PDF).
    """
    print(f"[CELERY WORKER] Received task for Note ID: {note_id}")
    time.sleep(1) # Simulate heavy lifting
    print(f"[CELERY WORKER] Successfully processed Note ID: {note_id}")
    return True
