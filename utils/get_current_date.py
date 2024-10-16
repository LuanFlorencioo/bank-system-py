from datetime import datetime

def get_current_date():
  current_date = datetime.now()
  formatted_date = current_date.strftime("%d/%m/%Y %H:%M:%S")

  return formatted_date