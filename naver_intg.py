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

version=(f'1.0.1')

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
        if lingua in KO_KR:
            df.info()
            print(f'''
naver_{keyword}_page_{page}_{creation_date}_{sort}.csv가 저장되었습니다.
네이버 {keyword} 키워드의 최근 {page} 페이지 데이터 수집이 완료되었습니다.

제작자: EastPersiaLtd
''')
        elif lingua in EN_GB:
            df.info()
            print(f'''
Saving naver_{keyword}_page_{page}_{creation_date}_{sort}.csv has completed.
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

class desc3:
    def first(self):
        if lingua in KO_KR:
            print(f'''
NLP-K WordCloud 한국어 스크립트 {version}입니다.
NLP-K WordCloud용 스프레드시트 셀렉터를 실행합니다.
''')
        elif lingua in EN_GB:
            print(f'''
NLP-K WordCloud script {version} for English.
Execute spreadsheet selector for NLP-K WordCloud...
''')

    def third(self):
        if lingua in KO_KR:
            print(df.columns,'''
파일의 칼럼 리스트입니다.
''')
        elif lingua in EN_GB:
            print(df.columns,'''
Here is a coloumn list of the file.
''')

    def fourth(self):
        if lingua in KO_KR:
            print(f'''
준비가 완료되었습니다.
''')
        elif lingua in EN_GB:
            print(f'''
Preperation has completed.
''')


    def fifth(self):
        if lingua in KO_KR:
            print(f'''
NLP-K WordCloud 마법사 {version}입니다.

사용할 수 있는 컬러맵 종류는 아래와 같습니다.

계절
spring/summer/autumn/winter

그레디언트
viridis/plasma/inferno/magma/cividis
Wistia/cool/hot/afmhot/coolwarm
bwr/seismic/Spectral/twilight/twilight_shifted
ocean/gist_earth/gist_stern/terrain
CMRmap/cubehelix/gnuplot/gnuplot2

스펙트럼
hsv/brg/gist_rainbow/rainbow/jet
turbo/nipy_spectral/gist_ncar
''')
        elif lingua in EN_GB:
            print(f'''
NLP-K WordCloud Wizard {version}.

Here is the list of colourmaps as it follows.

-Season
spring/summer/autumn/winter

-Gradient
viridis/plasma/inferno/magma/cividis
Wistia/cool/hot/afmhot/coolwarm
bwr/seismic/Spectral/twilight/twilight_shifted
ocean/gist_earth/gist_stern/terrain
CMRmap/cubehelix/gnuplot/gnuplot2

-Spectrum
hsv/brg/gist_rainbow/rainbow/jet
turbo/nipy_spectral/gist_ncar
''')

    def sixth_custom(self):
        if lingua in KO_KR:
            print(f'''
지정된 경로의 폰트를 사용합니다.
''')
        elif lingua in EN_GB:
            print(f'''
Use custom font on the path.
''')

    def sixth_noncustom(self):
        if lingua in KO_KR:
            print(f'''
커스텀 폰트를 사용하지 않습니다. 경고: 차트가 깨질 수 있습니다.
''')
        elif lingua in EN_GB:
            print(f'''
Not using custom font. WARNING: CHART WILL NOT DISPLAY CLEARLY.
''')

    def finished(self):
        if lingua in KO_KR:
            print(f'''
nlp_k_wordcloud_naver_{keyword}_page_{page}_{creation_date}_{sort}.png가 저장되었습니다.
NLP-K WordCloud 생성이 끝났습니다.

제작자: EastPersiaLtd
''')
        elif lingua in EN_GB:
            print(f'''
Saving nlp_k_wordcloud_naver_{keyword}_page_{page}_{creation_date}_{sort}.png has completed.
Generating a NLP-K WordCloud chart has finished.

Credit: EastPersiaLtd
''')

    def terminate(self):
        if lingua in KO_KR:
            print(f'''
스크립트를 종료합니다.
''')
        elif lingua in EN_GB:
            print(f'''
Script has terminated.
''')
#####

#####Limitation on search page range
def limits(i):
    if i>400:
        i:int=i-(i-400)
        return i
    elif i<=400:
        i:int=i
        return i

#####
desc=description()
finish=finish()
desc3=desc3()

#####Select Channel
lingua=str(input(f'''
사용할 언어를 고르세요/Select the language you want. KO-KR / EN-GB: 
'''))
#####

#####Select Keyword, Page, and Sort
desc.first()
#####
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

    auto=int(input(f'''
Wordcloud 자동 생성을 활성화하시겠습니까?(KO-KR 폰트 필요) 0=아니오 / 1=네: 
'''))

elif lingua in EN_GB:
    keyword=str(input('''
Please input the Keyword to search: 
'''))
    page=int(input('''
Choose the range of pages you want to scrap; Collect the latest n pages -> n: 
'''))
#####
    pre_page=page
    page=limits(page)
    finish.limitation()
#####
    sort=int(input('''
Choose the sorting order;

0=By relevance
1=By latest order
2=By eldest order

Select: 
'''))

    auto=int(input(f'''
Activate automatic Wordcloud generation?(KO-KR font required) 0=No / 1=Yes: 
'''))

#####
desc.second()
#####
creation_date=str(time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time())))
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

##########NLP-K
if auto==1:
    !pip install konlpy matplotlib wordcloud

    #####Import Packages
    from collections import Counter
    from konlpy.tag import Okt
    import matplotlib.pyplot as plt
    import os
    from wordcloud import WordCloud, STOPWORDS

    #####Wordcloud
    desc3.first()
    #####

    desc3.third()
    #####

    if lingua in KO_KR:
        column1=str(input('''
Wordcloud로 만들 칼럼을 지정해주세요(따옴표 생략): 
'''))
    elif lingua in EN_GB:
        column1=str(input('''
Select the column for generating a Wordcloud chart(You may ignore the inverted commas): 
'''))
    #####

    datas=df[column1].to_list()
    #####

    desc3.fourth()
    #####


    #####Customisation
    desc3.fifth()
    #####
    #number=int(input('이 글자 수 미만의 단어는 포함되지 않습니다(정수로 입력): '))
    #title=str(input('차트의 타이틀을 입력해주세요: '))

#####
    if lingua in KO_KR:
        cmap=str(input('''
차트에 사용될 컬러맵을 골라주세요: 
'''))
        font_custom=str(input('''
차트에 사용하고 싶은 폰트의 위치를 입력하세요: 
'''))
    elif lingua in EN_GB:
        cmap=str(input('''
Select a colourmap for the chart: 
'''))
        font_custom=str(input('''
Select the path of custom font for the chart: 
'''))
#####

    font_check=bool(font_custom)

    #####Clause 2-1: Generate the chart w/ custom font
    if font_check==True:
        desc3.sixth_custom()
        #####
        text="".join(map(str, datas))
        okt=Okt()
        nouns=okt.nouns(text)
        words=[n for n in nouns if len(n)>1]
        counting=Counter(words)
        #####
        wc=WordCloud(
            font_path=font_custom,
            width=1600,
            height=900,
            scale=2.0,
            max_font_size=500,
            prefer_horizontal=True,
            colormap=cmap,
            background_color='mintcream',
        )

    #####Clause 2-2: Generate the chart w/o custom font
    elif font_check==False:
        desc3.sixth_noncustom()
        #####
        text="".join(map(str, datas))
        okt=Okt()
        nouns=okt.nouns(text)
        words=[n for n in nouns if len(n)>1]
        counting=Counter(words)
        #####
        wc=WordCloud(
            width=1600,
            height=900,
            scale=2.0,
            max_font_size=500,
            prefer_horizontal=True,
            colormap=cmap,
            background_color='mintcream',
        )

    #####Creation
    gen=wc.generate_from_frequencies(counting)

    #####Showing the chart
    plt.figure(figsize=(16, 9))
    plt.imshow(gen)
    #plt.title(title, fontsize=30)
    plt.axis('off')

    #####Save the chart
    plt.savefig(f'nlp_k_wordcloud_naver_{keyword}_page_{page}_{creation_date}_{sort}.png')

    #####Show the chart
    plt.show()

    #####Finished 2
    desc3.finished()

else:
    desc3.terminate()

#####
#sync=int(input('구글 드라이브와 연동하시겠습니까? 0: 아니오 / 1: 예'))
#if sync==1:
#    print('구글 드라이브와 연동합니다.')
#    from google.colab import drive
#    drive.mount('/content/drive')
#    print('구글 드라이브와 연동했습니다.')
#elif sync==0:
#    print('구글 드라이브와 연동하지 않습니다.')
#else:
#    print('잘못된 수치입니다. 다시 시도해주세요.')
#    sys.exit()
#####