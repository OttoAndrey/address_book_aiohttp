CREATE_PHONE_REQUEST_SCHEMA = {
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
        "user_id": {
            "type": "integer",
            "exclusiveMinimum": 0,
        },
    },
    "required": ["number", "type", "user_id"],
}

CREATE_EMAIL_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "address": {
            "type": "string",
            "maxLength": 254,
            "format": "email",
            "pattern": "^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$",
        },
        "type": {
            "type": "string",
            "enum": ["work", "personal"],
        },
        "user_id": {
            "type": "integer",
            "exclusiveMinimum": 0,
        },
    },
    "required": ["address", "type", "user_id"],
}

CREATE_USER_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "full_name": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 255,
                },
                "sex": {
                    "type": "string",
                    "enum": ["male", "female"],
                },
                "birthdate": {
                    "type": "string",
                    "pattern": "[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])",
                    "format": "date",
                },
                "living_address": {
                    "type": "string",
                },
                "avatar_url": {
                    "type": "string",
                }
            },
            "required": ["full_name", "sex", "birthdate", "living_address"]
        },
        "email": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string",
                    "maxLength": 254,
                    "format": "email",
                    "pattern": "^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$",
                },
                "type": {
                    "type": "string",
                    "enum": ["work", "personal"],
                },
            },
            "required": ["address", "type"]
        },
        "phone": {
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
            "required": ["number", "type"]
        },
    },
    "required": ["user"],
}

UPDATE_PHONE_REQUEST_SCHEMA = {
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
        "user_id": {
            "type": "integer",
            "exclusiveMinimum": 0,
        },
    },
    "anyOf": [{
        "required": ["number"]
    },
        {
            "required": ["type"]
        },
        {
            "required": ["user_id"]
        }]
}

UPDATE_EMAIL_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "address": {
            "type": "string",
            "maxLength": 254,
            "format": "email",
            "pattern": "^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$",
        },
        "type": {
            "type": "string",
            "enum": ["work", "personal"],
        },
        "user_id": {
            "type": "integer",
            "exclusiveMinimum": 0,
        },
    },
    "anyOf": [{
        "required": ["address"]
    },
        {
            "required": ["type"]
        },
        {
            "required": ["user_id"]
        }]
}

UPDATE_USER_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "full_name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 255,
        },
        "sex": {
            "type": "string",
            "enum": ["male", "female"],
        },
        "birthdate": {
            "type": "string",
            "pattern": "[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])",
            "format": "date",
        },
        "living_address": {
            "type": "string",
        },
        "avatar_url": {
            "type": "string",
        }
    },
    "anyOf": [{
        "required": ["full_name"]
    },
        {
            "required": ["sex"]
        },
        {
            "required": ["birth_date"]
        },
        {
            "required": ["living_address"]
        },
        {
            "required": ["avatar_url"]
        }]
}
