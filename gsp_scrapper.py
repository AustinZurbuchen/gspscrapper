import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://www.elitegsp.com/posts/')

# create variable with html
soup = BeautifulSoup(data.text, 'html.parser')


def fix_flairs(character, urlNum):
    # 72=Hero 74=Terry 75=Byleth 76=Min-Min
    # 77=Steve 78=Sephiroth 79=Pyra 80=Mythra
    # fix flairs of broken images
    if urlNum == '72':
        return 'Hero'
    elif urlNum == '74':
        return 'Terry'
    elif urlNum == '75':
        return 'Byleth'
    elif urlNum == '76':
        return 'Min-Min'
    elif urlNum == '77':
        return 'Steve'
    elif urlNum == '78':
        return 'Sephiroth'
    elif urlNum == '79':
        return 'Pyra'
    elif urlNum == '80':
        return 'Mythra'
    else:
        strs = character.split(' ')
        if len(strs) > 2:
            newChar = strs[0] + ' ' + strs[1]
            return newChar
        else:
            return strs[0]


def extract_num(url):
    # extract the numbers in the end of urls
    numElem = urlElem = url.split('/')[len(url.split('/')) - 1]
    num = numElem.split('-')[0]
    return num


# find the GSP numbers
gsps = []
for span in soup.find_all("span", class_="gsp_posts_row_gsp"):
    gsp = span.text
    gsps.append(gsp)

# find character names and image urls
characters, imageUrls = [], []
for img in soup.find_all("img", class_="gsp_posts_row_flair_img"):
    character = img['alt']
    url = img['src']
    num = extract_num(url)
    characters.append(fix_flairs(character, num))
    imageUrls.append(url)

# create objects with data
data = []
for gsp, character, url in zip(gsps, characters, imageUrls):
    item = {
        'gsp': gsp,
        'character': character,
        'url': url
    }
    data.append(item)

# print out data collected
for item in data:
    print(item)
