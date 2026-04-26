from scraper.scrape_quotes import main as scrape_main
from scripts.create_vector_db import main as vector_main
from scripts.classify import main as classify_main
from scripts.search import run_search
from scripts.insights import main as insights_main
from scripts.summary import main as summary_main


def run_pipeline():

    print("\nSTEP 1: Scraping Data")
    scrape_main()

    print("\nSTEP 2: Creating Vector DB")
    vector_main()

    print("\nSTEP 3: Classifying Data")
    classify_main()

    print("\nSTEP 4: Generating Insights")
    insights_main()

    print("\nSTEP 5: AI Summary")
    summary_main()

    print("\n--- SYSTEM READY FOR SEARCH ---\n")

    # 🔁 Interactive Search Loop
    while True:

        run_search()

        choice = input("\nDo you want to search again? (y/n): ").lower()

        if choice != "y":
            print("\nExiting system...")
            break


if __name__ == "__main__":
    run_pipeline()
    