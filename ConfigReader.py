import configparser

class ConfigClass:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("settings.ini", encoding="utf-8")


    def get_site_url(self):
        return self.config["SITE"]["url"]


    def get_camunda_url(self):
        return self.config["SITE"]["camunda"]
    

    def get_admin_login(self):
        return self.config["Auth"]["admin_login"]


    def get_admin_pass(self):
        return self.config["Auth"]["admin_pass"]

    
    def get_admin_role(self):
        return self.config["Auth"]["admin_role"]


    def get_sql_host(self):
        return self.config["postgres"]["host"]
    

    def get_sql_password(self):
        return self.config["postgres"]["password"]


    def get_sql_username(self):
        return self.config["postgres"]["username"]


    def get_sql_port(self):
        return self.config["postgres"]["port"]


    def get_database_name(self):
        return self.config["postgres"]["db"]


    def get_path_to_sertificate(self):
        return self.config["tests"]["path_to_sert"]
    

    def get_name_sert(self):
        return self.config["tests"]["name_sert"]
    

    def get_valid_from_date_sertificate(self):
        return self.config["tests"]["valid_from"]

    
    def get_thumnnail(self):
        return self.config["tests"]["thumbnail"]


    def get_path_to_download(self):
        return self.config["tests"]["path_to_download"]


    def change_password(self, password):
        self.config.set("Auth", "admin_pass", password)
        with open("settings.ini", "w", encoding="utf-8") as config_file:
            self.config.write(config_file)


    def get_path_to_upload(self):
        return self.config["tests"]["path_to_upload"]
    
    
    def get_second_user_login(self):
        return self.config["Auth"]["second_user_login"]


    def get_second_user_pass(self):
        return self.config["Auth"]["second_user_pass"]

    
    def get_second_user_role(self):
        return self.config["Auth"]["second_user_role"]


    def get_third_user_login(self):
        return self.config["Auth"]["third_user_login"]


    def get_third_user_pass(self):
        return self.config["Auth"]["third_user_pass"]

    
    def get_third_user_role(self):
        return self.config["Auth"]["third_user_role"]

    
    def get_third_user_contact(self):
        return self.config["Auth"]["third_user_contact"]
    

    def get_admin_contact_fio(self):
        return self.config["Auth"]["admin_contact_fio"]
    
    
    def get_ad_user_login(self):
        return self.config["Auth"]["ad_user_login"]


    def get_ad_user_pass(self):
        return self.config["Auth"]["ad_user_pass"]


    def get_contact_fio(self):
        return self.config["Auth"]["contact_fio"]
    

    def get_ad_admin_login(self):
        return self.config["Auth"]["ad_admin_login"]
    

    def get_ad_admin_pass(self):
        return self.config["Auth"]["ad_admin_pass"]
    
    
    def get_database_warehouse_name(self):
        return self.config["postgres"]["db_warehouse"]
    
    
    def get_second_path_to_sertificate(self):
        return self.config["tests"]["second_path_to_sert"]
    

    def get_second_name_sertificate(self):
        return self.config["tests"]["second_name_sert"]
    

    def get_second_valid_from_date_sertificate(self):
        return self.config["tests"]["second_valid_from"]

    
    def get_second_thumnnail(self):
        return self.config["tests"]["second_thumbnail"]
    

    def get_old_sert_thumnnail(self):
        return self.config["tests"]["old_sert_thumbnail"]
    

    def get_auth_url(self):
        return self.config["API"]["auth"]
    

    def get_auth_client_id(self):
        return self.config["API"]["client_id"]
    

    def get_auth_client_secret(self):
        return self.config["API"]["client_secret"]
    

    def get_auth_scope(self):
        return self.config["API"]["scope"]
    

    def get_auth_grant_type(self):
        return self.config["API"]["grant_type"]
    

    def get_gw_url(self):
        return self.config["API"]["gw"]
    
    def get_intbr_url(self):
        return self.config["API"]["intbr"]