class User:
    #attributed needed --> name, email, password, job-title
    # they shall be initiated with a concept of constructor and the parameters are mapped to relevant attributes
    def __init__(self, name, email, password, job_title):
        self.name=name
        self.email=email
        self.password=password
        self.job_title=job_title

    #behaviors needed --> as they belong to this class. they are called as methods and can be accessed by obejcts of this class
    #change_password --> password changing utility for user
    #change_title --> Job-title changing utility for user
    #get_info --> Utility to print the info of each object in the class

    def change_password(self, change_pwd):
        self.password=change_pwd


    def change_title(self,new_title):
        self.job_title=new_title


    def get_info(self):
        print(f"{self.name} is working as {self.job_title} and can be contacted by {self.email}")