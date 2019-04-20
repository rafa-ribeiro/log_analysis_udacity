from log_db import initialize_views, top_three_articles, top_authors_most_popuplar, days_with_more_errors_request

def main():
    # print("Initialize DB Views.")
    # initialize_views()

    print("Top 3 most popular articles: ")
    result = top_three_articles()
    print(result)

    print("Top most popular Authors:")
    result = top_authors_most_popuplar()
    print(result)

    print("Days with more errors requests: ")
    result = days_with_more_errors_request()
    print(result)


if __name__ == "__main__":
    main()