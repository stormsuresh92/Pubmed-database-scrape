from requests_html import HTMLSession

session = HTMLSession()

def get_url(url):
    #url = f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/'
    r = session.get(url)
    full_text_urls = r.html.find('div.full-text-links')
    for pmcurl in full_text_urls:
      pmc_url = pmcurl.find('a.link-item.pmc', first=True).attrs['href']
    return pmc_url


def get_main_pdfs(url_response):
    baseurl = 'https://www.ncbi.nlm.nih.gov'
    r = session.get(url_response)
    pdf_url = r.html.find('div.format-menu ul')
    for pdf in pdf_url:
      try:
          main_pdf = baseurl + pdf.find('ul > li:nth-child(4) > a', first=True).attrs['href']
      except:
          pass
      with open( pmid + '.pdf', 'wb') as f:
          res = session.get(main_pdf)
          f.write(res.content)
    return main_pdf
  
pmid = input('Enter PMID: ')
c = get_url(f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/')
get_main_pdfs(c)
print('finished')

        