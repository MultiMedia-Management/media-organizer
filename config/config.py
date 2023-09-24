import os

db_in_memory = []
list_files_info = []

# DB check before dump the data into the files
max_retries_before_dump_the_data = 3
count_valid_insert_operation = 0

# Home directory conf
home_dir = os.path.expanduser("~")

# Some files that will be used in the application, with 
# the respective paths
CONF_FILE = home_dir + "/.mo_setting.json"
JSON_DB = home_dir + "/.mo_hash.json"
BASE_REPORT_DIR = home_dir + "/mo_reports"