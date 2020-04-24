from selenium.webdriver.common.keys import Keys


def test_check_title(py):
    py.visit('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')
    py.should().contain_title("pylenium")
    py.should().contain_title("selenium")


def test_assert_check_title(py):
    py.visit('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')
    assert py.should().contain_title("pylenium")
    assert py.should().contain_title("selenium")


def test_check_URl(py):
    py.visit("https://elsnoman.gitbook.io/pylenium/pylenium-commands/should")
    py.should().contain_url("https://elsnoman.gitbook.io/pylenium/")


def test_assert_check_URl(py):
    py.visit("https://elsnoman.gitbook.io/pylenium/pylenium-commands/should")
    assert py.should().contain_url("https://elsnoman.gitbook.io/pylenium/")


def test_have_title(py):
    py.visit('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')
    py.should().have_title("pylenium")
    # check in the error the title and get it from there


def test_assert_have_title(py):
    py.visit('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')
    assert py.should().have_title("pylenium")
    # check in the error the title and get it from there


def test_have_URL(py):
    py.visit('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')
    py.should().have_url('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')


def test_have_URL(py):
    py.visit('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')
    assert py.should().have_url('https://elsnoman.gitbook.io/pylenium/pylenium-commands/should')


def test_assert_search_element_hit_enter_using_type(py):
    py.visit('https://google.com')
    py.get('[name="q"]').type('selenium', Keys.ENTER)
    assert 'selenium' in py.title


def test_chain_commands_in_one_line(py):
    py.visit('https://www.selenium.dev/')
    # py.get('[id="banner-conservancy"]').find("Tickets").first().click()
    py.get('ul').find('href').first().click()

def test_assert_check(py):
    py.visit('https://elsnoman.gitbook.io/pylenium/pylenium-commands/commands')
    assert py.find('commands').check()

def test_search_element_hit_using_click(py):
    py.visit('https://www.selenium.dev/')
    py.get('[name="search"]').type("Webdriver")
    py.get('[class="search-icon"]').click()

def test_search_element_using_contains(py):
    py.visit('https://www.selenium.dev/')
    py.screenshot("pylenium_pic_sc.png")
    py.contains('Documentation').click()

def test_search_element_using_get(py):
    py.visit('https://www.selenium.dev/')
    py.screenshot("pylenium_pic_sc.png")
    py.get("[href='/documentation']").click()

def test_take_srcreenshot(py):
    py.visit('https://www.selenium.dev/')
    py.screenshot("pylenium_pic_sc.png")

def test_hover_element(py):
    py.visit('https://the-internet.herokuapp.com/hovers')
    py.get('([class="figure"])[2]').hover()

def test_scroll_element_in_page(py):
    py.visit('https://the-internet.herokuapp.com/infinite_scroll')
    scroll = py.scroll_to(0,4000)
    # py.wait(2000).until('selenium' in py.title)

def test_iframe_enter_data(py):
    py.visit('https://the-internet.herokuapp.com/iframe')
    py.switch_to.frame("mce_0_ifr")
    # py.get('#tinymce').clear().type("Prerna Gaikwad just typed in here.").should().have_text('Prerna')
    # py.get('#tinymce').clear().type("This is demo text").should().have_text('DEMO', True)
    py.get('#tinymce').clear().type('Pratik').should().have_text('Pratik')
    py.get('#tinymce').should().have_value('Pratik')
    py.get('#tinymce').clear().type("Pratik Gaikwad just typed in here.").should().not_have_value('Prerna')
    py.get('#tinymce').clear().type("Prerna Gaikwad just typed in here.").should().not_have_text('Prerna')
    py.get('#tinymce').clear().type("I am a tester").should().not_have_text('Pratik')
