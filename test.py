from datetime import datetime, timedelta

now = datetime.now()
nowdelta = datetime.now() - timedelta(seconds=5)

print(now.time().second)
print(nowdelta.time().second)