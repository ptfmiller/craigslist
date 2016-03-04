import json
import subprocess
from emailer import sendMail


if __name__ == '__main__':
    try:
        with open('/home/ec2-user/scraping/craigslist_sample/archive.json') as archiveFile:
            archive = json.load(archiveFile)
    except:
        archive = []
    subprocess.call("bash /home/ec2-user/scraping/craigslist_sample/update_bunk.sh", shell=True)
    with open('/home/ec2-user/scraping/craigslist_sample/bunkbed.json') as newFile:
        newData = json.load(newFile)
    newItems = []
    for item in newData:
        if item in archive:
            pass
        else:
            found = False
            for archiveItem in archive:
                if item['title'] == archiveItem['title'] and item['price'] == archiveItem['price']:
                    found = True
            if found:
                pass
            else:
                newItems.append(item)
                archive.append(item)
    sendMail(newItems)
    with open('/home/ec2-user/scraping/craigslist_sample/archive.json', 'w') as archiveFile:
        json.dump(archive, archiveFile)
