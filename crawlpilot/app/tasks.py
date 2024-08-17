from app import celery, db
from app.models import URLTask
from app.utils import scrape_page
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity




@celery.task(bind=True)
def crawl_url(self,url):
    from run import model
    title, summary, links = scrape_page(url)
    embedding = model.encode(summary)
    # embedding = None
    print(url)
    url_task = URLTask.query.filter_by(url=url).first()
    url_task.title = title
    url_task.summary = summary
    url_task.links = links
    url_task.vector = embedding
    url_task.status = 'complete'

    db.session.commit()


@celery.task
def bulk_crawl(urls):
    for url in urls:
        crawl_url.delay(url)


def compute_cosine_distance_matrix():
    urls = URLTask.query.filter(URLTask.status == 'complete').all()
    embeddings = [url.vector for url in urls]
    distance_matrix = cosine_similarity(embeddings)

    return distance_matrix