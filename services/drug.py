from flask import jsonify
from db import db
from models.drug import Drug


def throw_error_drug_already_exists():
    error_message = {'error': {'message': 'Drug already exists'}}
    return error_message, 403


def throw_error_drug_not_found():
    error_message = {'error': {'message': 'Bad request'}}
    return error_message, 403


def throw_error_invalid_quantity():
    error_message = {'error': {'message': 'Invalid quantity'}}
    return error_message, 403


def save_new_drug(name, quantity):
    new_drug = Drug(name=name, quantity=quantity)
    db.session.add(new_drug)
    db.session.commit()

    message = {
        '_id': new_drug.as_dict().get('id'),
        'name': new_drug.as_dict().get('name'),
        'quantity': new_drug.as_dict().get('quantity'),
    }

    return message, 200


def get_drug(name):
    drug = Drug.query.filter_by(name=name).first()

    if drug:
        return jsonify(drug.as_dict())

    return None


def get_all_drugs():
    drugs = Drug.query.all()
    response = []

    for drug in drugs:
        response.append(drug.as_dict())

    return jsonify(response)


def update_drug_quantity(drug_to_update, quantity, action):
    if action == "add":
        drug_to_update.quantity += quantity

    if action == "remove":
        drug_to_update.quantity -= quantity

    if not action:
        drug_to_update.quantity = quantity

    db.session.commit()

    return jsonify(drug_to_update.as_dict())


def delete_drug(drug_to_delete):
    db.session.delete(drug_to_delete)
    db.session.commit()

    return {
        "message": "drug deleted",
        "drug_deleted": drug_to_delete.as_dict()
    }
