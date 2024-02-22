def return_final_file_name(file_type, datetime_original, SOURCE_FILE_PATH):
    """
        type: "video||picture"
        datetime_original: date in the format "2020:10:31 15:13:00"
        SOURCE_FILE_PATH: Full path to the source file, for example "/misc/dir1/pic1.jpg"
    """

    # Extracting the extension and also the file name with no extension
    file_extension = SOURCE_FILE_PATH.split(".")[-1]
    file_name_with_no_ext = SOURCE_FILE_PATH.split("/")[-1].replace("." + file_extension,"")

    if file_type == "video":
        final_file_name = datetime_original.replace(":", "-").replace(" ", "_") + "__" + file_name_with_no_ext + "." + file_extension
        return final_file_name

    if file_type == "picture":
        final_file_name = datetime_original.replace(":", "-").replace(" ", "_") + "." + file_extension
        return final_file_name

    if (file_type == "video_no_exif") or (file_type == "picture_no_exif"):
        final_file_name = SOURCE_FILE_PATH.split("/")[-1]
        return final_file_name