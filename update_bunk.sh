#!/bin/bash
rm bunkbed.json

scrapy crawl BunkBedSpider -o bunkbed.json

