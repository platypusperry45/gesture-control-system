import { useEffect, useState } from "react";

import {

    Dialog,

    DialogTitle,

    DialogContent,

    DialogActions,

    Button,

    TextField,

} from "@mui/material";

import toast from "react-hot-toast";

import { renameGesture } from "../../services/gestureService";

export default function RenameGestureDialog({

    gesture,

    onClose,

    refresh,

}) {

    const [name, setName] = useState("");

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        setName(gesture?.name || "");

    }, [gesture]);

    async function submit() {

        if (!gesture) return;

        if (!name.trim()) {

            toast.error("Gesture name cannot be empty.");

            return;

        }

        try {

            setLoading(true);

            await renameGesture(

                gesture.name,

                name.trim()

            );

            toast.success("Gesture renamed.");

            refresh();

            onClose();

        }

        catch (err) {

            toast.error(

                err.response?.data?.detail ||

                "Rename failed."

            );

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <Dialog

            open={Boolean(gesture)}

            onClose={onClose}

            fullWidth

            maxWidth="sm"

        >

            <DialogTitle>

                Rename Gesture

            </DialogTitle>

            <DialogContent>

                <TextField

                    fullWidth

                    margin="normal"

                    label="New Name"

                    value={name}

                    onChange={(e) =>

                        setName(e.target.value)

                    }

                />

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

                    {loading ? "Saving..." : "Save"}

                </Button>

            </DialogActions>

        </Dialog>

    );

}