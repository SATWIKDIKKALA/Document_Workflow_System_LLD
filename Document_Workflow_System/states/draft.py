from abc import ABC, abstractmethod
from states.state import State
from exceptions.ErrorException import ErrorException
from enums.status import Status

class DraftState(State):
    def edit(self, new_content):
        self.document.content = new_content

    def submit(self):
        self.document.set_state(Status.UNDER_REVIEW)

    def approve(self):
        raise ErrorException("Cannot approve a Draft document.")

    def reject(self):
        raise ErrorException("Cannot reject a Draft document.")
