import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

# Signal for synchronous execution
@receiver(post_save, sender=User)
def sync_signal(sender, instance, **kwargs):
    print("Signal received, processing...")
    time.sleep(2)  # Simulate delay
    print("Signal processing done.")

# Signal to check threading
@receiver(post_save, sender=User)
def check_thread(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Signal to check transaction status
@receiver(post_save, sender=User)
def check_transaction(sender, instance, **kwargs):
    print(f"Inside Signal: Transaction status - {transaction.get_connection().in_atomic_block}")
