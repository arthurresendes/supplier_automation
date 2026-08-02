from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from rotas import router
from slowapi import  _rate_limit_exceeded_handler
from limitador import limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI(title='API Supplier Automation', version='1.0.0')
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://supplier-automationn.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)