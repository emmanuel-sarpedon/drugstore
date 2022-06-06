create_new_drug = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "quantity": {"type": "number", "minimum": 0}
    },
    "required": ["name", "quantity"]
}

update_drug_quantity = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "quantity": {"type": "number", "minimum": 0}
    },
    "required": ["id", "quantity"]
}
