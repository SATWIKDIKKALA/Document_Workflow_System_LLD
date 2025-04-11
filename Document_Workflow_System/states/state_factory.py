from enums.status import Status
from states.draft import DraftState
from states.under_review import UnderReviewState
from states.published import PublishedState
from exceptions.ErrorException import ErrorException

class StateFactory:
    @staticmethod
    def get_state(document):
        if document.status == Status.DRAFT:
            return DraftState(document)
        elif document.status == Status.UNDER_REVIEW:
            return UnderReviewState(document)
        elif document.status == Status.PUBLISHED:
            return PublishedState(document)
        else:
            raise ErrorException("Unknown document state.")