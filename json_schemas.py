user_config_json_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "token": {"type": "string"},
            "user": {"type": "string"}
        },
        "required": ["token", "user"]
    }
}

authorize_response_json_schema = {
        "type": "object",
        "properties": {
            "token": {"type": "string"},
            "user": {"type": "string"}
        },
        "required": ["token", "user"]
    }

add_meme_response_json_schema = {
        "type": "object",
        "properties": {
            "id": {"type": ["integer", "string"]},
            "info": {
                "type": "object",
                "additionalProperties": True
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "text": {
                "type": "string"
            },
            "updated_by": {
                "type": "string"
            },
            "url": {
                "type": "string",
                "format": "uri"
            },
        },
        "required": ["id", "info", "tags", "text", "updated_by", "url"],
        "additionalProperties": False
    }

get_memes_list_response_json_schema = {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "id": {"type": "integer"},
                    "info": {
                        "type": "object",
                        "additionalProperties": True
                    },
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "text": {
                        "type": "string"
                    },
                    "updated_by": {
                        "type": "string"
                    },
                    "url": {
                        "type": "string",
                        "format": "uri"
                    }
                },
                "required": ["id", "info", "tags", "text", "updated_by", "url"],
                "additionalProperties": False
            }
        },
        "required": ["data"],
        "additionalProperties": False
    }

get_one_meme_response_json_schema = {
        "type": "object",
        "properties": {
            "id": {"type": ["integer", "string"]},
            "info": {
                "type": "object",
                "additionalProperties": True
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "text": {
                "type": "string"
            },
            "updated_by": {
                "type": "string"
            },
            "url": {
                "type": "string",
                "format": "uri"
            },
        },
        "required": ["id", "info", "tags", "text", "updated_by", "url"],
        "additionalProperties": False
    }

update_meme_response_json_schema = {
        "type": "object",
        "properties": {
            "id": {"type": ["integer", "string"]},
            "info": {
                "type": "object",
                "additionalProperties": True
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "text": {
                "type": "string"
            },
            "updated_by": {
                "type": "string"
            },
            "url": {
                "type": "string",
                "format": "uri"
            },
        },
        "required": ["id", "info", "tags", "text", "updated_by", "url"],
        "additionalProperties": False
    }