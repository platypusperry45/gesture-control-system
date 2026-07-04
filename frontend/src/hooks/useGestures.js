import { useEffect, useState } from "react";
import * as gestureService from "../services/gestureService";

export default function useGestures() {

    const [gestures, setGestures] = useState([]);
    const [loading, setLoading] = useState(true);

    async function load() {
        try {
            const data = await gestureService.getGestures();
            setGestures(data);
        } catch {
            // Temporary demo data
            setGestures([
                { id: 1, name: "Open Hand", samples: 128 },
                { id: 2, name: "Thumbs Up", samples: 94 },
                { id: 3, name: "Victory", samples: 117 },
                { id: 4, name: "Fist", samples: 102 },
            ]);
        }

        setLoading(false);
    }

    useEffect(() => {
        load();
    }, []);

    return {
        gestures,
        loading,
        reload: load,
    };
}