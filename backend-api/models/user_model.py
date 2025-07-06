from utils.db_utils import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    first_name = db.Column(db.VARCHAR(100), nullable=False)
    last_name = db.Column(db.VARCHAR(100), nullable=False)
    email = db.Column(db.VARCHAR(150), nullable=False, unique=True)
    mobile = db.Column(db.VARCHAR(15), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "mobile": self.mobile
        }

class PlatformModel(db.Model):
    __tablename__ = "platforms"

    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    name = db.Column(db.VARCHAR(100), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class UserPlatformLinkModel(db.Model):
    __tablename__ = "user_platform_links"

    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    platform_id = db.Column(db.Integer, db.ForeignKey("platforms.id"), nullable=False)
    url = db.Column(db.VARCHAR(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "platform_id": self.platform_id,
            "url": self.url
        }

class UserProfessionalSummaryModel(db.Model):
    __tablename__ = "user_professional_summary"

    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.VARCHAR(150), nullable=True)
    summary = db.Column(db.Text, nullable=True)
    about_you = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "summary": self.summary,
            "about_you": self.about_you
        }
