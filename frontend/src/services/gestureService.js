import api from "./api";

export async function getGestures() {
    const { data } = await api.get("/gestures");
    return data;
}

export async function createGesture(payload) {
    const { data } = await api.post("/gestures", payload);
    return data;
}

export async function renameGesture(id, payload) {
    const { data } = await api.put(`/gestures/${id}`, payload);
    return data;
}

export async function deleteGesture(id) {
    const { data } = await api.delete(`/gestures/${id}`);
    return data;
}