import firebase as firebase
from firebase import firebase

fb = firebase.FirebaseApplication("https://e-commerce-7c6f6.firebaseio.com/", None)


def test():
    data = {
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
    }
    result = fb.post("", data)
    print(result)

test()