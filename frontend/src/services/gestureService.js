import api from "./api";

export async function getGestures() {
    const { data } = await api.get("/gestures");
    return data;
}

export async function addGesture(name) {
    return api.post("/gestures", { name });
}

export async function renameGesture(oldName, newName) {
    return api.put(`/gestures/${oldName}`, {
        new_name: newName,
    });
}

export async function deleteGesture(name) {
    return api.delete(`/gestures/${name}`);
}

export async function getDatasetSummary() {
    const { data } = await api.get("/gestures/summary");
    return data;
}