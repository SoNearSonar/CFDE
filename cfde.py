import re, os, wget
from tkinter import filedialog as fd
from zipfile import ZipFile as zf
from tarfile import TarFile as tf
from py7zr import SevenZipFile as sz

# Credit to https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py for the first regex
regexUrl = re.compile(r'^(?:http|ftp)s?://', re.IGNORECASE)

# Credit to https://www.geeksforgeeks.org/python-program-to-find-files-having-a-particular-extension-using-regex/# for the next regex lines
regexZipFileType = re.compile('\.zip$', re.IGNORECASE)
regex7ZipFileType = re.compile('\.7z$', re.IGNORECASE)
regexTarFileType = re.compile('\.(tgz$)|(tar\.gz$)|(tar\.xz$)', re.IGNORECASE)

print('Enter in the file url here that you want to download: ')
fileUrl = input()

zipFileMatch = re.search(regexZipFileType, fileUrl)
tarFileMatch = re.search(regexTarFileType, fileUrl)
sevenZipFileMatch = re.search(regex7ZipFileType, fileUrl)
urlMatch = re.search(regexUrl, fileUrl)

if (not zipFileMatch and not tarFileMatch and not sevenZipFileMatch) or not urlMatch:
    print('\nWhat was entered is not a valid url')
else:
    try:
        print('\nEnter in the directory you want the file to be downloaded to (a window will pop up)')
        directoryName = fd.askdirectory()
        
        if not os.path.isdir(directoryName):
            print('\nWhat was entered is not a valid directory')
            quit()
        
        fileName = wget.download(fileUrl, directoryName)

        if zipFileMatch:
            zf(fileName, 'r').extractall(directoryName)
        elif tarFileMatch:
            with tf.open(fileName) as t:
                t.extractall(directoryName)
        elif sevenZipFileMatch:
            sz(fileName, mode = 'r').extractall(directoryName)
    except Exception as ex:
        print('An error occurred when using this program: ' + ex)
quit()