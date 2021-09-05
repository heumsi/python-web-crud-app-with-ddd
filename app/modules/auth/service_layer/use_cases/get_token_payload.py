from jose import JWTError, jwt
from pydantic import BaseModel, ValidationError

from app.modules.auth.domain.model import TokenPayload
from app.modules.auth.service_layer.exceptions import TokenInvalidError


class GetTokenPayloadRequest(BaseModel):
    token: str


class GetTokenPayloadResponse(BaseModel):
    user_id: str


class GetTokenPayload:
    def __init__(self, jwt_secret_key: str, jwt_algorithm: str) -> None:
        self._jwt_secret_key = jwt_secret_key
        self._jwt_algorithm = jwt_algorithm

    def execute(self, req: GetTokenPayloadRequest) -> GetTokenPayloadResponse:
        try:
            decoded_jwt = jwt.decode(
                token=req.token,
                key=self._jwt_secret_key,
                algorithms=self._jwt_algorithm,
            )
            token_payload = TokenPayload(**decoded_jwt)
        except JWTError:
            raise TokenInvalidError("올바른 토큰이 아닙니다.")
        except ValidationError:
            raise TokenInvalidError("토큰 페이로드 버전이 맞지 않습니다. 새로 토큰을 발급해주세요.")
        return GetTokenPayloadResponse(user_id=token_payload.user_id)
