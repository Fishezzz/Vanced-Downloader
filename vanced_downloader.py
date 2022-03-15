from tqdm import tqdm
import json
import os
import requests

API_URL = 'https://api.vancedapp.com/api/v1'
session = requests.Session()
session.headers['User-Agent'] = session.headers.get('User-Agent', 'python-requests') + ' Vanced Downloader'

latest_metadata = session.get(API_URL + '/latest.json').json()
vanced_metadata = latest_metadata['vanced']

BASE_PATH = 'com.vanced.manager/files'
if not os.path.isdir('com.vanced.manager'):
    os.mkdir('com.vanced.manager')
if not os.path.isdir(BASE_PATH):
    os.mkdir(BASE_PATH)

def download(url: str, fname: str, session=requests):  # ripped from https://stackoverflow.com/a/62113293, modified for simpler syntax
    resp = session.get(url, stream=True)
    with tqdm.wrapattr(
        open(fname, 'wb'), 'write',
        miniters=1,
        desc=fname,
        total=int(resp.headers.get('content-length', 0)),
    ) as file:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)

print('>> YouTube Vanced')

if not os.path.isdir(BASE_PATH + '/vanced'):
    os.mkdir(BASE_PATH + '/vanced')

version = vanced_metadata['version']
changelog = vanced_metadata['changelog']

themes = vanced_metadata['themes']
langs = vanced_metadata['langs']

archs = ['x86', 'arm64_v8a', 'armeabi_v7a']
roots = ['nonroot', 'root']

for root in roots:
    path = BASE_PATH + '/vanced/' + root
    if not os.path.isdir(path):
        os.mkdir(path)
    
    vanced_url = API_URL + '/apks/v' + version + '/' + root
    
    print('Downloading ' + root + ' themed apks...')
    for theme in themes:
        theme_url = vanced_url + '/Theme/' + theme + '.apk'
        #print('Downloading ' + root + ' ' + theme + ' theme apk...')
        download(theme_url, path + '/' + theme + '.apk', session)
    
    print('Downloading ' + root + ' language apks...')
    for lang in langs:
        lang_url = vanced_url + '/Language/split_config.' + lang + '.apk'
        #print('Downloading ' + lang + ' language apk...')
        download(lang_url, path + '/' + 'split_config.' + lang + '.apk', session)
    
    print('Downloading ' + root + ' architecture apks...')
    for arch in archs:
        arch_url = vanced_url + '/Arch/split_config.' + arch + '.apk'
        #print('Downloading ' + root + ' ' + arch + ' architecture apk...')
        download(arch_url, path + '/' + 'split_config.' + arch + '.apk', session)


print('>> Vanced Music')

if not os.path.isdir(BASE_PATH + '/music'):
    os.mkdir(BASE_PATH + '/music')

version = latest_metadata['music']['version']

for root in roots:
    path = BASE_PATH + '/music/' + root
    if not os.path.isdir(path):
        os.mkdir(path)
    
    music_url = API_URL + '/music/v' + version + '/' + root + '.apk'
    print('Downloading ' + root + ' apk...')
    download(music_url, path + '/' + root + '.apk', session)


print('>> Manager')

if not os.path.isdir(BASE_PATH + '/manager'):
    os.mkdir(BASE_PATH + '/manager')

#manager_url = latest_metadata['manager']['url']
#manager_url = "https://github.com/YTVanced/VancedManager/releases/latest/download/manager.apk"
#manager_url = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/247263904/cce7f0b8-e6ba-4a91-b2a3-9b71130bb0c8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220314T034640Z&X-Amz-Expires=300&X-Amz-Signature=0feda08b2fe9d6c6a52e19073b335c074a9c0cf6f6e874cdc55600835f71cbbc&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=247263904&response-content-disposition=attachment%3B%20filename%3Dmanager.apk&response-content-type=application%2Fvnd.android.package-archive"
manager_url = "https://web.archive.org/web/20220314034640/https://github.com/YTVanced/VancedManager/releases/latest/download/manager.apk"
#manager_url = "https://web.archive.org/web/20220314034640/https://github.com/YTVanced/VancedManager/releases/download/v2.6.2-262/manager.apk"
#manager_url = "https://web.archive.org/web/20220314034641/https://objects.githubusercontent.com/github-production-release-asset-2e65be/247263904/cce7f0b8-e6ba-4a91-b2a3-9b71130bb0c8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220314T034640Z&X-Amz-Expires=300&X-Amz-Signature=0feda08b2fe9d6c6a52e19073b335c074a9c0cf6f6e874cdc55600835f71cbbc&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=247263904&response-content-disposition=attachment%3B%20filename%3Dmanager.apk&response-content-type=application%2Fvnd.android.package-archive"
#manager_url = "https://fishezzz.github.io/vanced/manager.apk"

print('Downloading manager apk...')
download(manager_url, BASE_PATH + '/manager/manager.apk', session)


print('>> MicroG')

if not os.path.isdir(BASE_PATH + '/microg'):
    os.mkdir(BASE_PATH + '/microg')

microg_url = latest_metadata['microg']['url']
#microg_url = "https://github.com/YTVanced/VancedMicroG/releases/latest/download/microg.apk"
#microg_url = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/249042622/a3db258c-c2eb-4c54-9e74-79da29291a14?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220314T104605Z&X-Amz-Expires=300&X-Amz-Signature=4c2c35a0ed2bdae20c830dc7c05ec40f6245e0d6aba876ce136d319638f5e94f&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=249042622&response-content-disposition=attachment%3B%20filename%3Dmicrog.apk&response-content-type=application%2Fvnd.android.package-archive"
#microg_url = "https://web.archive.org/web/20220314104604/https://github.com/YTVanced/VancedMicroG/releases/latest/download/microg.apk"
#microg_url = "https://web.archive.org/web/20220314104605/https://github.com/YTVanced/VancedMicroG/releases/download/v0.2.24.220220-220220001/microg.apk"
#microg_url = "https://web.archive.org/web/20220314104605/https://objects.githubusercontent.com/github-production-release-asset-2e65be/249042622/a3db258c-c2eb-4c54-9e74-79da29291a14?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220314T104605Z&X-Amz-Expires=300&X-Amz-Signature=4c2c35a0ed2bdae20c830dc7c05ec40f6245e0d6aba876ce136d319638f5e94f&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=249042622&response-content-disposition=attachment%3B%20filename%3Dmicrog.apk&response-content-type=application%2Fvnd.android.package-archive"
#microg_url = "https://fishezzz.github.io/vanced/microg.apk"

print('Downloading microg apk...')
download(microg_url, BASE_PATH + '/microg/microg.apk', session)
