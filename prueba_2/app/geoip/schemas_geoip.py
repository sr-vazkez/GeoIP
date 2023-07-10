from ipaddress import IPv4Address
from pydantic import BaseModel, Field

class GeoIpResponseSchema(BaseModel):
    status: bool = Field(True, description="Estatus de la consulta")
    msg: str = Field(description="Mensaje de la consulta")
    ip_address: IPv4Address = Field(description="IP consultada")