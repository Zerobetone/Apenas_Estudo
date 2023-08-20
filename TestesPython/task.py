class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.created_at = None
        self.completed = False

    def mark_as_completed(self):
        self.completed = True