import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from app.extras import custom_pydantic_msg


# Importar endpoints
from app.geoip.routers_geoip import router as router_geoip

# Inicializar FastAPI
app = FastAPI(
    title="GeoIP API",
    description="API para obtener la geolocalizacion de una IP",
    version="1.0.1"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic custom exception handler
app.add_exception_handler(
    RequestValidationError, custom_pydantic_msg.request_validation_error_handler
)
app.add_exception_handler(
    ValidationError, custom_pydantic_msg.validation_error_handler
)
app.add_exception_handler(
    HTTPException, custom_pydantic_msg.http_exception_handler
)
app.add_exception_handler(
    ValueError, custom_pydantic_msg.value_error_handler
)

# Importar endpoints

app.include_router(router_geoip)

# Para realizar debug
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8000, ssl_keyfile="../stack/ssl/localhost.key",
                ssl_certfile="../stack/ssl/localhost.crt", reload=True)