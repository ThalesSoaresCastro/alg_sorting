from fastapi import Depends, FastAPI, HTTPException
from tools.data_processing import ordered_array


import traceback2 as traceback
from logging42 import logger

app = FastAPI()

from tools.cached_data import redis_set

redis_set()

@app.get('/')
async def root():
    return {"API Version":1.0}

@app.get('/sort_alg',)
async def ordered_data():
    resp = await ordered_array()
    if not resp['arr']:
        logger.warning(f'Erro na rota /sort_alg. status_code {500}, msg:{resp.msg}')
        raise HTTPException(status_code=500, detail=resp['msg'])
    logger.info(f'Dados enviados com sucesso! rota /sort_alg status_code {200}')
    return resp