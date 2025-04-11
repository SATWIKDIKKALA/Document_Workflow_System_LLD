from document import Document
from exceptions.ErrorException import ErrorException

if __name__ == "__main__":
    doc = Document("Satwik's Book", "Biography")
    print(doc)

    doc.edit("Auto Biography")
    doc.submit()
    print(doc)

    try:
        doc.edit("trying to change under review")
    except ErrorException as e:
        print("Error:", e)

    doc.reject()
    print(doc)

    doc.edit("Made changes after rejection as Not an Auto Biography ")
    doc.submit()
    doc.approve()
    print(doc)

    try:
        doc.edit("After publishing attempts")
    except ErrorException as e:
        print("Error:", e)
    try:
        doc.approve()
    except ErrorException as e:
        print("Error:", e)