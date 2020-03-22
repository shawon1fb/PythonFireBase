from threading import Thread
import firebase_admin
from firebase_admin import credentials, firestore
from Downloader import download_wget


class ButtonData:
    def __init__(self, string, value):
        self.string = string
        self.value = value


category = {
    "1": "Accessories",
    "2": "Beauty & skin care",
    "3": "Jewelry",
    "4": "Shoes",
    "5": "Home décor",
    "6": "Technology",
    "7": "Watches",
}

l = [
    ButtonData(
        "Accessories",
        1,
    ),
    ButtonData(
        "Beauty & skin care",
        2,
    ),
    ButtonData(
        "Jewelry", 3,
    ),
    ButtonData(
        "Shoes",
        4,
    ),
    ButtonData(
        "Home décor",
        5,
    ),
    ButtonData(
        "Technology",
        6,
    ),
    ButtonData(
        "Watches",
        7,
    )
]


def fire():
    cred = credentials.Certificate("e-commerce-7c6f6-firebase-adminsdk-p7uhl-e42cfe1697.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection("Products")
    docs = doc_ref.stream()
    for doc in docs:
        v = doc.to_dict()
        print(v['ImageUrl'])
        image_url = v['ImageUrl']
        cat = v["productCategory"]
        print("\n")
        print("category:::::")
        print(category[cat])
        try:
            Thread(target=download_wget(image_url, path="Downloads/" + category[cat]))
        except Exception as e:
            print("Error: unable to start thread")
            print(e)


def main():
    fire()
    print("End program....")
    print("... Thank you ....")


main()
