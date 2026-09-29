from rest_framework.views import exception_handler

def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response == None:
        return None
    
    data = response.data
    values_are_lists = isinstance(data, dict) and (all(
        isinstance(val, list) for val in data.values())
    )
    if values_are_lists:
        response.data = {
            "code": "invalid",
            "detail": "Validation failed.",
            "fields": data
        }

        return response
    elif values_are_lists == False:
        response.data = {
            "code": data["detail"].code,
            "detail": data["detail"],
        }
        return response
            