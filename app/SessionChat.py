import time

class SessionChat:

    def __init__(self):
        self.members = ["user"]
        self.history = []

    def register_comment(self, member_name: str, comment: str):
        self.history.append((
            time.localtime(), member_name, comment
        ))

    def make_comment_tr(self, comment_t: tuple):
        timestamp, member_name, comment = comment_t
        return f"<tr><td>{member_name}</td><td>{comment}</td></tr>"
    
    def get_comments_table(self):
        comments_html = "".join([self.make_comment_tr(comment) for comment in self.history])
        return f"<table>{comments_html}</table>"
    
