from tqdm import tqdm
import json
import os
import requests

API_URL = 'https://api.vancedapp.com/api/v1'
METADATA_URL_ARCHIVED = 'https://web.archive.org/web/20220315012841if_/https://api.vancedapp.com/api/v1/latest.json'
BAKCUP_DOWNLOAD_URL_BASE = 'https://github.com/Fishezzz/Vanced-Downloader/raw/master'

session = requests.Session()
session.headers['User-Agent'] = session.headers.get('User-Agent', 'python-requests') + ' Vanced Downloader'

response = session.get(API_URL + '/latest.json')
if response.status_code == 200:
    print('Retrieved metadata')
    latest_metadata = response.json()
    vanced_metadata = latest_metadata['vanced']
elif response.status_code == 404:
    print('Could not retrieve metadata! Trying Web Archive backup.')
    response2 = session.get(METADATA_URL_ARCHIVED)
    if response2.status_code == 200:
        print('Retrieved metadata from Web Archive backup.')
        latest_metadata = response2.json()
        vanced_metadata = latest_metadata['vanced']
    else:
        print('Could not retrieve metadata from Web Archive backup! Using local "latest.json" file.')
        with open('latest.json', 'r') as f:
            latest_metadata = json.loads(f.read())
            vanced_metadata = latest_metadata['vanced']

BASE_PATH = 'com.vanced.manager/files'
if not os.path.isdir('com.vanced.manager'):
    os.mkdir('com.vanced.manager')
if not os.path.isdir(BASE_PATH):
    os.mkdir(BASE_PATH)

def download(url: str, fname: str, session=requests):  # ripped from https://stackoverflow.com/a/62113293, modified for simpler syntax
    if BAKCUP_DOWNLOAD_URL_BASE not in url:
        return 2
    
    try:		
        resp = session.get(url, stream=True)
        with tqdm.wrapattr(
            open(fname, 'wb'), 'write',
            miniters=1,
            desc=fname,
            total=int(resp.headers.get('content-length', 0)),
        ) as file:
            for data in resp.iter_content(chunk_size=1024):
                size = file.write(data)
        return 0
    except:
        return 1

def multi_download(urls: [], apk_name: str, fname: str, session=requests):
    index = 0
    while index < len(urls) and download(urls[index], fname, session) != 0:
        print('URL not available: ' + urls[index])
        index += 1
    if index >= len(urls):
        print('Could not download ' + apk_name + ' apk!')

print('>> YouTube Vanced')

if not os.path.isdir(BASE_PATH + '/vanced'):
    os.mkdir(BASE_PATH + '/vanced')

version = vanced_metadata['version']
themes = vanced_metadata['themes']
langs = vanced_metadata['langs']

archs = ['x86', 'arm64_v8a', 'armeabi_v7a']
roots = ['nonroot', 'root']

for root in roots:
    path = BASE_PATH + '/vanced/' + root
    if not os.path.isdir(path):
        os.mkdir(path)
    
    vanced_url = API_URL + '/apks/v' + version + '/' + root
    
    print('Downloading vanced ' + root + ' themed apks...')
    for theme in themes:
        fullpath = path + '/' + theme + '.apk'
        THEME_URLS = [
            vanced_url + '/Theme/' + theme + '.apk',
            BAKCUP_DOWNLOAD_URL_BASE + fullpath
        ]
        apk_name = 'vanced ' + root + ' ' + theme
        #print('Downloading ' + apk_name + ' theme apk...')
        multi_download(THEME_URLS, apk_name, fullpath, session)
    
    print('Downloading vanced ' + root + ' language apks...')
    for lang in langs:
        fullpath = path + '/' + 'split_config.' + lang + '.apk'
        LANG_URLS = [
            vanced_url + '/Language/split_config.' + lang + '.apk',
            BAKCUP_DOWNLOAD_URL_BASE + fullpath
        ]
        apk_name = 'vanced ' + root + ' ' + lang
        #print('Downloading ' + apk_name + ' language apk...')
        multi_download(LANG_URLS, apk_name, fullpath, session)
    
    print('Downloading vanced ' + root + ' architecture apks...')
    for arch in archs:
        fullpath = path + '/' + 'split_config.' + arch + '.apk'
        ARCH_URLS = [
            vanced_url + '/Arch/split_config.' + arch + '.apk',
            BAKCUP_DOWNLOAD_URL_BASE + fullpath
        ]
        apk_name = 'vanced ' + root + ' ' + arch
        #print('Downloading ' + apk_name + ' architecture apk...')
        multi_download(ARCH_URLS, apk_name, fullpath, session)


print('>> Vanced Music')

if not os.path.isdir(BASE_PATH + '/music'):
    os.mkdir(BASE_PATH + '/music')

version = latest_metadata['music']['version']

for root in roots:
    path = BASE_PATH + '/music/' + root
    if not os.path.isdir(path):
        os.mkdir(path)
	
    fullpath = path + '/' + root + '.apk'
    MUSIC_URLS = [
        API_URL + '/music/v' + version + '/' + root + '.apk',
        BAKCUP_DOWNLOAD_URL_BASE + fullpath
    ]
    apk_name = 'music ' + root
    print('Downloading ' + apk_name + ' apk...')
    multi_download(MUSIC_URLS, apk_name, fullpath, session)


print('>> Manager')

if not os.path.isdir(BASE_PATH + '/manager'):
    os.mkdir(BASE_PATH + '/manager')

fullpath = BASE_PATH + '/manager/manager.apk'

MANAGER_URLS = [
    latest_metadata['manager']['url'],
    "https://github.com/YTVanced/VancedManager/releases/latest/download/manager.apk",
    "https://web.archive.org/web/20220314034640/https://github.com/YTVanced/VancedManager/releases/latest/download/manager.apk",
    "https://web.archive.org/web/20220314034640/https://github.com/YTVanced/VancedManager/releases/download/v2.6.2-262/manager.apk",
    "https://web.archive.org/web/20220314034641/https://objects.githubusercontent.com/github-production-release-asset-2e65be/247263904/cce7f0b8-e6ba-4a91-b2a3-9b71130bb0c8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220314T034640Z&X-Amz-Expires=300&X-Amz-Signature=0feda08b2fe9d6c6a52e19073b335c074a9c0cf6f6e874cdc55600835f71cbbc&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=247263904&response-content-disposition=attachment%3B%20filename%3Dmanager.apk&response-content-type=application%2Fvnd.android.package-archive",
    "https://github.com/Fishezzz/Vanced-Downloader/releases/latest/download/manager.apk",
    "https://fishezzz.github.io/vanced/manager.apk",
    BAKCUP_DOWNLOAD_URL_BASE + fullpath
]

print('Downloading manager apk...')
multi_download(MANAGER_URLS, 'manager', fullpath, session)


print('>> MicroG')

if not os.path.isdir(BASE_PATH + '/microg'):
    os.mkdir(BASE_PATH + '/microg')

fullpath = BASE_PATH + '/microg/microg.apk'

MICROG_URLS = [
    latest_metadata['microg']['url'],
    "https://github.com/YTVanced/VancedMicroG/releases/latest/download/microg.apk",
    "https://web.archive.org/web/20220314104604/https://github.com/YTVanced/VancedMicroG/releases/latest/download/microg.apk",
    "https://web.archive.org/web/20220314104605/https://github.com/YTVanced/VancedMicroG/releases/download/v0.2.24.2",
    "https://web.archive.org/web/20220314104605/https://objects.githubusercontent.com/github-production-release-asset-2e65be/249042622/a3db258c-c2eb-4c54-9e74-79da29291a14?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220314T104605Z&X-Amz-Expires=300&X-Amz-Signature=4c2c35a0ed2bdae20c830dc7c05ec40f6245e0d6aba876ce136d319638f5e94f&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=249042622&response-content-disposition=attachment%3B%20filename%3Dmicrog.apk&response-content-type=application%2Fvnd.android.package-archive",
    "https://github.com/Fishezzz/Vanced-Downloader/releases/latest/download/microg.apk",
    "https://fishezzz.github.io/vanced/microg.apk",
    BAKCUP_DOWNLOAD_URL_BASE + fullpath
]

print('Downloading microg apk...')
multi_download(MICROG_URLS, 'microg', fullpath, session)
