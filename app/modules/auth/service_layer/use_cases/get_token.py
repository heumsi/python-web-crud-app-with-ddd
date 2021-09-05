from jose import JWTError, jwt
from pydantic import BaseModel

from app.modules.auth.domain.model import TokenPayload
from app.modules.auth.domain.repository import AuthRepository
from app.modules.auth.service_layer.exceptions import (
    TokenCreateError,
    UserNotFoundError, PasswordInvalidError,
)


class GetTokenRequest(BaseModel):
    user_id: str
    user_pasword: str


class GetTokenResponse(BaseModel):
    token: str


class GetToken:
    def __init__(
        self, auth_repository: AuthRepository, jwt_secret_key: str, jwt_algorithm: str
    ) -> None:
        self._auth_repository = auth_repository
        self._jwt_secret_key = jwt_secret_key
        self._jwt_algorithm = jwt_algorithm

    def execute(self, req: GetTokenRequest) -> GetTokenResponse:
        user = self._auth_repository.find_by_user_id(req.user_id)
        if not user:
            raise UserNotFoundError("존재하지 않는 유저입니다.")
        if user.password != req.user_pasword:
            raise PasswordInvalidError("패스워드가 일치하지 않습니다.")
        token_payload = TokenPayload(user_id=user.id)
        token = self._create_token(payload=token_payload)
        return GetTokenResponse(token=token)

    def _create_token(self, payload: TokenPayload) -> str:
        try:
            return jwt.encode(
                payload.dict(), self._jwt_secret_key, algorithm=self._jwt_algorithm
            )
        except JWTError:
            raise TokenCreateError("토큰을 만드는데 실패했습니다.")
