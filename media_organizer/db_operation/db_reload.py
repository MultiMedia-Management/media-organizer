from media_organizer.setup_env import setup_env
from media_organizer.report import report
import os
from media_organizer.general_format import general_format
from media_organizer.file_operation import file_operation
from media_organizer.config import config
from media_organizer.db_operation import db_operation

def reload_db_from_target_dir():
    """
    TODO
    """
    # print("here")

    question = input("Are you sure you would like to repopulate the DB? \n\
this can spend some time (y/n): ")
    if question == "y":

      state = "current_media"
      target_dir = setup_env.check_target_dir()

      SUPPORTED_EXT_PICTURE = ["jpg", "jpeg", "JPG", "JPEG"]
      SUPPORTED_EXT_VIDEO = ["mp4", "MP4", "mov", "MOV"]

      # Creating the header of the CSV file
      report.creating_the_header_of_CSV_file()

      for root, dirs, files in os.walk(target_dir):
          for file in files:
              # print(file)
              SOURCE_FILE_PATH = root + "/" + file
              FILE_EXT = SOURCE_FILE_PATH.split(".")[-1]
              if FILE_EXT in SUPPORTED_EXT_PICTURE:
                # import_picture(SOURCE_FILE_PATH)
                hash_source = file_operation.return_hash_from_file(SOURCE_FILE_PATH)
                general_format.formated_output(state, hash_source, "", SOURCE_FILE_PATH)
                config.db_in_memory.append({'filename': SOURCE_FILE_PATH, 'hash': hash_source})
                
                # Incrementing the counter
                config.count_valid_insert_operation = config.count_valid_insert_operation + 1

              elif FILE_EXT in SUPPORTED_EXT_VIDEO:
                # import_videos(SOURCE_FILE_PATH)
                hash_source = file_operation.return_hash_from_file(SOURCE_FILE_PATH)
                general_format.formated_output(state, hash_source, "", SOURCE_FILE_PATH)
                config.db_in_memory.append({'filename': SOURCE_FILE_PATH, 'hash': hash_source})

                # Incrementing the counter
                config.count_valid_insert_operation = config.count_valid_insert_operation + 1

              else:
                  # Printing that this format it's not supported
                  general_format.formated_output("not_supported", "", SOURCE_FILE_PATH, "")


              # Checking the # of operations before dump the data
              # from memory to file (JSON)
              if config.count_valid_insert_operation >= config.max_retries_before_dump_the_data:
                  db_operation.save_db_in_disk()
                  config.count_valid_insert_operation = 0

          # aux = (current_time, SOURCE_FILE_PATH, hash_source, DEST_FILE_PATH, state, "copied", "",)
          # aux = (state, SOURCE_FILE_PATH, hash_source, DEST_FILE_PATH, state, "copied", "",)
          # def formated_output(state, hash_source, SOURCE_FILE_PATH, DEST_FILE_PATH):
      # db_operation.save_db_in_disk_from_list()
      db_operation.save_db_in_disk()
      # Creating the CSV with all the operations
      report.dump_content_in_csv_file(config.BASE_REPORT_DIR + "/" + "reload.csv")

    else:
       print("Ok, exiting now ...")