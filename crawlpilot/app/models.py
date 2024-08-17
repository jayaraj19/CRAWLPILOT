from app import db

class URLTask(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    url = db.Column(db.String(250), unique=True, nullable=False)
    title = db.Column(db.String(250))
    summary = db.Column(db.String(10000))
    links = db.Column(db.JSON)
    status = db.Column(db.String(250), default='in progress')
    vector = db.Column(db.PickleType)


    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'summary': self.summary,
            'links': self.links,
            'status': self.status

        }