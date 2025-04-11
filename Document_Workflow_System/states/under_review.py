from abc import ABC, abstractmethod
from states.state import State
from exceptions.ErrorException import ErrorException
from enums.status import Status

class UnderReviewState(State):
    def edit(self, new_content):
        raise ErrorException("Cannot edit a Draft document.")

    def submit(self):
        raise ErrorException("Already Under Review")

    def approve(self):
        self.document.set_state(Status.PUBLISHED)

    def reject(self):
        self.document.set_state(Status.DRAFT)