from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):

#Given the DuckDuckGo home page is displayed
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "Elvis"
# When the user searches for "Elvis"
    search_page.load()

# Then the search result title contains "Elvis"
    search_page.search(PHRASE)

#Then the search result query is "Elvis"
    assert PHRASE == result_page.search_input_value()

#and the search result links pertain to "Elvis"

    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

# and the search result title contains is "Elvis"
    assert PHRASE in result_page.title()