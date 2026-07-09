import { useEffect, useState } from "react";

import { getActions } from "../services/actionService";

export default function useActions() {

    const [actions, setActions] = useState({});

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    async function refresh() {

        try {

            setLoading(true);

            const data = await getActions();

            setActions(data);

            setError("");

        }

        catch (err) {

            console.error(err);

            setError("Unable to load action mappings.");

        }

        finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        refresh();

    }, []);

    return {

        actions,

        loading,

        error,

        refresh,

    };

}