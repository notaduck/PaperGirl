class Paper:
    def __init__(self, author, creator, producer, subject, title, file_name, path):
        # TODO: check out *args and **kwargs for less clutter in init call
        self.author = author
        self.creator = creator
        self.producer = producer
        self.subject = subject
        self.title = title
        self.file_name = file_name
        self.path = path
