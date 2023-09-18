# pylint: disable=E0611,E0401
import os
import logging

# for fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

# for lambda
from mangum import Mangum

# for libs
from dataclasses import asdict

# app

from router import allocate

logger = logging.getLogger(__name__)  # get root logger
logger.setLevel(logging.DEBUG)
self_pid = os.getpid()


def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI(docs_url=None, redoc_url=None)

    # 미들웨어 정의
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 라우터 정의
    app.include_router(allocate.router)

    return app


app = create_app()


@app.on_event("startup")
async def startup_event():
    global model_data, model
    logger.info('fastapi app started')

    # try:
    #     from sqlalchemy import create_engine
    #
    #     from database.conn import Base
    #
    #     engine = create_engine("sqlite:///./sql_app.db")
    #     Base.metadata.create_all(bind=engine)
    #
    # except Exception as e:
    #     print(e)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        # swagger_css_url="static/swagger-ui.css",
        # swagger_js_url="static/swagger-ui-bundle.js",
        # swagger_favicon_url="static/favicon.png",
    )


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        # redoc_js_url="static/redoc-standalone.js",
        # redoc_favicon_url="static/favicon.png",
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="MTT API Docs.",
        version="3.2.0",
        description="MTT OpenAPI schema",
        routes=app.routes,
    )
    # openapi_schema["info"]["x-logo"] = {
    #     "url": "/static/logo.png"
    # }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

handler = Mangum(app, lifespan="off")

############################ DB 선언 및 테이블 생성 ########################################
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
from database.conn import Base, engine

Base.metadata.create_all(bind=engine)
################################################################################

import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, port=8282)
