from jose import jwt, JWTError
from pydantic import BaseModel

from app.auth.domain.model import TokenPayload
from app.users.domain.exceptions import UserNotFoundError
from app.users.service_layer.read import ReadUser, ReadUserRequest


class GetTokenRequest(BaseModel):
    user_id: str
    user_pasword: str


class GetTokenResponse(BaseModel):
    token: str


class GetTokenError(Exception):
    pass


class GetToken:
    def __init__(
        self, read_user: ReadUser, jwt_secret_key: str, jwt_algorithm: str
    ) -> None:
        self._read_user = read_user
        self._jwt_secret_key = jwt_secret_key
        self._jwt_algorithm = jwt_algorithm

    def execute(self, req: GetTokenRequest) -> GetTokenResponse:
        try:
            read_user_response = self._read_user.execute(ReadUserRequest(id=req.user_id))
        except UserNotFoundError as e:
            raise GetTokenError(str(e))
        token_payload = TokenPayload(user_id=read_user_response.id)
        token = self._create_token(payload=token_payload)
        return GetTokenResponse(token=token)

    def _create_token(self, payload: TokenPayload) -> str:
        try:
            return jwt.encode(payload.dict(), self._jwt_secret_key, algorithm=self._jwt_algorithm)
        except JWTError:
            raise GetTokenError("토큰을 만드는데 실패했습니다.")
