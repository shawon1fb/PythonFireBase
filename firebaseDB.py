import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate("e-commerce-7c6f6-firebase-adminsdk-p7uhl-e42cfe1697.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://e-commerce-7c6f6.firebaseio.com/'
})


def SetDataToFirebasse():
    ref = db.reference('/')
    ref.set({
        'boxes':
            {
                'box001': {
                    'color': 'red',
                    'width': 1,
                    'height': 3,
                    'length': 2
                },
                'box002': {
                    'color': 'green',
                    'width': 1,
                    'height': 2,
                    'length': 3
                },
                'box003': {
                    'color': 'yellow',
                    'width': 3,
                    'height': 2,
                    'length': 1
                }
            }
    })


SetDataToFirebasse()