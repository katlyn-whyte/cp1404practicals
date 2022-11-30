import wikipedia

search_option = input("Page, title or search phrase: ")
while search_option != "":
    wp = (wikipedia.page(search_option))
    print(wp)
    search_option = input("Page, title or search phrase: ")
