class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author
    
    def get_post_info(self):
        print(f"Pst: {self.message} written by {self.author}")