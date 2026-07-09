import { useEffect, useState } from "react";

import {

    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    TextField,
    MenuItem,
    Button,

} from "@mui/material";

import toast from "react-hot-toast";

import api from "../../services/api";

import {

    createAction,

} from "../../services/actionService";

import {

    ACTION_TYPES,

} from "../../constants/actions";

export default function AddActionDialog({

    open,

    onClose,

    refresh,

}) {

    const [gestures, setGestures] = useState([]);

    const [gesture, setGesture] = useState("");

    const [type, setType] = useState("Keyboard");

    const [action, setAction] = useState("");

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        async function loadGestures() {

            try {

                const { data } = await api.get("/gestures");

                setGestures(data);

            }

            catch (err) {

                console.error(err);

            }

        }

        if (open) {

            loadGestures();

            setGesture("");

            setType("Keyboard");

            setAction("");

        }

    }, [open]);

    useEffect(() => {

        if (ACTION_TYPES[type]?.length) {

            setAction(ACTION_TYPES[type][0]);

        }

    }, [type]);

    async function submit() {

        if (!gesture) {

            toast.error("Select a gesture.");

            return;

        }

        try {

            setLoading(true);

            await createAction({

                gesture,

                type,

                action,

                enabled: true,

            });

            toast.success("Action mapping created.");

            refresh();

            onClose();

        }

        catch (err) {

            toast.error(

                err.response?.data?.detail ||

                "Unable to create mapping."

            );

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <Dialog

            open={open}

            onClose={onClose}

            fullWidth

            maxWidth="sm"

        >

            <DialogTitle>

                Add Action Mapping

            </DialogTitle>

            <DialogContent>

                <TextField

                    select

                    fullWidth

                    margin="normal"

                    label="Gesture"

                    value={gesture}

                    onChange={(e)=>setGesture(e.target.value)}

                >

                    {

                        gestures.map(g=>(

                            <MenuItem

                                key={g.name}

                                value={g.name}

                            >

                                {g.name}

                            </MenuItem>

                        ))

                    }

                </TextField>

                <TextField

                    select

                    fullWidth

                    margin="normal"

                    label="Action Type"

                    value={type}

                    onChange={(e)=>setType(e.target.value)}

                >

                    {

                        Object.keys(ACTION_TYPES).map(key=>(

                            <MenuItem

                                key={key}

                                value={key}

                            >

                                {key}

                            </MenuItem>

                        ))

                    }

                </TextField>

                <TextField

                    select

                    fullWidth

                    margin="normal"

                    label="Action"

                    value={action}

                    onChange={(e)=>setAction(e.target.value)}

                >

                    {

                        ACTION_TYPES[type]?.map(a=>(

                            <MenuItem

                                key={a}

                                value={a}

                            >

                                {a}

                            </MenuItem>

                        ))

                    }

                </TextField>

            </DialogContent>

            <DialogActions>

                <Button

                    onClick={onClose}

                    disabled={loading}

                >

                    Cancel

                </Button>

                <Button

                    variant="contained"

                    onClick={submit}

                    disabled={loading}

                >

                    {

                        loading

                        ?

                        "Saving..."

                        :

                        "Save"

                    }

                </Button>

            </DialogActions>

        </Dialog>

    );

}