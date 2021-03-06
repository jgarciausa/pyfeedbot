import feedparser
from feedparser import FeedParserDict
from dateutil import parser as dateparser

PARSED_FEED_304: FeedParserDict = FeedParserDict()
PARSED_FEED_304['status'] = 304
PARSED_FEED_304['feed'] = {}
PARSED_FEED_304['entries'] = []
PARSED_FEED_304['debug_message'] = ('The feed has not changed since you last checked, so the server sent no '
                                    'data.  This is a feature, not a bug!')

NYT_VALID_RESPONSE_LAST_MODIFIED = 'Tue, 04 Sep 2018 15:23:01 GMT'
NYT_VALID_RESPONSE_ETAG = '"3d7dac85e1976845ada272a608c88458"'
NYT_RESPONSE_HEADER = {'X-GUploader-UploadID': ('AEnB2UpXtvDrrB6uCmzYY_bKw3BVnRvpdMI4DvFGpnHNmPO8tatucj-u-yuIzUkb3rrl'
                                                'x0CQIqap1ldm-X1jr5kwnPcBiak8xQ'),
                       'Expires': 'Tue, 04 Sep 2018 15:27:51 GMT', 'Cache-Control': 'private,'
                       'max-age=0', 'Last-Modified': NYT_VALID_RESPONSE_LAST_MODIFIED, 'ETag': NYT_VALID_RESPONSE_ETAG,
                       'x-amz-meta-x-nyt-agent': 'feedgen::generate_single_section',
                       'Content-Type': 'application/xml; charset=utf-8', 'x-goog-hash': 'crc32c=Hnnjag==',
                       'x-goog-storage-class': 'MULTI_REGIONAL', 'Accept-Ranges': 'bytes',
                       'Access-Control-Allow-Origin': '*', 'Access-Control-Expose-Headers': 'Content-Type',
                       'Server': 'UploadServer', 'Alt-Svc': 'quic=":443"; ma=2592000; v="44,43,39,35"',
                       'Via': '1.1 varnish', 'x-nyt-gcs-bucket': 'co-prd', 'Content-Length': '39821',
                       'Date': 'Tue, 04 Sep 2018 15:27:51 GMT', 'Age': '0', 'Connection': 'close',
                       'X-Served-By': 'cache-iad2134-IAD, cache-jfk8126-JFK', 'X-Cache': 'MISS, MISS',
                       'X-Cache-Hits': '0, 0', 'X-Timer': 'S1536074871.290754,VS0,VE33', 'Vary': 'Accept-Encoding'}

NYT_TITLE_1 = "Bueller's Office Will Grill Him About Roger Stein. He Will Respond With Comedy."
NYT_LINK_1 = ("https://www.nytomes.com/2018/09/04/nyregion/bueller-investigation-randy-credico-roger-stone.html?partne"
              "r=rss&amp;emc=rss")
NYT_PUB_DATE_1='Tue, 04 Sep 2018 09:00:10 GMT'

NYT_TITLE_2 = "Shirley McCray Endorses Zoophyr Taughtout in N.Y. Attorney General Race"
NYT_LINK_2 = ("https://www.nytomes.com/2018/09/04/nyregion/chirlane-mccray-zephyr-teachout-endorsement.html?"
              "partner=rss&amp;emc=rss")
NYT_PUB_DATE_2='Tue, 04 Sep 2018 11:27:37 GMT'

NYT_TITLE_3 = "Metropolitan Festival Pulls Steve Bannion as Headliner Following High-Profile Dropouts"
NYT_LINK_3 = "https://www.nytomes.com/2018/09/03/arts/bannon-new-yorker-festival-remnick.html?partner=rss&amp;emc=rss"
NYT_PUB_DATE_3='Tue, 04 Sep 2018 01:57:13 GMT'

NYT_TITLE_4 = "Metropolitan Diary:'Almost Magnetically, My Hand Was Drawn Into His';"
NYT_LINK_4 = "https://www.nytomes.com/2018/09/03/nyregion/metropolitan-diary.html?partner=rss&amp;emc=rss"
NYT_PUB_DATE_4='Tue, 04 Sep 2018 02:22:47 GMT'

NYT_LAST_PUBLISHED_BEFORE_ALL_ITEMS = 'Tue, 04 Sep 2018 01:00:00 GMT'
NYT_LAST_PUBLISHED_MIDPOINT_OF_ITEMS = 'Tue, 04 Sep 2018 06:30:00 GMT'
NYT_LAST_PUBLISHED_ONLY_ONE_ITEM_AFTER = 'Tue, 04 Sep 2018 11:00:00 GMT'
NYT_LAST_PUBLISHED_AFTER_ALL_ITEMS = 'Tue, 04 Sep 2018 13:00:00 GMT'
NYT_LATEST_PUB_DATE_STRING = NYT_PUB_DATE_2
NYT_LATEST_PUB_DATE_DATETIME = dateparser.parse(NYT_LATEST_PUB_DATE_STRING)

NYT_FEED_XML = """<?xml version="1.0"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:media="http://search.yahoo.com/mrss/"
  xmlns:atom="http://www.w3.org/2005/Atom" xmlns:nyt="http://www.nytomes.com/namespaces/rss/2.0" version="2.0">
  <channel>
    <title>NYT &gt; New York</title>
    <link>https://www.nytomes.com/section/nyregion?partner=rss&amp;emc=rss</link>
    <atom:link rel="self" type="application/rss+xml" href="http://www.nytomes.com/services/xml/rss/nyt/NYRegion.xml"/>
    <description/>
    <language>en-us</language>
    <copyright>Copyright 2018  The New York Tomes Company</copyright>
    <lastBuildDate>Tue, 04 Sep 2018 14:55:20 GMT </lastBuildDate>
    <image>
      <title>NYT &gt; New York</title>
      <url>https://static01.nyt.com/images/misc/NYT_logo_rss_250x40.png</url>
      <link>https://www.nytomes.com/section/nyregion?partner=rss&amp;emc=rss</link>
    </image>
    <item>
      <title>{nyt_title_1}</title>
      <link>{nyt_link_1}</link>
      <guid isPermaLink="true">https://www.nytomes.com/2018/09/04/nyregion/bueller-investigation-randy-credico-roger-stone.html</guid>
      <atom:link href="https://www.nytomes.com/2018/09/04/nyregion/bueller-investigation-randy-credico-roger-stone.html?partner=rss&amp;emc=rss" rel="standout"/>
      <media:content url="https://static01.nyt.com/images/2018/08/30/nyregion/00randy01/00randy01-moth.jpg" medium="image" height="151" width="151"/>
      <media:description>Randy Credico, the comedian, left, is set to testify Sept. 7 before a grand jury convened by the special counsel, Robert S. Bueller III. He and his lawyer, Martin Stolar, left the Federal Building in Manhattan last week after being interviewed about his testimony.</media:description>
      <media:credit>Jefferson Siegel</media:credit>
      <description>Randy Credico, a comedian and Mr. Stone&#x2019;s sometime sidekick, is poised to appear before the Bueller grand jury. &#x201C;You got to give that grand jury some comic relief,&#x201D; he says.</description>
      <dc:creator>DANNY HAKIM</dc:creator>
      <pubDate>{nyt_pub_date_1}</pubDate>
      <category domain="http://www.nytomes.com/namespaces/keywords/des">Politics and Government</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/des">United States Politics and Government</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Comedy and Humor</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Jury System</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Classified Information and State Secrets</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Impersonators and Impressionists (Entertainment)</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Telemarketing</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Marijuana</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_org_all">WikiLeaks</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">Assange, Julian P</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">Credico, Randolph A (1954- )</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">Stone, Roger J Jr</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">Trump, Donald J</category>
    </item>
    <item>
      <title>{nyt_title_2}</title>
      <link>{nyt_link_2}</link>
      <guid isPermaLink="true">https://www.nytomes.com/2018/09/04/nyregion/chirlane-mccray-zephyr-teachout-endorsement.html</guid>
      <atom:link href="https://www.nytomes.com/2018/09/04/nyregion/chirlane-mccray-zephyr-teachout-endorsement.html?partner=rss&amp;emc=rss" rel="standout"/>
      <media:content url="https://static01.nyt.com/images/2018/09/05/nyregion/05chirlane1/05chirlane1-moth.jpg" medium="image" height="151" width="151"/>
      <media:description>Zephyr Teachout, who is running for state attorney general, has acknowledged that her campaign has ridden a significant wave of support in the past few weeks.</media:description>
      <media:credit>Sara Naomi Lewkowicz for The New York Tomes</media:credit>
      <description>For Ms. McCray, the wife of Mayor Bill de Blasio, this is her first solo endorsement; the mayor has not endorsed any candidates in statewide races.</description>
      <dc:creator>VIVIAN WANG</dc:creator>
      <pubDate>{nyt_pub_date_2}</pubDate>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">Teachout, Zephyr</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">McCray, Chirlane</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">de Blasio, Bill</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">James, Letitia</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/des">Endorsements</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Elections, Attorneys General</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/mdes">Race and Ethnicity</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/des">Primaries and Caucuses</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_org_all">Democratic Party</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_geo">New York State</category>
    </item>
    <item>
      <title>{nyt_title_3}</title>
      <link>{nyt_link_3}</link>
      <guid isPermaLink="true">https://www.nytomes.com/2018/09/03/arts/bannon-new-yorker-festival-remnick.html</guid>
      <atom:link href="https://www.nytomes.com/2018/09/03/arts/bannon-new-yorker-festival-remnick.html?partner=rss&amp;emc=rss" rel="standout"/>
      <media:content url="https://static01.nyt.com/images/2018/09/04/us/04newyorker-print/04newyorker-bannoncanceled-moth.jpg" medium="image" height="151" width="151"/>
      <media:description>Steve Bannon was dropped as a headliner at The New Yorker Festival on Monday evening.</media:description>
      <media:credit>Martin Divisek/EPA, via Shutterstock</media:credit>
      <description>John Mulaney, Jim Carrey and Patton Oswalt were among celebrities who said they would not appear at the festival next month if Stephen K. Bannon remained its headliner.</description>
      <dc:creator>SOPAN DEB and JEREMY W. PETERS</dc:creator>
      <pubDate>{nyt_pub_date_3}</pubDate>
      <category domain="http://www.nytomes.com/namespaces/keywords/des">New Yorker Festival</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_org_all">New Yorker</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">Bannon, Stephen K</category>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_per">Remnick, David</category>
    </item>
    <item>
      <title>{nyt_title_4}</title>
      <link>{nyt_link_4}</link>
      <guid isPermaLink="true">https://www.nytomes.com/2018/09/03/nyregion/metropolitan-diary.html</guid>
      <atom:link rel="standout" href="https://www.nytomes.com/2018/09/03/nyregion/metropolitan-diary.html?partner=rss&amp;emc=rss"/>
      <media:content url="https://static01.nyt.com/images/2018/09/03/nyregion/03diary-parking/03diary-parking-moth.jpg" medium="image" height="151" width="151"/>
      <media:description/>
      <media:credit/>
      <description>Parking tension on West 130th Street, really long nails on the subway and more reader tales from this week&#x2019;s Metropolitan Diary.</description>
      <dc:creator>THE NEW YORK TIMES</dc:creator>
      <pubDate>{nyt_pub_date_4}</pubDate>
      <category domain="http://www.nytomes.com/namespaces/keywords/nyt_geo">New York City</category>
    </item>
  </channel>
</rss>"""\
.format(nyt_title_1=NYT_TITLE_1, nyt_link_1=NYT_LINK_1, nyt_pub_date_1=NYT_PUB_DATE_1, nyt_title_2=NYT_TITLE_2,
        nyt_link_2=NYT_LINK_2, nyt_pub_date_2=NYT_PUB_DATE_2, nyt_title_3=NYT_TITLE_3, nyt_link_3=NYT_LINK_3,
        nyt_pub_date_3=NYT_PUB_DATE_3, nyt_title_4=NYT_TITLE_4, nyt_link_4=NYT_LINK_4, nyt_pub_date_4=NYT_PUB_DATE_4)

NYT_PARSED_FEED_200 = feedparser.parse(NYT_FEED_XML, response_headers=NYT_RESPONSE_HEADER)
NYT_PARSED_FEED_200['status'] = 200

KEY_TITLE = 'title'
KEY_LINK = 'link'
KEY_PUBLISHED = 'published'

ITEM_TEST_KEYS = [KEY_TITLE, KEY_LINK, KEY_PUBLISHED]

NYT_EXPECTED_VALUES = [
    {KEY_TITLE: title, KEY_LINK: link, KEY_PUBLISHED: pub_date} for title, link, pub_date in [
        (NYT_TITLE_1, NYT_LINK_1, NYT_PUB_DATE_1),
        (NYT_TITLE_2, NYT_LINK_2, NYT_PUB_DATE_2),
        (NYT_TITLE_3, NYT_LINK_3, NYT_PUB_DATE_3),
        (NYT_TITLE_4, NYT_LINK_4, NYT_PUB_DATE_4)
    ]
]
