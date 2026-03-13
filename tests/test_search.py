from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):

#Given the DuckDuckGo home page is displayed
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "Elvis"
# When the user searches for "David Bowie"
    search_page.load()

# Then the search result title contains "David Bowie"
    search_page.search(PHRASE)

# and the search query is "David Bowie"
    assert PHRASE in result_page.title()

#and the search result links pertain to "David Bowie"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    
    raise Exception("Incomplete test")