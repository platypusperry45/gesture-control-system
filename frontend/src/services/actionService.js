import api from "./api";

export async function getActions() {

    const { data } = await api.get("/actions");

    return data;

}

export async function createAction(mapping) {

    await api.post(
        "/actions",
        mapping,
    );

}

export async function updateAction(
    gesture,
    mapping,
) {

    await api.put(

        `/actions/${gesture}`,

        mapping,

    );

}

export async function deleteAction(
    gesture,
) {

    await api.delete(

        `/actions/${gesture}`,

    );

}