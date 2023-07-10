from ipaddress import IPv4Address
from fastapi import APIRouter, status
from app.geoip.internals_geoip import ConsultorCiudadOrigen
from app.geoip.schemas_geoip import GeoIpResponseSchema

router = APIRouter(
    prefix="/api/v1",
    tags=["GeoIP"],

)

# Instanciar la clase ConsultorCiudadOrigen

@router.get(
        "/geoip/{ip_address}", 
        status_code=status.HTTP_200_OK,
        summary="Obtener la geolocalizacion de una IP",
        response_description="Regresa la geolocalizacion de una IP",
        response_model=GeoIpResponseSchema
        )
async def get_geoip(ip_address: IPv4Address):
    """**Obtener la geolocalizacion de una IP**.
    
    Este endpoint regresa la geolocalizacion de una IP.

    Para realizar la consulta se utilizan los siguientes servicios:
    - https://geolocation-db.com/
    - https://ipinfo.io/
    - http://api.hostip.info/
    - https://json.geoiplookup.io
    - http://ip-api.com/
    - https://api.ipbase.com/

    Ingresa una IP y regresa la geolocalizacion aproximada de la IP.

    Returns:
        Status code 200: Si la consulta fue exitosa.
        Status code 422: Si la IP no es valida.
    """
    return ConsultorCiudadOrigen(ip_address).obtener_ciudad_origen()
