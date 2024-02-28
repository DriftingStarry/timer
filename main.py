from datetime import datetime
nowdate = datetime.now()
targetdate = datetime(2024,7,29)
r = targetdate - nowdate
print(r)