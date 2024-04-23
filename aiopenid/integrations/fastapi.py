from typing import Annotated, Any

from aiopenid.oauth2 import BaseOauth2


try:
    from fastapi import Request, Query
except ImportError:
    raise Exception("FastAPI is not installed")


class OAuth2AuthorizationCodeCallback:
    def __init__(self, client: BaseOauth2) -> None:
        self.client = client

    async def __call__(self, request: Request, code: Annotated[str, Query()]) -> Any:
        redirect_url = str(request.url)

        return await self.client.authorization_code_callback(
            code=code, redirect_uri=redirect_url
        )
