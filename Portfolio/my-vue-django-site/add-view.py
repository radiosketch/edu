import sys
import os

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = os.path.join(BASE_DIR, 'djangovue')
print(PROJECT_DIR)

def main():
	try:
		# Initialize required arguments
		view_name_index = sys.argv.index('-n') + 1
		view_url_index = sys.argv.index('-u') + 1
		view_name = sys.argv[view_name_index]
		view_url = sys.argv[view_url_index]
	except Exception as e:
		print('Missing required argument, use -h to see required parameters')
		quit()

	print(view_name, view_url)

try:
	if sys.argv.index('-h') is not None:
		print('''
			add-view.py is a dev tool for adding views to the current django project
			Required Arguments:
				-n <name>
				-u <url>
			Optional Arguments:
				-h : Display this message
			Example Usage:
				python add-view.py -n "name" -u "url"
			''')
finally:
	main()
