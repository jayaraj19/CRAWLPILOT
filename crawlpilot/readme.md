CRAWLPILOT

Project Overview

CRAWLPILOT is a web scraping and text processing API that allows you to scrape web pages, summarize their content, and analyze the relationships between them using cosine similarity. The project is built using Flask, Celery, SQLite, and Docker. It includes several REST APIs for crawling individual and bulk URLs, generating reports, and computing cosine similarity matrices for text embeddings.

Features

	•	Single URL Scraping: Scrape a single URL to extract the page title, a summary of the page content, and all links on the page.
	•	Bulk URL Crawling: Asynchronously crawl a list of URLs, with progress tracking and results retrieval.
	•	Cosine Similarity: Compute a cosine distance matrix for the content of multiple URLs.
	•	Reports: Generate a paginated list of all crawled URLs without duplicates.