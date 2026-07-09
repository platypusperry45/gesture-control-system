import { useMemo, useState } from "react";

import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
    MenuItem,
    TextField,
    Stack,
    Typography,
} from "@mui/material";

import toast from "react-hot-toast";

import { createAction } from "../../services/actionService";

const GESTURES = [
    "open_palm",
    "fist",
    "thumbs_up",
    "peace",
    "okay",
    "point",
];

const ACTIONS = {

    Keyboard: [
        "Ctrl+C",
        "Ctrl+V",
        "Ctrl+X",
        "Ctrl+Z",
        "Ctrl+Y",
        "Alt+Tab",
        "Win+D",
    ],

    Media: [
        "Play/Pause",
        "Next Track",
        "Previous Track",
        "Volume Up",
        "Volume Down",
        "Mute",
    ],

    Browser: [
        "New Tab",
        "Close Tab",
        "Refresh",
        "Back",
        "Forward",
    ],

    Mouse: [
        "Left Click",
        "Right Click",
        "Double Click",
    ],

    System: [
        "Screenshot",
        "Lock PC",
        "Sleep",
    ],

};

export default function AddActionDialog({

    open,
    onClose,
    refresh,

}) {

    const [gesture, setGesture] = useState("");

    const [type, setType] = useState("Media");

    const [action, setAction] = useState("");

    const actions = useMemo(
        () => ACTIONS[type] || [],
        [type]
    );

    async function submit() {

        if (!gesture || !action) {

            toast.error("Please complete all fields.");

            return;

        }

        try {

            await createAction({

                gesture,

                type,

                action,

                enabled: true,

            });

            toast.success("Gesture mapping created.");

            refresh();

            onClose();

            setGesture("");

            setAction("");

            setType("Media");

        }

        catch {

            toast.error("Unable to save mapping.");

        }

    }

    return (

        <Dialog
            open={open}
            onClose={onClose}
            maxWidth="sm"
            fullWidth
        >

            <DialogTitle>

                <Typography
                    variant="h5"
                    fontWeight={700}
                >

                    Create Gesture Mapping

                </Typography>

            </DialogTitle>

            <DialogContent>

                <Stack spacing={3} mt={1}>

                    <TextField

                        select

                        fullWidth

                        label="Gesture"

                        value={gesture}

                        onChange={(e)=>
                            setGesture(e.target.value)
                        }

                    >

                        {

                            GESTURES.map(g=>

                                <MenuItem
                                    key={g}
                                    value={g}
                                >

                                    {g}

                                </MenuItem>

                            )

                        }

                    </TextField>

                    <TextField

                        select

                        fullWidth

                        label="Action Type"

                        value={type}

                        onChange={(e)=>{

                            setType(e.target.value);

                            setAction("");

                        }}

                    >

                        {

                            Object.keys(ACTIONS).map(type=>

                                <MenuItem

                                    key={type}

                                    value={type}

                                >

                                    {type}

                                </MenuItem>

                            )

                        }

                    </TextField>

                    <TextField

                        select

                        fullWidth

                        label="Action"

                        value={action}

                        onChange={(e)=>
                            setAction(e.target.value)
                        }

                    >

                        {

                            actions.map(action=>

                                <MenuItem

                                    key={action}

                                    value={action}

                                >

                                    {action}

                                </MenuItem>

                            )

                        }

                    </TextField>

                </Stack>

            </DialogContent>

            <DialogActions>

                <Button onClick={onClose}>

                    Cancel

                </Button>

                <Button

                    variant="contained"

                    onClick={submit}

                >

                    Save Mapping

                </Button>

            </DialogActions>

        </Dialog>

    );

}