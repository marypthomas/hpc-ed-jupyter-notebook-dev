import json

class GMetaEntry:
    datatype = "GMetaEntry"

    def __init__(self, file_name, subject):
        # Fields required by Globus
        self.file_name = file_name
        self.subject = subject

        self.id = "std"
        self.visibility = '["public"]'

        self.content = {}

    def set_visibility(self, vis):
        self.visibility = vis

    def add_content(self, field, value):
        self.content[field] = value

    def remove_content(self, field):
        del self.content[field]
    
    def create_json(self):
        gmetaentry = {
            "@datatype": "GMetaEntry",
            "subject": self.subject,
            "visible_to": self.visibility,
            "content": self.content
        }
        json.dump(gmetaentry, open(f'output_data/{self.file_name}.json', 'w'), indent=4)