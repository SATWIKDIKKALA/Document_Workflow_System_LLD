from enums.status import Status
from states.state_factory import StateFactory

class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.status = Status.DRAFT
        self.state = StateFactory.get_state(self)

    def set_state(self, new_status):
        self.status = new_status
        self.state = StateFactory.get_state(self)

    def edit(self, new_content):
        self.state.edit(new_content)

    def submit(self):
        self.state.submit()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject()

    def __str__(self):
        return f"Document('{self.title}', Status: {self.status.value}, Content: {self.content})"