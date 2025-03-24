from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database 지정
engine = create_engine('sqlite:///test.db')

# ORM 사용 
Base = declarative_base()

# User 모델 정의
class User(Base):
    __tablename__ = 'users'  # 테이블 이름
    id = Column(Integer, primary_key=True)  # 열 정의
    name = Column(String(50))
    age = Column(Integer)

# 엔진과 연결된 DB에 테이블 생성
Base.metadata.create_all(engine)

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

# 새로운 User 객체 생성
user1 = User(name="Kim", age=30)
user2 = User(name="Park", age=20)
user3 = User(name="Alice", age=15)

# 세션에 추가하고 커밋
session.add_all([user1, user2, user3])
session.commit()
