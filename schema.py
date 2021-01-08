PHONE_UPDATE_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "number": {
            "type": "string",
            "minLength": 11,
            "maxLength": 11,
        },
        "type": {
            "type": "string",
            "enum": ["city", "mobile"],
        },
    },
    "anyOf": [{
        "required": ["number"]
    }, {
        "required": ["type"]
    }]
}
