import _thread
from threading import Thread

import firebase_admin
from firebase_admin import credentials, firestore

from Downloader import download_wget

from queue import Queue

q = Queue()


def fire():
    cred = credentials.Certificate("e-commerce-7c6f6-firebase-adminsdk-p7uhl-e42cfe1697.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection("Products")
    docs = doc_ref.stream()

    for doc in docs:
        v = doc.to_dict()
        # print(doc.to_dict())
        print(v['ImageUrl'])
        image_url = v['ImageUrl']
        print("\n")
        try:
            Thread(target=download_wget(image_url))
        except Exception as e:
            print("Error: unable to start thread")
            print(e)


def main():
    fire()

    print("test")
    print("test")


main()
