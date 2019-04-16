from log_db import initialize_views, top_three_articles

def main():
    print("Initialize DB Views.")
    initialize_views()


    print("Top 3 most popular articles: ")
    result = top_three_articles()
    print(result)


if __name__ == "__main__":
    main()