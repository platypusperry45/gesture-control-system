import { useEffect, useState } from "react";

import { getGestures } from "../services/gestureService";

export default function useGestures() {

    const [gestures, setGestures] = useState([]);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    async function load() {

        try {

            setLoading(true);

            const data = await getGestures();

            setGestures(data);

            setError("");

        }

        catch {

            setError("Backend not connected");

            setGestures([]);

        }

        finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        load();

    }, []);

    return{

gestures,

loading,

error,

refresh:load,

};
}
    