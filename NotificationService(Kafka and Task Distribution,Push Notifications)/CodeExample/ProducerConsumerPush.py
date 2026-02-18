import threading
import queue
import time
import random

# Shared queue for notifications (produced regardless of user status)
notification_queue = queue.Queue()

# Simulate online/offline status of users
user_online_status = {
    "user1": True,
    "user2": False,
    "user3": True
}

# Producer: generates notifications
def producer():
    notification_id = 1
    while notification_id <= 10:
        user_id = random.choice(list(user_online_status.keys()))
        notification = f"Notification {notification_id} for {user_id}"
        print(f"[Producer] Generated: {notification}")
        notification_queue.put((user_id, notification))
        notification_id += 1
        time.sleep(0.5)  # simulate time between notifications

# Middleman / Dispatcher: checks if user is online before pushing
def push_dispatcher():
    while True:
        if notification_queue.empty():
            time.sleep(0.1)
            continue

        user_id, notification = notification_queue.get()

        if user_online_status.get(user_id):
            # User online → push notification
            push_to_user(user_id, notification)
        else:
            # User offline → re-queue for later delivery
            print(f"[Dispatcher] {user_id} offline, will retry: {notification}")
            notification_queue.put((user_id, notification))
            # Optional delay before next check
            time.sleep(1)

        notification_queue.task_done()

# Simulated push function
def push_to_user(user_id, notification):
    print(f"[Push] Delivered to {user_id}: {notification}")

# Start threads
producer_thread = threading.Thread(target=producer)
dispatcher_thread = threading.Thread(target=push_dispatcher, daemon=True)

producer_thread.start()
dispatcher_thread.start()

producer_thread.join()
notification_queue.join()
print("All notifications processed.")
