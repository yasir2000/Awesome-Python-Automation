import schedule
from umbrellaReminder import umbrella_reminder

# Define schedule job
schedule.every().day.at("06:00").do(umbrella_reminder.send_umbrella_reminder)

# Main loop to run scheduled tasks
while True:
    schedule.run_pending()
