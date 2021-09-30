from .master_password import verify_password, un_flatten_hash
from .key_derivation_service import derive_key
from .encryption_service import decrypt
from database import get_user
from models import MasterPasswordParameters, KeyDerivationParameters, AuthenticateResult, User
from typing import Tuple


def authenticate(username, password, params) -> Tuple[AuthenticateResult, User]:
    user_result = None
    authenticate_result = None

    if not username or not password:
        return (AuthenticateResult.Failed, None)

    user = get_user(username)

    if user is None:
        return (AuthenticateResult.UsernameDoesNotExist, None)

    unflattened = un_flatten_hash(user.hash)

    hash_params = MasterPasswordParameters(
        KeyDerivationParameters(
            unflattened.alg,
            unflattened.keysize,
            unflattened.saltsize,
            unflattened.iterations,
            unflattened.degree_of_parallelism,
            unflattened.memory_size
        ),
        -1
    )

    valid = verify_password(password, unflattened.salt, unflattened.hash, hash_params)

    if valid:
        authenticate_result = AuthenticateResult.Successful

        ran_key = decrypt(user.encrypted_key, password)

        user_result = User(user.unique_id,
                           None,
                           user.username,
                           None,
                           decrypt(user.firstname, ran_key),
                           decrypt(user.lastname, ran_key),
                           decrypt(user.phone_number, ran_key),
                           decrypt(user.email, ran_key),
                           user.sw_version,
                           True,
                           ran_key)

    else:
        authenticate_result = AuthenticateResult.PasswordIncorrect

    return (authenticate_result, user_result)