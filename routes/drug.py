from flask import Blueprint, request
from flask_expects_json import expects_json

import controllers.drug as controller
import validations.drug as validation

drugs = Blueprint('drugs', __name__)


@drugs.route('/drugs/create', methods=['POST'])
@expects_json(validation.create_new_drug)
def create_new_drug():
    return controller.create_new_drug(request)


@drugs.route('/drugs/', methods=['GET'])
def get_all_drugs():
    return controller.get_all_drugs()


@drugs.route('/drugs/<drug_name>', methods=['GET'])
def get_drug(drug_name):
    return controller.get_drug(drug_name)


@drugs.route('/drugs/update', methods=['POST'])
@expects_json(validation.update_drug_quantity)
def update_quantity():
    return controller.update_quantity(request)


@drugs.route('/drugs/add', methods=['POST'])
@expects_json(validation.update_drug_quantity)
def add_quantity():
    return controller.update_quantity(request, "add")


@drugs.route('/drugs/remove', methods=['POST'])
@expects_json(validation.update_drug_quantity)
def remove_quantity():
    return controller.update_quantity(request, "remove")


@drugs.route('/drugs/delete/<drug_id>', methods=['DELETE'])
def delete_drug(drug_id):
    return controller.delete_drug(drug_id)
