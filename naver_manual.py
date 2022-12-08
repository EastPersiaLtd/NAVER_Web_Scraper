#@title TEST A

!pip install bs4 pandas

##########Import Packages
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

#####Create the lists
post_title=[]
post_desc=[]
post_url=[]

KO_KR=['KO_KR', 'ko_kr', 'KO-KR', 'KO-kr', 'Ko-Kr', 'Ko-kr', 'ko-Kr', 'ko-KR', 'ko-kr', 'KR', 'kr', 'Korea', 'Korean', 'korea', 'korean', 'Hangeul', 'hanguel',
'한국어', '한글', '한국말', 'gksrnrdj', 'gksrmf', 'gksrnrakf']
EN_GB=['EN_GB', 'en_gb', 'EN-GB', 'EN-gb', 'En-Gb', 'En-gb', 'en-Gb', 'en-GB', 'en-gb', 'EN-US', 'en-us', 'English', 'english', 'ENG', 'eng', 'not american']

version=(f'1.0.0')

class description:
    def first(self):
        if lingua in KO_KR:
            print(f'''
한국어를 고르셨습니다.

네이버 웹 스크래퍼 {version}입니다.
''')

        elif lingua in EN_GB:
            print(f'''
You chosen english.

NAVER Web Scraper {version}.
''')

    def second(self):
        if lingua in KO_KR:
            if sort==0:
                print(f'''
{keyword}를(을) {page} 페이지만큼 검색한 뒤 관련도순으로 정렬합니다.
''')

            elif sort==1:
                print(f'''
{keyword}를(을) {page} 페이지만큼 검색한 뒤 최신순으로 정렬합니다.
''')

            elif sort==2:
                print(f'''
{keyword}를(을) {page} 페이지만큼 검색한 뒤 오래된순으로 정렬합니다.
''')
#####
        elif lingua in EN_GB:
            if sort==0:
                print(f'''
Searching {keyword} for {page} page(s) and sort them by relevance...
''')

            elif sort==1:
                print(f'''
Searching {keyword} for {page} page(s) and sort them by latest order...
''')

            elif sort==2:
                print(f'''
Searching {keyword} for {page} page(s) and sort them by eldest order...
''')

class finish:
    def finish_phrase(self):
        df.info()
        if lingua in KO_KR:
            print(f'''
naver_{keyword}_page_{page}_{creation_date}.csv가 저장되었습니다.
네이버 {keyword} 키워드의 최근 {page} 페이지 데이터 수집이 완료되었습니다.

제작자: EastPersiaLtd
''')

        elif lingua in EN_GB:
            print(f'''
Saving naver_{keyword}_page_{page}_{creation_date}.csv has completed.
Data collecting of NAVER {keyword} keyword's latest {page} page(s) has(have) finished.

Credit: EastPersiaLtd
''')

    def limitation(self):
        if lingua in KO_KR:
            print(f'''
최대 400 페이지 까지만 검색이 가능합니다. {pre_page} -> 400
''')
        elif lingua in EN_GB:
            print(f'''
You can not search for greater than 400 pages. {pre_page} -> 400
''')
#####

#####
desc=description()
finish=finish()

#####Select Channel
lingua=str(input(f'''
사용할 언어를 고르세요/Select the language you want. KO-KR / EN-GB: 
'''))
#####

#####Select Keyword, Page, and Sort
desc.first()
if lingua in KO_KR:
    keyword=str(input('''
키워드를 입력해주세요: 
'''))
    page=int(input('''
페이지 수를 입력해주세요: 
'''))
    pre_page=page
    page=limits(page)
    finish.limitation()

    sort=int(input('''
정렬 순서를 선택해주세요.

0=관련도순
1=최신순
2=오래된순

선택: 
'''))

elif lingua in EN_GB:
    keyword=str(input('''
Please input the Keyword to search: 
'''))
    page=int(input('''
Choose the range of pages you want to scrap; Collect the latest n pages -> n: 
'''))
    pre_page=page
    page=limits(page)
    finish.limitation()

    sort=int(input('''
Choose the sorting order;

0=By relevance
1=By latest order
2=By eldest order

Select: 
'''))

#####
desc.second()
#####
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))

#####Limitation on search page range
def limits(i):
    if i>400:
        i:int=i-(i-400)
        return i

    elif i<=400:
        i:int=i
        return i

page=limits(page)
#####

#####Loops
if page==1:
    n=1
    pages=list(range(1, n+10, 10))
elif page>1:
    n=(((page-1)*10)+1)
    pages=list(range(1, n+10, 10))
#####
for i in range(len(pages)):
    pali=pages[i]
    url=f'https://search.naver.com/search.naver?where=news&query={keyword}&sort={sort}&start={pali}'
    #####
    response=requests.get(url)
    soup=BeautifulSoup(response.text, 'html.parser')
    #####
    title=soup.select('a.news_tit')
    desc=soup.select('a.api_txt_lines.dsc_txt_wrap')
    articles=soup.select('div.group_news > ul.list_news > li div.news_area > a')
    #####
    for j in title:
        post_title.append(j.get_text())
    for k in desc:
        post_desc.append(k.get_text())
    for l in articles:
        post_url.append(l.attrs['href'])

#####List JOIN
post_list = list(zip(post_title, post_desc, post_url))
col=['post_title', 'post_desc', 'post_url']

#####DataFrame conversion
df=pd.DataFrame(post_list, columns=col)
#df=df.replace(r'\n', '', regex=True)
df.to_csv(
    f'naver_{keyword}_page_{page}_{creation_date}_{sort}.csv',
    index=False,
    encoding="utf-8-sig"
)

#####Finished
finish.finish_phrase()