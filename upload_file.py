import requests


def upload_file(url, path, token, file_path, file_name):
    r = requests.get(url.format(path + file_name), headers={'Authorization': token})
    if r.status_code == 404:
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path={}&overwrite=true'.format(path + file_name)
        r = requests.session()
        resp = r.get(url, headers={'Authorization': token})
        upload_url = resp.json()['href']
        data = open(file_path, 'rb')
        resp = r.put(upload_url, data=data)

        print(resp.status_code)
        print("Uploading done")
    else:
        print("Already uploaded")
