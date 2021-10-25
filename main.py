import pytest
import requests

url_ddg = "https://api.duckduckgo.com"

def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

    rsp_data = resp.json()

    assert "DuckDuckGo" in rsp_data["Heading"]

resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")

rsp_data = resp.json()

related_topics = rsp_data["RelatedTopics"]

text_list = []
for topic in related_topics:
    text_list.append(topic['Text'])

text_string = str(text_list)

def test_washington():
    assert "Washington" in text_string

def test_adams():
    assert "Adams" in text_string

def test_jefferson():
    assert "Jefferson" in text_string

def test_madison():
    assert "Madison" in text_string

def test_monroe():
    assert "Monroe" in text_string

def test_jackson():
    assert "Jackson" in text_string

def test_van_buren():
    assert "Van Buren" in text_string

def test_harrison():
    assert "Harrison" in text_string

def test_tyler():
    assert "Tyler" in text_string

def test_polk():
    assert "Polk" in text_string

def test_taylor():
    assert "Taylor" in text_string

def test_fillmore():
    assert "Fillmore" in text_string

def test_pierce():
    assert "Pierce" in text_string

def test_buchanan():
    assert "Buchanan" in text_string

def test_lincoln():
    assert "Lincoln" in text_string

def test_johnson():
    assert "Johnson" in text_string

def test_grant():
    assert "Grant" in text_string

def test_hayes():
    assert "Hayes" in text_string

def test_garfield():
    assert "Garfield" in text_string

def test_arthur():
    assert "Arthur" in text_string

def test_cleveland():
    assert "Cleveland" in text_string

def test_mckinley():
    assert "McKinley" in text_string

def test_roosevelt():
    assert "Roosevelt" in text_string

def test_taft():
    assert "Taft" in text_string

def test_wilson():
    assert "Wilson" in text_string

def test_harding():
    assert "Harding" in text_string

def test_coolidge():
    assert "Coolidge" in text_string

def test_hoover():
    assert "Hoover" in text_string

def test_truman():
    assert "Truman" in text_string

def test_eisenhower():
    assert "Eisenhower" in text_string

def test_kennedy():
    assert "Kennedy" in text_string

def test_nixon():
    assert "Nixon" in text_string

def test_ford():
    assert "Ford" in text_string

def test_carter():
    assert "Carter" in text_string

def test_reagan():
    assert "Reagan" in text_string

def test_bush():
    assert "Bush" in text_string

def test_clinton():
    assert "Clinton" in text_string

def test_obama():
    assert "Obama" in text_string

def test_trump():
    assert "Trump" in text_string

def test_biden():
    assert "Biden" in text_string