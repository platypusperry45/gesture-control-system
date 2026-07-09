import api from "./api";

/*
|--------------------------------------------------------------------------
| Training Controls
|--------------------------------------------------------------------------
*/

export async function startTraining(config = {}) {

    const { data } = await api.post(
        "/training/start",
        config
    );

    return data;

}

export async function stopTraining() {

    const { data } = await api.post(
        "/training/reset"
    );

    return data;

}

export async function resetTraining() {

    const { data } = await api.post(
        "/training/reset"
    );

    return data;

}

/*
|--------------------------------------------------------------------------
| Training Status
|--------------------------------------------------------------------------
*/

export async function getTrainingStatus() {

    const { data } = await api.get(
        "/training/status"
    );

    return data;

}

export async function getTrainingLogs() {

    const { data } = await api.get(
        "/training/logs"
    );

    return data;

}

/*
|--------------------------------------------------------------------------
| Model
|--------------------------------------------------------------------------
*/

export async function getModelStatus() {

    const { data } = await api.get(
        "/model/status"
    );

    return data;

}

export async function deployModel() {

    const { data } = await api.post(
        "/train/deploy"
    );

    return data;

}