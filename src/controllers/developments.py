from app import app
from handlers.error_handler import NotFoundError, ValidationError
from constants.error_code import ErrorCode


@app.route("/200", methods=['GET'])
def probe():
    return 'ok'


@app.route("/404", methods=['GET'])
def not_found_error():
    raise NotFoundError(ErrorCode.INVALID_EMAIL)


@app.route("/400", methods=['GET'])
def validation_error():
    raise ValidationError(ErrorCode.PAYLOAD_ERROR)
