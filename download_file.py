import os
import requests
from tqdm import tqdm


def download_file(url, path, username, token, version, build, distro):
    session = requests.session()
    r = session.get(url.format(version, build, distro, username, token), stream=True)

    file_name = r.headers['Content-Disposition'][21:]
    file_size = int(r.headers['Content-length'])

    abs_path = os.path.abspath(path + file_name)

    if not os.path.exists(abs_path) or os.path.getsize(abs_path) == file_size:
        progress_bar = tqdm(total=file_size, unit='byte', unit_scale=True, desc=file_name, dynamic_ncols=True)

        with open(path + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1048576):
                progress_bar.update(1048576)
                if chunk:
                    f.write(chunk)
                else:
                    print(chunk)
            f.close()
        progress_bar.close()
        session.close()

    else:
        print('{} already downloaded'.format(file_name))

    return abs_path, file_name
