import wikipediaapi as wiki

wiki = wiki.Wikipedia('en', extract_format=wiki.ExtractFormat.WIKI)


def get_summary(keyword):
    wk = wiki.page(keyword)
    return wk.summary

