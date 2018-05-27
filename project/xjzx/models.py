from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

pymysql.install_as_MySQLdb()

db=SQLAlchemy()

class BaseModel(object):
    create_time=db.Column(db.DateTime,default=datetime.now())
    update_time=db.Column(db.DateTime,default=datetime.now())
    isDelete=db.Column(db.Boolean,default=0)

class NewsCategory(db.Model,BaseModel):
    __tablename__='newscategory'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    news_info=db.relationship('NewsInfo',backref='newscategory',lazy='dynamic')

class NewsInfo(db.Model,BaseModel):
    __tablename__='newsinfo'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    summary=db.Column(db.String(1000))
    pic=db.Column(db.String(50))
    category_id=db.Column(db.Integer,db.ForeignKey('newscategory.id'))
    content=db.Column(db.Text)
    status=db.Column(db.SmallInteger,default=1)
    reason=db.Column(db.String(500))
    user_id=db.Column(db.Integer,db.ForeignKey('userinfo.id'),default=0)
    click_count=db.Column(db.Integer,default=0)
    comment_count=db.Column(db.Integer,default=0)
    newscomment=db.relationship('NewsComment',backref='newsinfo',lazy='dynamic')

tb_news_collect=db.Table('tb_news_collect',db.Column('userinfo_id',db.Integer,db.ForeignKey('userinfo.id')),
                         db.Column('newsinfo_id',db.Integer,db.ForeignKey('newsinfo.id')))
tb_user_follow=db.Table('tb_user_follow',db.Column('origin_id',db.Integer,db.ForeignKey('userinfo.id')),
                        db.Column('follow_id',db.Integer,db.ForeignKey('userinfo.id')))
class UserInfo(db.Model,BaseModel):
    __tablename__='userinfo'
    id=db.Column(db.Integer,primary_key=True)
    mobile=db.Column(db.String(20))
    password_hash=db.Column(db.String(50))
    signature=db.Column(db.String(200))
    nick_name=db.Column(db.String(30))
    gender=db.Column(db.Boolean)
    avatar=db.Column(db.String(50),default='user_pic.png')
    public_count=db.Column(db.Integer,default=0)
    follow_count=db.Column(db.Integer,default=0)
    isAdmin=db.Column(db.Boolean,default=0)
    news=db.relationship('NewsInfo',backref='user',lazy='dynamic')
    news_collect=db.relationship('NewsInfo',secondary=tb_news_collect,lazy='dynamic')
    news_comment=db.relationship('NewsComment',backref='user_info',lazy='dynamic')
    user_on=db.relationship('UserInfo',secondary=tb_user_follow,lazy='dynamic',
                            primaryjoin=id==tb_user_follow.c.origin_id,
                            secondaryjoin=id==tb_user_follow.c.follow_id)

    @property
    def password(self):
        pass
    @password.setter
    def password(self,pwd):
        self.password_hash=generate_password_hash(pwd)
    def check_pwd(self,pwd):
        return check_password_hash(self.password_hash, pwd)

class NewsComment(db.Model,BaseModel):
    __tablename__='newscomment'
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('userinfo.id'))
    news_id=db.Column(db.Integer,db.ForeignKey('newsinfo.id'))
    msg=db.Column(db.String(500))
    like_count=db.Column(db.Integer,default=0)
    comment_id=db.Column(db.Integer,db.ForeignKey('newscomment.id'),default=0)
    comments=db.relationship('NewsComment',lazy='dynamic')





