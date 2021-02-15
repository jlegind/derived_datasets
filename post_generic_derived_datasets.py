import requests
import datetime
import json


def derived_dataset(sourceUrl, title, login, password, api="http://api.gbif-uat.org/v1/derivedDataset"):
    '''
    For putting up custom downloads and minting a DOI
    '''
    headers = {'Content-Type': 'application/json'}
    now = datetime.datetime.now()
    xson = {
              "sourceUrl": sourceUrl,
              "title": title
            }

    derivative = requests.post(api ,
                                   data=json.dumps(xson),
                                   auth=(login, password),
                                   headers = headers

                                   )

    if derivative.ok:
        print("DOI added")
    else:
        print("DOI NOT added")
    return derivative
#
relateddatasets = {"6197c830-d9c7-11de-b793-b8a03c50a862": 1,
                   "9668b676-f762-11e1-a439-00145eb45e9a": 26,
                   "7b7bb606-f762-11e1-a439-00145eb45e9a": 1,
                   "50c9509d-22c7-4a22-a47d-8c48425ef4a7": 222}

res = derived_dataset('https://ipt.gbif.org/archive.do?r=jan_test&v=1.5', 'Grapsidae of Spain', 'jlegind', 'mussimus')

print(res.content)
