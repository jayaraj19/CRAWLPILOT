from flask import Blueprint, request, jsonify
from app.models import URLTask
from app import db,app





@app.route('/crawl', methods=['POST'])
def crawl():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    url_task = URLTask(url=url)
    db.session.add(url_task)
    db.session.commit()
    from app.tasks import crawl_url
    crawl_url.delay(url)
    # crawl_url(url)
    return jsonify({'message': 'Crawling started', 'data': url_task.to_dict()}), 202


@app.route('/bulk-crawl', methods=['POST'])
def bulk_crawl_view():
    urls = request.json.get('urls')
    if not urls:
        return jsonify({'error': 'URLs are required'}), 400
    from app.tasks import bulk_crawl
    bulk_crawl.delay(urls)

    return jsonify({'message': 'Bulk crawling started'}), 202


@app.route('/status/<int:task_id>', methods=['GET'])
def status(task_id):
    url_task = URLTask.query.get_or_404(task_id)
    # if url_task.status == 'in progress':
    #     return jsonify({'status': 'in progress'}), 200

    response = {
        'url': url_task.url,
        'title': url_task.title,
        'summary': url_task.summary,
        'links': url_task.links
    }
    return jsonify(response), 200


@app.route('/report', methods=['GET'])
def report():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    pagination = URLTask.query.filter(URLTask.status == 'complete').paginate(page, per_page, False)
    urls = pagination.items

    response = []
    for url in urls:
        response.append({
            'url': url.url,
            'title': url.title,
            'summary': url.summary,
            'links': url.links
        })

    return jsonify({
        'urls': response,
        'total': pagination.total,
        'page': pagination.page,
        'pages': pagination.pages
    })


@app.route('/distance-matrix', methods=['GET'])
def distance_matrix():
    from app.tasks import compute_cosine_distance_matrix
    matrix = compute_cosine_distance_matrix()
    return jsonify(matrix.tolist())