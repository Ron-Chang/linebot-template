from flask import Blueprint, jsonify
from werkzeug.exceptions import (
    HTTPException,
    MethodNotAllowed,
    NotFound,
    RequestEntityTooLarge,
    ServiceUnavailable,
)

from constants.error_code import ErrorCode

error_bp = Blueprint('error', __name__)


def make_error_schema(message, error_code, error_key):
    _dict = {
        'message': message,
        'error_code': error_code,
        'error_key': error_key
    }
    return _dict


class _BaseError(Exception):
    """
        base error class
    """

    def __init__(self, code=404, error_code=None, message=None, debug_message=None):
        super(_BaseError, self).__init__()
        self.code = code
        self.message = message
        self.error_code = error_code or ErrorCode.BASE_ERROR
        self.error_key = ErrorCode.value_to_key(self.error_code)
        self.debug_message = debug_message

    def __str__(self):
        return self.__class__.__name__

    def to_dict(self):
        return make_error_schema(
            message=self.message, error_code=self.error_code, error_key=self.error_key)


class NotFoundError(_BaseError):
    def __init__(self, error_code=None, message=None, debug_message=None):
        super(NotFoundError, self).__init__(
            code=404,
            message=message or 'Not Found Error',
            error_code=error_code,
            debug_message=debug_message,
        )


class NotAuthorizedError(_BaseError):
    def __init__(self, error_code=None, message=None, debug_message=None):
        super(NotAuthorizedError, self).__init__(
            code=401,
            message=message or 'Not Authorized Error',
            error_code=error_code,
            debug_message=debug_message,
        )


class ValidationError(_BaseError):
    def __init__(self, error_code=None, message=None, debug_message=None):
        super(ValidationError, self).__init__(
            code=400,
            message=message or 'Validation Error',
            error_code=error_code,
            debug_message=debug_message,
        )


class ExternalServiceError(_BaseError):
    def __init__(self, error_code=None, message=None, debug_message=None):
        super(ExternalServiceError, self).__init__(
            code=400,
            message=message or 'External Service Error',
            error_code=error_code,
            debug_message=debug_message,
        )


# ------------------------- [ Exception Handler ] -------------------------- #


@error_bp.app_errorhandler(ExternalServiceError)
def handle_external_service_error(e):
    return jsonify(e.to_dict()), e.code


@error_bp.app_errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify(e.to_dict()), e.code


@error_bp.app_errorhandler(NotAuthorizedError)
def handle_not_auth_error(e):
    return jsonify(e.to_dict()), e.code


@error_bp.app_errorhandler(NotFoundError)
def handle_not_found_error(e):
    return jsonify(e.to_dict()), e.code


# ------------------------- [ System Exception Handler ] -------------------------- #


@error_bp.app_errorhandler(NotFound)
def handle_404_error(e):
    error_code = ErrorCode.INVALID_OPERATION
    _schema = make_error_schema(
        message='Endpoint Not Found',
        error_code=error_code,
        error_key=ErrorCode.value_to_key(error_code)
    )
    return jsonify(_schema), 404


@error_bp.app_errorhandler(MethodNotAllowed)
def handle_405_error(e):
    error_code = ErrorCode.INVALID_OPERATION
    _schema = make_error_schema(
        message='Method Not Allowed',
        error_code=error_code,
        error_key=ErrorCode.value_to_key(error_code)
    )
    return jsonify(_schema), 405


@error_bp.app_errorhandler(RequestEntityTooLarge)
def handle_413_error(e):
    error_code = ErrorCode.SIZE_ERROR
    _schema = make_error_schema(
        message='File Too Large',
        error_code=error_code,
        error_key=ErrorCode.value_to_key(error_code)
    )
    return jsonify(_schema), 413


@error_bp.app_errorhandler(HTTPException)
def handle_http_error(e):
    error_code = ErrorCode.INVALID_OPERATION
    code = getattr(e, 'code', 400)
    message = getattr(e, 'description', 'Bad Request')
    _schema = make_error_schema(
        message=message,
        error_code=error_code,
        error_key=ErrorCode.value_to_key(error_code)
    )
    return jsonify(_schema), code


@error_bp.app_errorhandler(ServiceUnavailable)
def handle_503_error(e):
    error_code = ErrorCode.BASE_ERROR
    _schema = make_error_schema(
        message='Service Unavailable',
        error_code=error_code,
        error_key=ErrorCode.value_to_key(error_code)
    )
    return jsonify(_schema), 503


@error_bp.app_errorhandler(Exception)
def handle_500_error(e):
    error_code = ErrorCode.BASE_ERROR
    _schema = make_error_schema(
        message='Internal Server Error',
        error_code=error_code,
        error_key=ErrorCode.value_to_key(error_code)
    )
    return jsonify(_schema), 500
