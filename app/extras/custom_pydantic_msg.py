from fastapi import Request, status
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from pydantic_translations import Translator

tr = Translator("es")


def get_response_validation_error(exc):
    """Funcion para obtener los campos de la validacion de pydantic.

    Args:
        fields (List): Lista de campos

    Returns:
        String: Regresa un string con los campos
    """
    err = exc.errors()[0]
    err = tr.translate_error(err)

    error_msg = {"success": False, "msg": (str(err["loc"][-1])) + ": " + err["msg"]}

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=error_msg,
    )


def request_validation_error_handler(request: Request, exc: RequestValidationError) -> JSONResponse:

    return get_response_validation_error(exc)


def validation_error_handler(request: Request, exc: ValidationError) -> JSONResponse:
    return get_response_validation_error(exc)


def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:

    err = {"success": False, "msg": exc.detail}
    status_code = exc.status_code
    return JSONResponse(
        status_code=status_code,
        content=err
    )


def value_error_handler(request: Request, exc: ValueError) -> JSONResponse:
    print("value_error_handler")
    err = {"success": False, "msg": exc.args[0]}
    status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(
        status_code=status_code,
        content=err)
