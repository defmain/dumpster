#!/usr/bin/python

import urllib

def commit(download, name):
	download = urllib.urlretrieve(download, name)
        return

if __name__ == "__main__":
	raw_url = "Paste URL:  "
	raw_name = "Name the Image on disk: "
	image_url = raw_input(raw_url)
	image_name = raw_input(raw_name)
	commit(image_url, image_name)
