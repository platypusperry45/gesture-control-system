from __future__ import annotations

import json
from pathlib import Path

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/actions",
    tags=["Actions"],
)

MAPPING_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "action_mappings.json"
)


def load():

    if not MAPPING_FILE.exists():

        return {}

    with open(
        MAPPING_FILE,
        "r",
        encoding="utf-8",
    ) as f:

        return json.load(f)


def save(data):

    with open(
        MAPPING_FILE,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
        )


# ----------------------------------
# GET
# ----------------------------------

@router.get("")
def get_actions():

    return load()


# ----------------------------------
# POST
# ----------------------------------

@router.post("")
def create_action(mapping: dict):

    data = load()

    gesture = mapping["gesture"]

    data[gesture] = {

        "type": mapping["type"],

        "action": mapping["action"],

        "enabled": mapping["enabled"],

    }

    save(data)

    return {"success": True}


# ----------------------------------
# PUT
# ----------------------------------

@router.put("/{gesture}")
def update_action(
    gesture: str,
    mapping: dict,
):

    data = load()

    if gesture not in data:

        raise HTTPException(
            404,
            "Gesture not found",
        )

    data[gesture] = mapping

    save(data)

    return {"success": True}


# ----------------------------------
# DELETE
# ----------------------------------

@router.delete("/{gesture}")
def delete_action(
    gesture: str,
):

    data = load()

    if gesture in data:

        del data[gesture]

        save(data)

    return {"success": True}