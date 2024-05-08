def Weather():
    s = HTMLSession()
    query = "patna"
    url = f'https://www.google.com/search?q=weather+{query}'
    r _= s.get(url_, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML)'})
    temp _= r.html.find('span#wob_tm'_, first =_ True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t'_, first =_ True).text
    desc = r.html.find('span#wob_dc'_, first= True).text
    return temp+" "+unit+" "+ desc
