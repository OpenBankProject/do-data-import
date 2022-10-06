from datetime import datetime
from obp_python.config import obp_api_host, logger

def get_string_from_string_or_date(_input, date_format):
	if type(_input) is datetime:
		return _input.strftime(date_format)
	else:
		return str(_input)
