Document Workflow System – Requirements

Statuses Supported:
The system should support a document that can exist in one of three statuses: 
Draft, Under Review, and Published.

Draft Editable:
A document in the Draft status should be editable.

Submit for Review:
The system should allow a document in the Draft status to be submitted, transitioning its status to Under Review.

No Edit in Review:
For a document that is Under Review, editing should be disallowed.

Review Outcomes:
The system should support two review outcomes for a document Under Review:

Approving the document should transition its status from Under Review to Published.

Rejecting the document should revert its status back to Draft.

Lock Published:
Once a document is Published, it should be locked from further modifications.

Enforce Valid Transitions:
The system should enforce valid transitions by ensuring that operations (edit, submit, approve, reject) are only allowed in their respective statuses.

Handle Invalid Operations Gracefully:
The system should handle invalid operations gracefully by providing clear error messages or notifications.

Future Enhancements:
The design should allow for future enhancements, such as additional statuses or operations in the document workflow.
