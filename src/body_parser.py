from bs4 import BeautifulSoup as Bs
from google.protobuf.text_format import MessageToString


result = any
def parse_html(html_text):
    parsed = Bs(html_text, "lxml")
    result = parsed.body.text
    return result

def parse_gcrp(gcrp_text):
    parsed = MessageToString(gcrp_text)
    result = parsed
    return result
