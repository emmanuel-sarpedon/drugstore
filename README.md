# Drugstore - Inventaire de pharmacie

---
## Ajouter un nouveau médicament à l'inventaire.

```/drugs/create POST```

**Paramètres:**
```json
{
  "name": "DOLIPRANE",
  "quantity": 10
}
```
**En cas de succès:**
```json

{
  "_id": 1,
  "name": "ASPEGIC",
  "quantity": 10
}
```

## Obtenir les quantités de tous les médicaments.

```/drugs GET```

**En cas de succès:**
```json
[
    {
        "_id": 1,
        "name": "DOLIPRANE",
        "quantity": 20
    },
    {
        "_id": 2,
        "name": "IBUPROFENE",
        "quantity": 10
    }
]
```

## Ajouter une quantité dans l'inventaire

```/drugs/add PUT```
**Paramètres:**
```json
{
  "id": 1,
  "quantity": 5
}
```
Ajoutera 5 DOLIPRANE dans l'inventaire

## Retirer une quantité dans l'inventaire

```/drugs/remove PUT```
**Paramètres:**
```json
{
  "id": 1,
  "quantity": 3
}
```
Ajoutera 3 DOLIPRANE dans l'inventaire

## Supprimer un médicament de l'inventaire

```/drugs/delete/:drug_id DELETE```
**Paramètres:**
```json
{
  "id": 1,
  "quantity": 5
}
```
Ajoutera 5 DOLIPRANE dans l'inventaire
