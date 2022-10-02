def filterBible(scripture, book, chapter):

    match_item = book + chapter
    result = [item for item in scripture if match_item in item[0:5]]
    return result


scripture = ["01001001",
             "01001002",
             "01002001",
             "01002002",
             "01002003",
             "02001001",
             "02001002",
             "02001003",
             "66022021"]
book = "01"
chapter = "001"


print(filterBible(scripture,
                  book,
                  chapter))