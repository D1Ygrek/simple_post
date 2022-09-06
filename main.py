import uvicorn

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from parsers.log_parser import parse_log

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

security = HTTPBasic()

@app.post("/WMLS_GetFromStore")
async def get_from_store(
    req: Request,
    credentials: HTTPBasicCredentials = Depends(security)
    ):
    #check_cred()
    ask = await req.body()
    return parse_log(ask.decode('utf-8'))


if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port = 2727, reload=True)