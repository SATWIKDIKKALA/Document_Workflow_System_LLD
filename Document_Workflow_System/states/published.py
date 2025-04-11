from abc import ABC, abstractmethod
from states.state import State
from exceptions.ErrorException import ErrorException
from enums.status import Status

class PublishedState(State):
    def edit(self, new_content):
        raise ErrorException("Cannot edit after document is published.")

    def submit(self):
        raise ErrorException("Cannot review after document is published.")

    def approve(self):
        raise ErrorException("Already Approved.")

    def reject(self):
        raise ErrorException("Published cannot be rejected.")
