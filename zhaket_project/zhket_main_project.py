from zhaket_project.setting_of_zhaket_project import get_url, extract_data_form_excel, login, upload_new_plugin_and_save_old_plugin
from zhaket_project.setting_of_zhaket_project import remove_row_in_excel_file, get_plugins_url_which_insert_to_database, list_of_urles

 

path_excel_file=r""
# Pay attention that after the completion of the project, all the information in the Excel file will be deleted, so if you need the Excel file after the completion of the project, enter the path of the file that you copied from the original file here.
main_data=extract_data_form_excel(path_excel_file)


WEBSITE_KEY="6Ldfg4koAAAAABKRQfve_GSGoPGJadjdKTnakeeD"
PATH_EXTRACT_FILE=r""


def main(data):
    
    for (url, version, status, path, name) in data: 
        get_url(url)
        login(url,WEBSITE_KEY)  
        upload_new_plugin_and_save_old_plugin(path, PATH_EXTRACT_FILE, name, version, status, url)
        remove_row_in_excel_file(path_excel_file)
    get_plugins_url_which_insert_to_database(list_of_urles)    
        
main(main_data)
   

