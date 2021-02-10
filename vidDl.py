import os
import requests
import ffmpeg

def addHttps(url):
    """

    :param url: Check url for https header. add header if none exists
    :return: url with https
    """

    return (url,' https://' + url)[url.find('https') == -1]


def parseM3(url):
    """

    :param url: A valid ubc.streaming m3u8 url
    :return: returns the links of all associated .ts files
    """

    content_type = 'application/vnd.apple.mpegurl'
    tsUrls = []

    try:
        r = requests.get(addHttps(url),timeout = 1)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    urlTemplate = '/'.join(url.split('/')[:-1]) +'/{}'

    urlTemplate = addHttps(urlTemplate)




    content = r.content.decode('utf-8')

    parts = content.split(',')

    for line in parts:
        if line.find('nseg'):

            tsUrl= urlTemplate.format(line[line.find('seg'):line.find('.ts')+3])

            tsUrls.append(tsUrl)


    return tsUrls



def start_download(url):
    """

    :param url: A valid streaming.video.ubc.ca/ url pointing to a m3u8 file
    :return: Associated video with the segments
    """


    tsUrls = parseM3(url)

    open('1.ts', 'wb').write(requests.get(urls[2]).content)












def stitch_vids():
    pass


def saveFile():
    pass


downurl = "streaming.video.ubc.ca/hls/p/113/sp/11300/serveFlavor/entryId/0_7c97s2hl/v/2/ev/2/flavorId/0_ptw0zujb/name/a.mp4/index.m3u8"
tsUrls = parseM3(downurl)


print(tsUrls[3])
# with open('1.ts','wb') as f:
#     f.write(requests.get(tsUrls[1]).content)
