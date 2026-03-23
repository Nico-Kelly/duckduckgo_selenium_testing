import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

    #read the file

    with open('config.json') as config_file:
        config = json.load(config_file)

    #assert values are acceptable

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    #return the config so it can be used

    return config


@pytest.fixture
def browser(config):

    #initialize the ChromeDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()

    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    
    else:
        raise Exception(f'Browser "{config["browser"]}" is not suported')


    #Make its calls wait up to 10 seconds for elements to appear
    #b.implicitly_wait(config['implicit_wait']) deprecated this in order to use explicit wait instead.

    #Return the WebDriver instance for the setup
    yield b

    #Quit the WebDriver instance for the cleanup
    b.quit()

