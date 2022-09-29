from obp_python.createBranch import createBranch
from obp_python.config import logger


def create_branch_from_row(row):
	try:
		createBranch(
			bank_id=row[0].value.strip(),
			branch_id=row[1].value,
			name=row[1].value,
			line_1=row[4].value,
			city=row[3].value,
			county=row[2].value
		)
	except Exception as e:
		logger.exception(f'Could not create Branch from line {row[0].row}. Reason: {e}')