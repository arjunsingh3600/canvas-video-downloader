import os
import sys
import requests


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



def start_download(url,name):
    """

    :param url: A valid streaming.video.ubc.ca/ url pointing to a m3u8 file
    :return: Associated video with the segments
    """


    tsUrls = parseM3(url)

    index =0

    with open(name + '.ts', 'ab') as f:



        for url in tsUrls:

            os.system('cls')
            print('Downloading {}'.format(name))
            print('{} / {}'.format(index, len(tsUrls)))
            index = index + 1

            r = requests.get(url)
            if (r.status_code==200):
                f.write(r.content)

        print('downloaded')


if __name__ == "__main__":


    args = sys.argv

    if '.txt' not in args[1]:
        sys.exit(-1)
    else:
        print('invalid arg')
        filename = args[1] # file name with index urls




    with open(filename,'r') as url:
        links = url.read()


    links = links.split('\n')



    subList = [(links[n],links[n+1]) for n in range(0, len(links), 2)]



    for link in subList:
        if link[1] != '' and link[0] !='':
            start_download(link[1], link[0])



    sys.exit(0)



