__author__ = 'Tom Stanley'
import wikipedia


def main():
    user_search = input("Enter a search:").strip()
    while user_search != "":
        try:
            wiki_page = wikipedia.page(user_search)
            print("{}\n{}\n{}".format(str(wiki_page.title), str(wiki_page.summary), str(wiki_page.url)))
            user_search = input("Enter a search:").strip()
        except wikipedia.WikipediaException:
            print("It looks like wikipedia can't find what you are looking for, please search again")
        user_search = input("Enter a search:").strip()


if __name__ == '__main__':
    main()