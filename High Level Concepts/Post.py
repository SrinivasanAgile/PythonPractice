class Post:
    #when user posts some info,then it has to be done with some functions inside this class
    # first function is to post the information
    def __init__(self, msg, author):
        self.message=msg
        self.author=author
    #this function is to fetch the posted message
    def get_post_info(self):
        print(f"{self.author} has posted the message as {self.message}")
