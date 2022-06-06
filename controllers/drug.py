from models.drug import Drug
import services.drug as service


def create_new_drug(request):
    name = request.get_json().get("name")
    quantity = request.get_json().get("quantity")

    drug = Drug.query.filter_by(name=name).first()

    if drug:
        return service.throw_error_drug_already_exists()

    if not drug:
        return service.save_new_drug(name, quantity)


def get_all_drugs():
    return service.get_all_drugs()


def get_drug(name):
    drug = service.get_drug(name)

    if drug:
        return service.get_drug(name)

    return service.throw_error_drug_not_found()


def update_quantity(request, action=None):
    drug_id = request.get_json().get("id")
    quantity = request.get_json().get("quantity")

    drug_to_update = Drug.query.filter_by(id=drug_id).first()

    if not drug_to_update:
        return service.throw_error_drug_not_found()

    if action == "remove" and drug_to_update.quantity - quantity < 0:
        return service.throw_error_invalid_quantity()

    if drug_to_update:
        return service.update_drug_quantity(drug_to_update, quantity, action)


def delete_drug(drug_id):
    drug_to_delete = Drug.query.filter_by(id=drug_id).first()

    if not drug_to_delete:
        return service.throw_error_drug_not_found()

    return service.delete_drug(drug_to_delete)
