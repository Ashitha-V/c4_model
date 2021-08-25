#!usr/bin/python


import os
from DslFileCheck import DslFileCheck
from pyhtml_01 import DSLDashboard


# Main class calling all other classes (DslFileCheck and DSLDashboard)
class DslMain:
    file_name = ''
    file_path = ''

    def __init__(self, dir_path):
        self.file_path = dir_path

# Gets the DSL filename from the given directory.
    def get_file(self):
        # print("filename check - ", os.listdir(self.file_path))
        if len(os.listdir(self.file_path)) > 0:
            self.file_name = self.file_path + '/' + os.listdir(self.file_path)[0]
            print('DSL file name is - ', self.file_name)
            return self.file_name
        else:
            # print('The file location is wrong.')
            assert False, 'The file location is wrong.'
        # file_name = './dsl_files/' + file_name


#
if __name__ == '__main__':

    Dsl_obj = DslMain('./dsl_files')
    file_path = Dsl_obj.get_file()

    dslChk = DslFileCheck()

    file_data = dslChk.load_file(file_path)
    prod_dict = dslChk.dsl_file_product_chk()
    name_cont_dict, cont_dict, name_cont_map_dict, failed_cont_dict = dslChk.dsl_file_container_chk()
    print(cont_dict)
    print("----------------------------------------")
    print(failed_cont_dict.keys())
    container_status_dict = dslChk.dsl_file_cont_relation()
    env_dict = dslChk.dsl_file_depl_env()
    html_obj = DSLDashboard()
    html_obj.product_status(prod_dict, cont_dict, failed_cont_dict)
    html_obj.env_status(env_dict, failed_cont_dict)
    html_obj.each_product_status(prod_dict, name_cont_dict, name_cont_map_dict, container_status_dict, failed_cont_dict)
    html_obj.html_dashboard()
