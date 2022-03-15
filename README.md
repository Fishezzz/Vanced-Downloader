# Vanced Downloader

Python script to download all YouTube Vanced files at once. Based on [MinePlayersPE/vanced_adbinstall.py](https://gist.github.com/MinePlayersPE/e983d6603059bd821f0b3b287949f36a).

- [Vanced Downloader](#vanced-downloader)
- [Usage](#usage)
  - [SHA256 sums](#sha256-sums)
- [Files](#files)
  - [Vanced Manager](#vanced-manager)
  - [Vanced MicroG](#vanced-microg)
  - [Vanced Music](#vanced-music)
  - [Vanced](#vanced)
  - [Vanced (root)](#vanced-root)

# Usage

First clone this repository on your PC using the CLI or download it as a zip and extract it.

Make sure you have installed python.

Install the required packages:

```
pip install tqdm requests
```

To download all the apks at once, execute the following python script:

```
python vanced_downloader.py
```

It will download all the latest apks and place them in a folder structure that looks like this:

```
com.vanced.manager/
    file/
        manager/
        microg/
        music/
            nonroot/
            root/
        vanced/
            nonroot/
            root/
```

This is how (part of) your filesystem would look like on your phone after you installed Vanced/Music using Vanced Manager. (not all folders would be present)

On your phone they should be stored at: `/Internal Storage/Android/data/com.vanced.manager` (or a similar location)

Some notes:
- you might not be able to see these files on your phone (I used to be able to, but now I can no longer access the `Android/data` folder)
- you need to use your PC to copy the apks onto your phone
- you might need to enable USB data transfer/switch USB mode when connecting your phone to your PC

## SHA256 sums

***Only works on Linux***

To check the integrity of the files you downloaded, you can calculate the SHA256 sum of the apk(s) and and compare them with the checksums that are listed further below.

To check one apk:

```
sha256sum <path/to/apk>
```

To check all the apks at once:

```bash
chmod +x sha.sh # make it executable
./sha.sh
```

This will append all the checksums to this file ([README.md](README.md)).

# Files

You only need the files that are required for the things you want to install. So choose what you want to install.

After you have made your selection, you can delete the files (and folders) that are not needed and copy the files to the correct location on your phone.
To ensure the files are in the correct location, do this in one of the following ways:

- Option 1
  - copy the folder `com.vanced.manager` that contains the downloaded files
  - on your PC: browse to the folder that **contains** the folder `com.vanced.manager` (eg.: `/Internal Storage/Android/data`)
  - paste the folder `com.vanced.manager` in the folder you just browsed to
  - if you get a prompt about merging folders or overwriting files/folders, click merge/overwrite/ok
- Option 2
  - copy the folder `files` that contains the downloaded files
  - on your PC: browse to the folder that **contains** the folder `files` (eg.: `/Internal Storage/Android/data/com.vanced.manager`)
  - paste the folder `files` in the folder you just browsed to
  - if you get a prompt about merging folders or overwriting files/folders, click merge/overwrite/ok
- Option 3
  - recreate the folder structure on your phone, using your phone or your PC
  - copy/paste each file you need to the correct location

## Vanced Manager

*[More info about Vanced Manager](https://github.com/YTVanced/VancedManager)*

*This is the only apk you don't need to place in a specific folder if you haven't installed Vanced/Vanced Manager or you want to reinstall it.*

| File | SHA256 sum |
|------|------------|
| [manager.apk](com.vanced.manager/files/manager/manager.apk) | c2da3df534ece06c4e87d60ae4690f4c58a9b6d3d05a45898181123201c1d8d9 |

## Vanced MicroG

*[More info about Vanced MicroG](https://github.com/YTVanced/VancedMicroG)*

Place this apk in the folder `com.vanced.manager/files/microg`

| File | SHA256 sum |
|------|------------|
| [microg.apk](com.vanced.manager/files/microg/microg.apk) | e5ce4f9759d3e70ac479bf2d0707efe5a42fca8513cf387de583b8659dbfbbbf |

## Vanced Music

Place this apk in the folder `com.vanced.manager/files/music/nonroot`

| File | SHA256 sum |
|------|------------|
| [nonroot.apk](com.vanced.manager/files/music/nonroot/nonroot.apk) | 47a8398198f1a5266a28dfcb6281d2b75a1146e0fe4f6d1bd878586d95752445 |

## Vanced Music (root)

This is the **rooted** version of Vanced Music. You can only install this if you have rooted your phone. If you don't know what this means, you should probably install the [normal version](#vanced-music).

Place this apk in the folder `com.vanced.manager/files/music/root`

| File | SHA256 sum |
|------|------------|
| [root.apk](com.vanced.manager/files/music/root/root.apk) | 59de7a375fa1c3c369fbce1d5e0d4e69f17f37b6214aac7777c5e582c3567bec |

## Vanced

*[More info about Vanced](https://github.com/YTVanced/Vanced)*

The following apks are needed for a succesful install:

- **one** of the "Theme" apks (dark or black)
- **one** of the "Architecture" apks (x86, arm64_v8a or armeabi_v7a)
- at least one of the "Language" apks

Place these apks in the folder `com.vanced.manager/files/vanced/nonroot`

### Theme

You need to choose **one** of these.

| File | SHA256 sum |
|------|------------|
| [dark.apk](com.vanced.manager/files/vanced/nonroot/dark.apk) | 80eedb9b772afd9f1b9ec3ee274453f5bb51bcfbdce72c636e0d0652d8fd2d3c |
| [black.apk](com.vanced.manager/files/vanced/nonroot/black.apk) | 45776ffc5407685f5846334985202a11f7bda22f6f89ab9968776b0c782436a4 |

### Architecture

You need to choose **one** of these.

`arm64_v8a` is the most likely option, so if you don't know which one to choose, take this one. If you know you have a x86 processor in your phone, choose `x86`.
If the first 2 options didn't work, or you have an older phone, you can try `armeabi_v7a`.

Another option is to try and put all 3 of the apks on your phone and the installer should chooses the correct one.

| File | SHA256 sum |
|------|------------|
| [split_config.x86.apk](com.vanced.manager/files/vanced/nonroot/split_config.x86.apk) | 14ecf337e54c3e3e4179517623504dd0d68774d91ea0a09ab341c262ca97a51c |
| [split_config.arm64_v8a.apk](com.vanced.manager/files/vanced/nonroot/split_config.arm64_v8a.apk) | 72c53df4d3bf0c32cca02245f02c5637a97d6f74a9946459151258c51e384d0a |
| [split_config.armeabi_v7a.apk](com.vanced.manager/files/vanced/nonroot/split_config.armeabi_v7a.apk) | 745e1fdaa3d639d1fd16f953c62e0b0608410e7307f5fbdcd69e0782c270003f |

### Language

You need at least one of these, but you can select multiple. Just make sure to remember which languages you selected, so you can correctly check the in the list of languages in the installer.

| Language (en) | Language | File | SHA256 sum |
|---------------|----------|------|------------|
| Afrikaans | Afrikaans | [split_config.af.apk](com.vanced.manager/files/vanced/nonroot/split_config.af.apk) | e6c20907a4cd688a339bc24d06f5f96945c4a1e3ce2ba85f111d6375030b3c79 |
| Amharic | አማርኛ | [split_config.am.apk](com.vanced.manager/files/vanced/nonroot/split_config.am.apk) | 517d680157623c59ec59da8676c2b0b39ef859781e02ab6cdf5540b91f49e41f |
| Arabic | العربية | [split_config.ar.apk](com.vanced.manager/files/vanced/nonroot/split_config.ar.apk) | 1add343c7b7c1724a8193a4c9a83b01ba9c610c08f6e02c0b184d2e04a7637a1 |
| Azeri | Azərbaycan­ılı | [split_config.az.apk](com.vanced.manager/files/vanced/nonroot/split_config.az.apk) | fa4676ba6736cde7191d62545135911cf4e0beb9ffd763216c652e5ce4098990 |
| Belarusian | беларуская | [split_config.be.apk](com.vanced.manager/files/vanced/nonroot/split_config.be.apk) | c65444681c7475dc34e55f653513b3b2229b29bc70961556362d1420eab86494 |
| Bulgarian | български | [split_config.bg.apk](com.vanced.manager/files/vanced/nonroot/split_config.bg.apk) | 204447fbaed3f4de3b62e79a88d60230422ff62ef459be8dfca2b29bcda23b40 |
| Bengali | বাংলা | [split_config.bn.apk](com.vanced.manager/files/vanced/nonroot/split_config.bn.apk) | 49031570020314af3cd373be705ebc26394dfd2d72e0d75f4ecdb165b92462de |
| Bosnian | босански | [split_config.bs.apk](com.vanced.manager/files/vanced/nonroot/split_config.bs.apk) | eded2300225c3e72e60a26f227cc12f7e606c114ccce0e6b8529f1ac269103b3 |
| Catalan | català | [split_config.ca.apk](com.vanced.manager/files/vanced/nonroot/split_config.ca.apk) | 95bf4543a0a807ffe103256b53c55f71acd23d63ca7cfd2afe9df6fd1c3eca51 |
| Czech | čeština | [split_config.cs.apk](com.vanced.manager/files/vanced/nonroot/split_config.cs.apk) | e001bdd62f4e540e0fa7d1924057eeacf67569d2179e87f9f77387deee2f870e |
| Danish | dansk | [split_config.da.apk](com.vanced.manager/files/vanced/nonroot/split_config.da.apk) | 9ab3dddd57d1b08b290b0c400bd22fa23035138c40603b2667d3ceca44251389 |
| German | Deutsch | [split_config.de.apk](com.vanced.manager/files/vanced/nonroot/split_config.de.apk) | 5242514e8fddae20a61563d5df2a71f6f6aff70a1c58b00c9801479a6d7022ce |
| Greek | ελληνικά | [split_config.el.apk](com.vanced.manager/files/vanced/nonroot/split_config.el.apk) | 147c7cf0e7777c38dbcf3da0ae78b094a619825a226724cc792616631b08e5e3 |
| English | English | [split_config.en.apk](com.vanced.manager/files/vanced/nonroot/split_config.en.apk) | 1ac71651012966619cecb09ff5a3d499796e048ce3cd60429642392073734c1d |
| Spanish | español | [split_config.es.apk](com.vanced.manager/files/vanced/nonroot/split_config.es.apk) | 1fcd56aaf01147a12c08ec9cb27e5a4541fb1f3c70a52209c279349bee0ae744 |
| Estonian | eesti | [split_config.et.apk](com.vanced.manager/files/vanced/nonroot/split_config.et.apk) | bc70e6c7be89b655d74e91c835588418d94a9e59e59e011f1a19493723485b87 |
| Basque | euskara | [split_config.eu.apk](com.vanced.manager/files/vanced/nonroot/split_config.eu.apk) | b7436822ade61ea013b0defd341539f80e6f3a59b86d4db7dfeab5312a1f07fc |
| Persian | فارسى | [split_config.fa.apk](com.vanced.manager/files/vanced/nonroot/split_config.fa.apk) | 1a7b0700a9c0654d8bb79414ebcbaf1076acb1d069f6a0d5ee61ea6edd170132 |
| Finnish | suomi | [split_config.fi.apk](com.vanced.manager/files/vanced/nonroot/split_config.fi.apk) | 8ac2cf96ab5b7fc00d3fd6b0febbc9af30e59281d22346a39de58b7ac1c89710 |
| French | français | [split_config.fr.apk](com.vanced.manager/files/vanced/nonroot/split_config.fr.apk) | 442b24ef574ed35f6b0db78d928abd38c0dda4c4bacaa5567ad6b50a2dce0b87 |
| Galician | galego | [split_config.gl.apk](com.vanced.manager/files/vanced/nonroot/split_config.gl.apk) | 485ed491893afb10a30c007fd4d3fecba4c9653b68c90800b6b927b1c49a3628 |
| Gujarati | ગુજરાતી | [split_config.gu.apk](com.vanced.manager/files/vanced/nonroot/split_config.gu.apk) | 880a151e04ab86d33d96aa0c149a9622ab82748001e27497cf3d9b71e658fec0 |
| Hindi | हिंदी | [split_config.hi.apk](com.vanced.manager/files/vanced/nonroot/split_config.hi.apk) | 0e79551e3633fa92ffa4cc4fda6f2a7c69403daf4d2eee5f395f3f4ee06ef6cc |
| Croatian | hrvatski | [split_config.hr.apk](com.vanced.manager/files/vanced/nonroot/split_config.hr.apk) | ade17321b0a70c6047e98c7aed0ad50cae3143dcf94dedf029a4eef67da214a0 |
| Hungarian | magyar | [split_config.hu.apk](com.vanced.manager/files/vanced/nonroot/split_config.hu.apk) | 9ec03c075c8ecba5e66b5e3b9fed108cb265886822a28556644bb2f2ff7d8810 |
| Armenian | Հայերեն | [split_config.hy.apk](com.vanced.manager/files/vanced/nonroot/split_config.hy.apk) | 1f8b10cdf9824191e66e8129e5cbbb92f08bea8fa1bc38374fce3755f82d8fbc |
| Indonesian | Bahasa Indonesia | [split_config.in.apk](com.vanced.manager/files/vanced/nonroot/split_config.in.apk) | fa39a9b16ff98ceed4f966a1849549a484e6c104395cc2e61c48c43387cefbda |
| Icelandic | íslenska | [split_config.is.apk](com.vanced.manager/files/vanced/nonroot/split_config.is.apk) | 77015113178c4071ebbbf37d9a157084f5f2b84443d9ab3a02ebda0cef080dfe |
| Italian | italiano | [split_config.it.apk](com.vanced.manager/files/vanced/nonroot/split_config.it.apk) | 073d1e01f4bf0f64f0113f3a62163b9d12c9a262d93e61096d33de9b8a63f4bb |
| Hebrew | עברית | [split_config.iw.apk](com.vanced.manager/files/vanced/nonroot/split_config.iw.apk) | d9775b4e744f365d76c28f7955d6d81b87308e17cd3631d135a0cebcbaf93f67 |
| Japanese | 日本語 | [split_config.ja.apk](com.vanced.manager/files/vanced/nonroot/split_config.ja.apk) | 905c939344557b644492a698c2ced15a0179b46808c6d7d3e6089c245ca60999 |
| Georgian | ქართული | [split_config.ka.apk](com.vanced.manager/files/vanced/nonroot/split_config.ka.apk) | 7e9518ac4a4d0df4fb3e68484ed7339ce81d19c3b0f4386fbf00d0c3cd045c17 |
| Kazakh | Қазащb | [split_config.kk.apk](com.vanced.manager/files/vanced/nonroot/split_config.kk.apk) | da7abcd7a2dcaab0c04af34b8a5317da919dd9aee91399aa2c0119b314e649a8 |
| Khmer | ខ្មែរ | [split_config.km.apk](com.vanced.manager/files/vanced/nonroot/split_config.km.apk) | 69c7075ac8f0e0e7237468cf0277f0754a226cd37cc406e83f61fcb910a58998 |
| Kannada | ಕನ್ನಡ | [split_config.kn.apk](com.vanced.manager/files/vanced/nonroot/split_config.kn.apk) | 1e26ef2c4c871185a742e30f8adf6404a251dc62f444f50eebfe8e8de26666b2 |
| Korean | 한국어 | [split_config.ko.apk](com.vanced.manager/files/vanced/nonroot/split_config.ko.apk) | 049e2a9c37bddd480ff473abac74fe6d81715e4c083d24e3e7e3fc5666683417 |
| Kyrgyz | Кыргыз | [split_config.ky.apk](com.vanced.manager/files/vanced/nonroot/split_config.ky.apk) | f8516c55807e5b30c64ce0337792a19458f01484d8c3e8c2b8e04fa047787f85 |
| Lao | ລາວ | [split_config.lo.apk](com.vanced.manager/files/vanced/nonroot/split_config.lo.apk) | 45c09f66bebc3b456637baebe02527f5ed32115bc78e48cd3152fcd946949fc0 |
| Lithuanian | lietuvių | [split_config.lt.apk](com.vanced.manager/files/vanced/nonroot/split_config.lt.apk) | a158a5259d70d087168c3b55fed01668cebec6a485c8bfe38e175738d176cbbf |
| Latvian | latviešu | [split_config.lv.apk](com.vanced.manager/files/vanced/nonroot/split_config.lv.apk) | b743c4a84a872ab96a935ad846bcb24bcf2ba27c7abbfebb82db6a80dd89a9bf |
| Macedonian | македонски јазик | [split_config.mk.apk](com.vanced.manager/files/vanced/nonroot/split_config.mk.apk) | b88f25d7039ba7dc2386ae9d9edc288615bfed6c17674b782f57b7b65fddaafb |
| Malayalam | മലയാളം | [split_config.ml.apk](com.vanced.manager/files/vanced/nonroot/split_config.ml.apk) | 2102894a8d967c35ae270b26a96df69353b773cb09bc62b996332d33a6074920 |
| Mongolian | Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ | [split_config.mn.apk](com.vanced.manager/files/vanced/nonroot/split_config.mn.apk) | 5a4ab00c272da503cceda5172c1e355cc3d4b7deab3860f7833312710f2f648b |
| Marathi | मराठी | [split_config.mr.apk](com.vanced.manager/files/vanced/nonroot/split_config.mr.apk) | 5e5b0b25583123c2f7ff27a62b2f39e2ab4588ab2407349ff45a9567575302da |
| Malay | Bahasa Malaysia | [split_config.ms.apk](com.vanced.manager/files/vanced/nonroot/split_config.ms.apk) | 07f79b578f9ef6cb9943e57c300c09962e2ceb06cd2c15650ffd8b7103cd74a2 |
| Burmese | Myanmar | [split_config.my.apk](com.vanced.manager/files/vanced/nonroot/split_config.my.apk) | 5ccf304edf2a9a54780eeae81eae26d1c8a7d28ec29919dbf8e04ba7e60dbdef |
| Norwegian (Bokmål) | norsk (bokmål) | [split_config.nb.apk](com.vanced.manager/files/vanced/nonroot/split_config.nb.apk) | 5d2993fd6174fbc661aa7edf0f473979ac368b8b830ffac719e63c476fbee3f0 |
| Nepali | नेपाली (नेपाल) | [split_config.ne.apk](com.vanced.manager/files/vanced/nonroot/split_config.ne.apk) | d08bda208a09e239996425012ecf6eaf390ea455e8e6003e2f24e7198a7038d1 |
| Dutch | Nederlands | [split_config.nl.apk](com.vanced.manager/files/vanced/nonroot/split_config.nl.apk) | 422f291cfe736d46ee96ced79cc6115fe69c4711073ffd4a45c77cddd1e3a8a7 |
| Punjabi | ਪੰਜਾਬੀ | [split_config.pa.apk](com.vanced.manager/files/vanced/nonroot/split_config.pa.apk) | b73d1c5f9d4632788cbfc578d9ca4fe6f9715cdfd307b20bf673ae2e908b62ad |
| Polish | polski | [split_config.pl.apk](com.vanced.manager/files/vanced/nonroot/split_config.pl.apk) | 80856e3fa0f83d5d08de326ff12a3b7b09ae0e7a6a0c53013aef869ef1cad343 |
| Portuguese | Português | [split_config.pt.apk](com.vanced.manager/files/vanced/nonroot/split_config.pt.apk) | ef674d912b8494940a0dbf26c2dbe7a9351acdeebd46d18661acc49663a56802 |
| Romanian | română | [split_config.ro.apk](com.vanced.manager/files/vanced/nonroot/split_config.ro.apk) | 3556a179ea8156b0de3be9b7c81fc8ee259741d760dc7bd62111d413a46c6374 |
| Russian | русский | [split_config.ru.apk](com.vanced.manager/files/vanced/nonroot/split_config.ru.apk) | ba19051f9451e758eb2799b4d8d66fb7962477f3eab1545f0cdc848c7074b06c |
| Sinhala | සිංහ | [split_config.si.apk](com.vanced.manager/files/vanced/nonroot/split_config.si.apk) | a877d9844f46f5639adbc02971963745bf1dc712d2a5642bcede091d823fe886 |
| Slovak | slovenčina | [split_config.sk.apk](com.vanced.manager/files/vanced/nonroot/split_config.sk.apk) | 85007ddd621301fd74318630bcfc6569420f6b531d8160355bfcbe1be971c837 |
| Slovenian | slovenski | [split_config.sl.apk](com.vanced.manager/files/vanced/nonroot/split_config.sl.apk) | 19be426c957ccce4d7de9e061b863cbeec61f155d1a65b58872a09103105f157 |
| Albanian | shqipe | [split_config.sq.apk](com.vanced.manager/files/vanced/nonroot/split_config.sq.apk) | 707ac5494ba6f074923c928125349341d8c8d4268336485d85b33a536659fd28 |
| Serbian | srpski/српски | [split_config.sr.apk](com.vanced.manager/files/vanced/nonroot/split_config.sr.apk) | 6100d9238c2f20bc47ec5de5f340febf3fc76e7aed06609da2fd6014eb32d280 |
| Swedish | svenska | [split_config.sv.apk](com.vanced.manager/files/vanced/nonroot/split_config.sv.apk) | 40ad316be63f1c3670a724f149ddea318dedd03eade8829a00a53a094a264cd5 |
| Kiswahili | Kiswahili | [split_config.sw.apk](com.vanced.manager/files/vanced/nonroot/split_config.sw.apk) | 5ca6eb17793d87f21945b3e6747714a4d99c58c70cac2aa88579bb89c7c7b1a6 |
| Tamil | தமிழ் | [split_config.ta.apk](com.vanced.manager/files/vanced/nonroot/split_config.ta.apk) | dd2d5dd6a7225b36897554b1890046acf184f496906a2cd3864df4a2cc74f124 |
| Telugu | తెలుగు | [split_config.te.apk](com.vanced.manager/files/vanced/nonroot/split_config.te.apk) | a2a9cba97aff46c5366ce5d595d0682b2b7266596a9f81195807c8d5871af2f8 |
| Thai | ไทย | [split_config.th.apk](com.vanced.manager/files/vanced/nonroot/split_config.th.apk) | c15632e445f556142a00278abf6460d5cb6baab9f9630ef83cc089886916ab4e |
| Tagalog | Wikang Tagalog | [split_config.tl.apk](com.vanced.manager/files/vanced/nonroot/split_config.tl.apk) | 3df76535a6253cb6ae81cdb43d6075e37db7cfa0bc0b963fc697343010578659 |
| Turkish | Türkçe | [split_config.tr.apk](com.vanced.manager/files/vanced/nonroot/split_config.tr.apk) | ebdfa7444da279b23affb919b1e479b05b6fd758e43a2d976121665355bace02 |
| Ukrainian | українська | [split_config.uk.apk](com.vanced.manager/files/vanced/nonroot/split_config.uk.apk) | c3813269e5e0e39b6192556a2c4c0cceaff9171de4dca884aba9c54d7979510e |
| Urdu | اُردو | [split_config.ur.apk](com.vanced.manager/files/vanced/nonroot/split_config.ur.apk) | 58816faa4432e374599641e036d16ffd9f6dec8445e5891437cf2e66b265eaec |
| Uzbek | U'zbek/Ўзбек | [split_config.uz.apk](com.vanced.manager/files/vanced/nonroot/split_config.uz.apk) | 758d9b6b9247a15a6b1e309a5f6548ff1b005fad374ef1e74c34225b7a02ee8f |
| Vietnamese | Tiếng Việt | [split_config.vi.apk](com.vanced.manager/files/vanced/nonroot/split_config.vi.apk) | 392bb405db4b7c9f59f1ae1dbba8290846e2f3483a3026e1a00a680bc5004b41 |
| Chinese | 中文 | [split_config.zh.apk](com.vanced.manager/files/vanced/nonroot/split_config.zh.apk) | d2ea3e056a6a032c0f2076e01b19cbae1bbe7ae787ab0d80974ace191e9cfb5c |
| isiZulu | isiZulu | [split_config.zu.apk](com.vanced.manager/files/vanced/nonroot/split_config.zu.apk) | 2971fb4f006f0c9da948ddfb140ebf539be26d50e0d666ead9403ef679f83e35 |

## Vanced (root)

This is the **rooted** version of Vanced. You can only install this if you have rooted your phone. If you don't know what this means, you should probably install the [normal version](#vanced).

Place these apks in the folder `com.vanced.manager/files/vanced/root`

### Theme

You need to choose **one** of these.

| File | SHA256 sum |
|------|------------|
| [black.apk](com.vanced.manager/files/vanced/root/black.apk) | ba1a22f4dcc1821a592988647b5d761bc0632bb15ceb8b09eb9fb69be6979c83 |
| [dark.apk](com.vanced.manager/files/vanced/root/dark.apk) | c473f53cec7808f2765ced8f37d3558971c9d94ae12ff3f61abaeb213f80d430 |

### Architecture

You need to choose **one** of these.

`arm64_v8a` is the most likely option, so if you don't know which one to choose, take this one. If you know you have a x86 processor in your phone, choose `x86`.
If the first 2 options didn't work, or you have an older phone, you can try `armeabi_v7a`.

Another option is to try and put all 3 of the apks on your phone and the installer should chooses the correct one.

| File | SHA256 sum |
|------|------------|
| [split_config.x86.apk](com.vanced.manager/files/vanced/root/split_config.x86.apk) | 4e570a4570ebe41882a44eeaae4149c39faa3969e8712bac5fb39460057a1cf8 |
| [split_config.arm64_v8a.apk](com.vanced.manager/files/vanced/root/split_config.arm64_v8a.apk) | 389083b9713a59a9f71e2ab26ffbbdbf5df3df20ef047f96d7f3a1ce5bb936b8 |
| [split_config.armeabi_v7a.apk](com.vanced.manager/files/vanced/root/split_config.armeabi_v7a.apk) | 0eb8b298404cf07129a30a667392a5258da16c61d461e4e4c10e951b20eb351c |

### Language

You need at least one of these, but you can select multiple. Just make sure to remember which languages you selected, so you can correctly check the in the list of languages in the installer.

| Language (en) | Language | File | SHA256 sum |
|---------------|----------|------|------------|
| Afrikaans | Afrikaans | [split_config.af.apk](com.vanced.manager/files/vanced/root/split_config.af.apk) | 7a00bde45be4518346c0e86cca7f73a19fcc0152b24e0c95a4e8a3ad8b57531b |
| Amharic | አማርኛ | [split_config.am.apk](com.vanced.manager/files/vanced/root/split_config.am.apk) | 60772bfd589e69441a3cf73214aaa4d3e98c28f6056d3bae55a95ee27de29a03 |
| Arabic | العربية | [split_config.ar.apk](com.vanced.manager/files/vanced/root/split_config.ar.apk) | 359941cb1a892e516b284ed8aa06b2a76370f0dc662cb9d974f3b7029ade6607 |
| Azeri | Azərbaycan­ılı | [split_config.az.apk](com.vanced.manager/files/vanced/root/split_config.az.apk) | 62c54d79428e53429420944dfcc78b4c12f7aaf61d6e44e5d09973d8a845f9db |
| Belarusian | беларуская | [split_config.be.apk](com.vanced.manager/files/vanced/root/split_config.be.apk) | 26943f95d11cd3a4a5e793bcdc88f09d0bd2f0653baf62c4a911d7ff9f34ad57 |
| Bulgarian | български | [split_config.bg.apk](com.vanced.manager/files/vanced/root/split_config.bg.apk) | ae0c5c9e5e579d7ac5b3aca0e9aba8d729d69225f56092661588aee3f0b51506 |
| Bengali | বাংলা | [split_config.bn.apk](com.vanced.manager/files/vanced/root/split_config.bn.apk) | a3d897b563d584e4f32f0ab1139ab0dfe01a1e7fcb26d35c13273b29ce724ed5 |
| Bosnian | босански | [split_config.bs.apk](com.vanced.manager/files/vanced/root/split_config.bs.apk) | 7300d9762eb93f49d978f1d40bd2ead6c82328f9bc6ed54eb1ca044e30733aa1 |
| Catalan | català | [split_config.ca.apk](com.vanced.manager/files/vanced/root/split_config.ca.apk) | 9472e0e8353d6c8f235eee86f167ca317ab095018adcbdda06fbc2c229a937fc |
| Czech | čeština | [split_config.cs.apk](com.vanced.manager/files/vanced/root/split_config.cs.apk) | e7d68ae17f59a6daf165f8415e6c72690e261b216916eb0591e871f2fa547977 |
| Danish | dansk | [split_config.da.apk](com.vanced.manager/files/vanced/root/split_config.da.apk) | 5c8493234a043a74c4a64fed893951358ccf0942b9c8e3e54e204d06f96a00f8 |
| German | Deutsch | [split_config.de.apk](com.vanced.manager/files/vanced/root/split_config.de.apk) | 9322f3db646327e559aec90af0773f85571a2c611822cf2eaa19a78ab9886ce9 |
| Greek | ελληνικά | [split_config.el.apk](com.vanced.manager/files/vanced/root/split_config.el.apk) | 2bd1d6128010d89e33f885222f8ac0a33c1fb65918daa79854aa2d346396d252 |
| English | English | [split_config.en.apk](com.vanced.manager/files/vanced/root/split_config.en.apk) | d83e988a8bdb371a56662ee160b702e13a49ade5e655b6cbfe9f010873668094 |
| Spanish | español | [split_config.es.apk](com.vanced.manager/files/vanced/root/split_config.es.apk) | a1df5b76046494272a1b88d4c3dc69ffdb093b49817025d5b8e24ff8b4aa1d2e |
| Estonian | eesti | [split_config.et.apk](com.vanced.manager/files/vanced/root/split_config.et.apk) | 493cb23252d6e6ff9e38d0bc9fa03da481943107b87bd9cdcd58ef6b099ee1c8 |
| Basque | euskara | [split_config.eu.apk](com.vanced.manager/files/vanced/root/split_config.eu.apk) | 63d576514b89bfa2fdbea8695cf6f676852d25553542570091d6e07131e735b8 |
| Persian | فارسى | [split_config.fa.apk](com.vanced.manager/files/vanced/root/split_config.fa.apk) | 87ea075806dcc99f6e24495a7421d9deec45b244cb39dd18f7fbef9483403937 |
| Finnish | suomi | [split_config.fi.apk](com.vanced.manager/files/vanced/root/split_config.fi.apk) | 65848bb6ec5300f15824ff41463a09cd7f0630e28bebb2f5bce6ecb5ec7f863a |
| French | français | [split_config.fr.apk](com.vanced.manager/files/vanced/root/split_config.fr.apk) | 6e3913f9cb11f54282023620fa61e6becaa847da6462c0bdeb3b9b637706141d |
| Galician | galego | [split_config.gl.apk](com.vanced.manager/files/vanced/root/split_config.gl.apk) | 6077dd822dab2ce90abe0a512366610f105dbea1a8445e2ce1ea1e3743da6462 |
| Gujarati | ગુજરાતી | [split_config.gu.apk](com.vanced.manager/files/vanced/root/split_config.gu.apk) | 7eb3d043885a898929a2c5e5cb0e2f4f0a391530c70f00907e97a5ebcc4e2eca |
| Hindi | हिंदी | [split_config.hi.apk](com.vanced.manager/files/vanced/root/split_config.hi.apk) | 861d3ef7d62e0c53a978eb1d648cd065bd2b8097065ff81f0410b3b3a8a665a6 |
| Croatian | hrvatski | [split_config.hr.apk](com.vanced.manager/files/vanced/root/split_config.hr.apk) | 51574acdfba362e2a60b2f546fa86f44d53def86f484889eba8c882d1647aecf |
| Hungarian | magyar | [split_config.hu.apk](com.vanced.manager/files/vanced/root/split_config.hu.apk) | 222c8a112c39e2bd3a1a9269d54c8f72ed5ecfa24499d29da589526bee820143 |
| Armenian | Հայերեն | [split_config.hy.apk](com.vanced.manager/files/vanced/root/split_config.hy.apk) | ea4949243ae82e7ceb8b792ab3b39eec9c517ebed0509b7a2e00609aba28c5dd |
| Indonesian | Bahasa Indonesia | [split_config.in.apk](com.vanced.manager/files/vanced/root/split_config.in.apk) | 07ed16b1974b816c2cd1a46b4bd5531ffcbf5f0b4f07fd8629fcf5c1d7614e17 |
| Icelandic | íslenska | [split_config.is.apk](com.vanced.manager/files/vanced/root/split_config.is.apk) | 8c65234d89e365d48c7d356fc0a664170d3865d06d452cb89f3acacacbdddc78 |
| Italian | italiano | [split_config.it.apk](com.vanced.manager/files/vanced/root/split_config.it.apk) | b59c3ca81dc47299084822e4f52e2a3d7e9f1d9a9fc1ef04bb7eaf4705e76d36 |
| Hebrew | עברית | [split_config.iw.apk](com.vanced.manager/files/vanced/root/split_config.iw.apk) | 0a2bee180def9686b5fed3ea377a862d99788fd90e7e36924e5eb520b7d39ea3 |
| Japanese | 日本語 | [split_config.ja.apk](com.vanced.manager/files/vanced/root/split_config.ja.apk) | 53e6c1d30a8c763a5a87157c66ae3f5ef0f9c98fca31f0a9d9043ca88d584385 |
| Georgian | ქართული | [split_config.ka.apk](com.vanced.manager/files/vanced/root/split_config.ka.apk) | 0d53fe36c636c0f6562f8988598224c100814c5f8b699ff673fa254be5af11e6 |
| Kazakh | Қазащb | [split_config.kk.apk](com.vanced.manager/files/vanced/root/split_config.kk.apk) | 844340dbd76f139f4f697971820ff85f9b49f6a7c0946b38ced7ca9b0c58aaf9 |
| Khmer | ខ្មែរ | [split_config.km.apk](com.vanced.manager/files/vanced/root/split_config.km.apk) | a12b12059d68d9d86ad104b56c19b76f14941064ecde2abdf6b325d6ce64dada |
| Kannada | ಕನ್ನಡ | [split_config.kn.apk](com.vanced.manager/files/vanced/root/split_config.kn.apk) | d7e05093a692445d5454ea1fef54942ec21c2c775878450ed8ff2ae88a257bf6 |
| Korean | 한국어 | [split_config.ko.apk](com.vanced.manager/files/vanced/root/split_config.ko.apk) | ffd9f9bed6030cc81ecd6d48972888941996d860f29a1d607d64e9d48157bbff |
| Kyrgyz | Кыргыз | [split_config.ky.apk](com.vanced.manager/files/vanced/root/split_config.ky.apk) | 2c654cb228828ce52c4bd7269a8fd61b90495c56c8167da03b2db9248d98cb3a |
| Lao | ລາວ | [split_config.lo.apk](com.vanced.manager/files/vanced/root/split_config.lo.apk) | f873034d31b136fe008c7ef12fd844e39a4e60999baa1c9b3f8493181691c877 |
| Lithuanian | lietuvių | [split_config.lt.apk](com.vanced.manager/files/vanced/root/split_config.lt.apk) | 8a1dd4b78762be72ae3a032965476778834a295bfa2a8976cad9a5cc5abef0b8 |
| Latvian | latviešu | [split_config.lv.apk](com.vanced.manager/files/vanced/root/split_config.lv.apk) | 5398e884d24ef35a602b1100f56b1daecc5a1943e8d9a254ba7ca97a75c5fa34 |
| Macedonian | македонски јазик | [split_config.mk.apk](com.vanced.manager/files/vanced/root/split_config.mk.apk) | 5634a4909a4e29c029e9d672c4e82ecafd780731f582d65b7038b2a34779e11f |
| Malayalam | മലയാളം | [split_config.ml.apk](com.vanced.manager/files/vanced/root/split_config.ml.apk) | b0624159db7d62acf3d46725a27981ebc40638e097c1f0129f908deeecfdb079 |
| Mongolian | Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ | [split_config.mn.apk](com.vanced.manager/files/vanced/root/split_config.mn.apk) | c8e92dbf8194fb91b6f953a1d4053ce21109bf2ca06a34e1ce3cd8318550e80c |
| Marathi | मराठी | [split_config.mr.apk](com.vanced.manager/files/vanced/root/split_config.mr.apk) | c74124587d6314bf2e3622d7b8d2add562bfd61e13c51487c83a16c1e8a590f5 |
| Malay | Bahasa Malaysia | [split_config.ms.apk](com.vanced.manager/files/vanced/root/split_config.ms.apk) | 6dd64012b135a5e5f0d255794f3a32f64812914b40a9d1ed426df7c265a0daad |
| Burmese | Myanmar | [split_config.my.apk](com.vanced.manager/files/vanced/root/split_config.my.apk) | 1848f83b26d513ffbb967ee2e91465f143ebb0fca3977ca87eef9f0ffe117bf8 |
| Norwegian (Bokmål) | norsk (bokmål) | [split_config.nb.apk](com.vanced.manager/files/vanced/root/split_config.nb.apk) | 1ecdae29d9e345e6d69feb778b941d1ca4f77f6f8d3890ddecb36a514bbb4d5e |
| Nepali | नेपाली (नेपाल) | [split_config.ne.apk](com.vanced.manager/files/vanced/root/split_config.ne.apk) | 31f98cacbeb8a160b5fe24a1e1bca161c97a9214cf65de23dc19c7b783dc352f |
| Dutch | Nederlands | [split_config.nl.apk](com.vanced.manager/files/vanced/root/split_config.nl.apk) | e294bba36f52d53ec864ae99a3392e117079d5807ce9f757fbfc3ec33b3b7649 |
| Punjabi | ਪੰਜਾਬੀ | [split_config.pa.apk](com.vanced.manager/files/vanced/root/split_config.pa.apk) | 2219a0791065ebefe021927544b5858215487b88ca3255e54cf3d1ca0fe8d0d6 |
| Polish | polski | [split_config.pl.apk](com.vanced.manager/files/vanced/root/split_config.pl.apk) | 3dbaa470ea6aa5c08d13b478b69e64014cbc8a13de2e196417b4fd0ed100acb0 |
| Portuguese | Português | [split_config.pt.apk](com.vanced.manager/files/vanced/root/split_config.pt.apk) | 4e5158ac00b2ff08c5f3dd20ba2f643d07566c6f18ab5f5c71b779b1d7f398c5 |
| Romanian | română | [split_config.ro.apk](com.vanced.manager/files/vanced/root/split_config.ro.apk) | 9c830dba6222cc455913e830e5956314be73c53f98711eadb37abfe36b4b04ee |
| Russian | русский | [split_config.ru.apk](com.vanced.manager/files/vanced/root/split_config.ru.apk) | 3de05a5dce148aada91334575c7ea380a511fd123cb4bdfa38fc624c858c1249 |
| Sinhala | සිංහ | [split_config.si.apk](com.vanced.manager/files/vanced/root/split_config.si.apk) | 1853b57ce31c9ad872aaafb91e0c6000ce70f66e824a9ada9f5ee35d1ca58255 |
| Slovak | slovenčina | [split_config.sk.apk](com.vanced.manager/files/vanced/root/split_config.sk.apk) | 09261b8963b52b34a86febda82ac9092af672226d11932b36ae03e9b7982fad8 |
| Slovenian | slovenski | [split_config.sl.apk](com.vanced.manager/files/vanced/root/split_config.sl.apk) | 77909829d90aff882dfc1f2f3d967f30b0937e3039535eed65db65d593146c8b |
| Albanian | shqipe | [split_config.sq.apk](com.vanced.manager/files/vanced/root/split_config.sq.apk) | dd83f597d878a830bd81c19d6aafde8c677f927825d8b2fa6588ce1575a80278 |
| Serbian | srpski/српски | [split_config.sr.apk](com.vanced.manager/files/vanced/root/split_config.sr.apk) | 79f502b5127048d46adad94ff915e27f1d78b0dd57cd46ba4901c27e0c55b838 |
| Swedish | svenska | [split_config.sv.apk](com.vanced.manager/files/vanced/root/split_config.sv.apk) | 7999f5295e66f719edecc51744aedbd4c8a6472d0f343ba4a03ec589d0b65632 |
| Kiswahili | Kiswahili | [split_config.sw.apk](com.vanced.manager/files/vanced/root/split_config.sw.apk) | 681d4233835ea29977d763525827c04ba853f186c6bd0bfc112221ce28fe2f14 |
| Tamil | தமிழ் | [split_config.ta.apk](com.vanced.manager/files/vanced/root/split_config.ta.apk) | e17983387c63068f75eb69c7b58915c7bab3bcf122e22afa367d5e6b22587c43 |
| Telugu | తెలుగు | [split_config.te.apk](com.vanced.manager/files/vanced/root/split_config.te.apk) | aa99736db0898ea0927139bb6c8d01e341c5aca5dbfffe8155a373abf8555bf5 |
| Thai | ไทย | [split_config.th.apk](com.vanced.manager/files/vanced/root/split_config.th.apk) | 3a46a92a305684bf6fe1be182990ae0bdabd97eafffb2e0131012b7f0dec0b2e |
| Tagalog | Wikang Tagalog | [split_config.tl.apk](com.vanced.manager/files/vanced/root/split_config.tl.apk) | 47a6b153a7b160afcfd0c4bf6c44744df8b09a4728c93a717bc3a5894efca78a |
| Turkish | Türkçe | [split_config.tr.apk](com.vanced.manager/files/vanced/root/split_config.tr.apk) | 859646353b86cd3cb442ae186361061796151546b032efaf5ad2cd619d8af284 |
| Ukrainian | українська | [split_config.uk.apk](com.vanced.manager/files/vanced/root/split_config.uk.apk) | db200ad2e92d5c39513a31c71d99e1ec44c9028de7ab944b80cc51b213a4c453 |
| Urdu | اُردو | [split_config.ur.apk](com.vanced.manager/files/vanced/root/split_config.ur.apk) | 927ade4c12053c14aa46d05202385ff4ac73bd073bee67c509bf3709425f1ab2 |
| Uzbek | U'zbek/Ўзбек | [split_config.uz.apk](com.vanced.manager/files/vanced/root/split_config.uz.apk) | 70e981659849846d117f0f0d4bf5b7d4fecdd0a7d027342a47452b3609fd95a3 |
| Vietnamese | Tiếng Việt | [split_config.vi.apk](com.vanced.manager/files/vanced/root/split_config.vi.apk) | 6cac2644953be10713b4e406028ed6219ceba465afa34403516a31604f1bc60e |
| Chinese | 中文 | [split_config.zh.apk](com.vanced.manager/files/vanced/root/split_config.zh.apk) | c52b6498d11280b820a3e9091d40ca1b5a80026af26c2f0447883b3fa727cf23 |
| isiZulu | isiZulu | [split_config.zu.apk](com.vanced.manager/files/vanced/root/split_config.zu.apk) | a0c86c247ac4dbfee85c59bc3733b4112cdcb027a28677a07530bfed5c13cef6 |
