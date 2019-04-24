#!/usr/bin/env python2.7
#
# Project Analysis Log

from log_db import check_views, top_three_articles
from log_db import top_authors_most_popuplar, days_with_more_errors_request


def main():
    print("Check DB Views.")
    check_views()

    print("Top 3 most popular articles: ")
    top_three_articles()

    print("Top most popular Authors:")
    top_authors_most_popuplar()

    print("Days with more errors requests: ")
    days_with_more_errors_request()


if __name__ == "__main__":
    main()
