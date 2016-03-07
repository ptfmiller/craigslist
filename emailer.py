import boto.ses

def sendMail(inputList):
    if len(inputList) == 0:
        return
    else:
        mailBody = 'A new post has appeared!\n\n'
        for i in range(len(inputList)):
            item = inputList[i]
            itemString = '{0}. {1}: {2} - {3}\n'.format(i, item['price'], item['title'], item['link'])
            mailBody = mailBody + itemString
        mailBody = mailBody + '\nLove,\nPhil'
        conn = boto.ses.connect_to_region('us-east-1')
        conn.send_email('ptfmiller@gmail.com', 'New craigslist post(s)', mailBody, ['ptfmiller@gmail.com', 'jamieelizabethmiller@gmail.com])
