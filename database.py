from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



db_dependency: Annotated(Session, Depends(get_db))
user_dependency: Annotated(dict, Depends(get_current_user))
token: Annotated(str, Depends(oauth2_bearer)) 
formdata: Annotated(OAuth2PasswordRequestForm, Depends())

bcrypt_context=CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer=OAuth2PasswordBearer(tokenUrl='/auth/token')
Annotated[str, Depends(oauth2_bearer))

router = APIRouter(tags=['auth'], prefix='/auth')
app = FastAPI()
app.include_router(auth.router)


