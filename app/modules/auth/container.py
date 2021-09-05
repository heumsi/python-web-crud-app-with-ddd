from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from app.modules.auth.adapters.repository import DatasetAuthRepository
from app.modules.auth.service_layer.use_cases.get_token import GetToken
from app.modules.auth.service_layer.use_cases.get_token_payload import GetTokenPayload


class AuthContainer(DeclarativeContainer):
    config = providers.Configuration()

    # repositories
    db = providers.Dependency()
    uow = providers.Dependency()
    auth_repository = providers.Singleton(DatasetAuthRepository, db=db)

    # service
    get_token = providers.Singleton(
        GetToken,
        auth_repository=auth_repository,
        jwt_secret_key=config.jwt_secret_key,
        jwt_algorithm=config.jwt_algorithm,
    )
    get_token_payload = providers.Singleton(
        GetTokenPayload,
        jwt_secret_key=config.jwt_secret_key,
        jwt_algorithm=config.jwt_algorithm,
    )
