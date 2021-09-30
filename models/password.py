

class Password(object):

    def __init__(self, unique_id: str, application: str, username: str, email: str, description: str, website: str, category: str, passphrase: str):
        self.unique_id = unique_id
        self.application = application
        self.username = username
        self.email = email
        self.description = description
        self.website = website
        self.category = category
        self.passphrase = passphrase
