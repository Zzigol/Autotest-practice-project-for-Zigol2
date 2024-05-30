import os

class FilePathHelper:

    def get_path_simple_mark():
        return os.getcwd() + '\\test_files\\simple_mark.docx'


    def get_path_table_mark():
        return os.getcwd() + '\\test_files\\table_mark.docx'


    def get_path_check_import_false_date():
        return os.getcwd() + '\\test_files\\check_import_false_date.xlsx'


    def get_path_check_import_false_int():
        return os.getcwd() + '\\test_files\\check_import_false_int.xlsx'


    def get_path_check_import_false_checkbox():
        return os.getcwd() + '\\test_files\\check_import_false_checkbox.xlsx'


    def get_path_check_import_false_dictionary():
        return os.getcwd() + '\\test_files\\check_import_false_dictionary.xlsx'


    def get_path_check_import_false_str():
        return os.getcwd() + '\\test_files\\check_import_false_str.xlsx'


    def get_path_import_files_zip():
        return os.getcwd() + '\\test_files\\import_files.zip'


    def get_path_import_alphabets():
        return os.getcwd() + '\\test_files\\Import_alphabets.xlsx'


    def get_path_wrong_files_zip():
        return os.getcwd() + '\\test_files\\wrong_import_file.zip'
    
    
    def get_path_test_files(file):
        return os.getcwd() + f'\\test_files\\{file}'
    

    def get_path_old_cert():
        return os.getcwd() + '\\test_files\\AUTOTEST_1_OLD.cer'


    def get_path_import_invalid():
        return os.getcwd() + '\\test_files\\Import_invalid.xlsx'
    
    def get_path_file_test_one():
        return os.getcwd() + '\\test_files\\File_test1.txt'
    
    def get_path_file_test_two():
        return os.getcwd() + '\\test_files\\File_test2.txt'