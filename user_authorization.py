from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

    def setup(self):
        engine = create_engine('sqlite:///%s' % 'userdata.db')
        Base.metadata.create_all(engine)
        metadata = MetaData(engine)
        self.session = sessionmaker(bind=engine)()
        metadata.create_all(engine)

    def add_user(self, userdata):
        new_user = User(name=userdata, fullname=userdata, nickname=userdata)
        self.session.add(new_user)
        self.session.commit()

    def find_user(self, userdata):
        # result = self.session.query(User)
        # for row in result:
        #     print(row)
        result = self.session.query(User).filter_by(name=userdata).first()
        return result is not None


# using class
user_authorization = User()
user_authorization.setup()
user_authorization.add_user('Jim')
print(user_authorization.find_user('Sam'))
