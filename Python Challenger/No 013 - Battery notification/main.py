import psutil
from pynotifier import Notification
from win10toast import ToastNotifier

battery = psutil.sensors_battery()
toaster = ToastNotifier()
percent = 15

if percent <= 30:
    Notification(
        title="Nível de bateria está baixo.",
        description=f"{str(percent)}",
        duration=5
    ).send()
    toaster.show_toast(
        "Notificação",
        "Corpo da notificação",
        icon_path=None,
        duration=20,
        threaded=True
    )
    