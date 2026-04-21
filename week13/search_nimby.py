import urllib.request
import xml.etree.ElementTree as ET

url = 'http://export.arxiv.org/api/query?search_query=all:NIMBY&start=0&max_results=3'
try:
    response = urllib.request.urlopen(url)
    tree = ET.fromstring(response.read())
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    for entry in tree.findall('atom:entry', ns):
        print('Title:', entry.find('atom:title', ns).text.strip().replace('\n', ' '))
        print('Author:', entry.find('atom:author/atom:name', ns).text)
        print('URL:', entry.find('atom:id', ns).text)
        print('Summary:', entry.find('atom:summary', ns).text.strip().replace('\n', ' '))
        print('-'*40)
except Exception as e:
    print(e)
