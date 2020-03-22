import os

import wget


def download_requests(url, path="Downloads/"):
    import requests
    # only for firebase storage
    r = requests.get(url)
    temp = url.split('?')[0]
    imageName = temp.split('/')[-1]
    print(imageName)
    try:
        with open(path + imageName, 'wb') as f:
            f.write(r.content)
    except Exception as e:
        print("Download exception :::")
        print(e)

    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)


def download_wget(url, path="Downloads/"):
    print("download started ::::::::")
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            print("Execp::" + str(e))
    try:
        #   wget.download(url, path)
        download_requests(url=url, path=path + "/")

    except Exception as e:
        print(e)


"""try:
       wget.download(url, '/Users/scott/Downloads/cat4.jpg')
   except Exception as e:
       print("Download exception:::")
       print(e)"""

# download()
# download_wget(
#    'https://firebasestorage.googleapis.com/v0/b/gifter-d73d5.appspot.com/o/Men%20Shoes%2F41sn7yKkbbL.jpg?alt=media&token=3d434358-155d-40e4-9acb-de285d17d79c')
