import { useEffect, useState } from "react";

import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    TextField,
    MenuItem,
    Button,
    Switch,
    FormControlLabel,
    Stack,
} from "@mui/material";

import SaveIcon from "@mui/icons-material/Save";

import toast from "react-hot-toast";

import { updateAction } from "../../services/actionService";

const TYPES = [
    "Keyboard",
    "Media",
    "Browser",
    "Mouse",
    "System",
];

export default function EditActionDialog({

    action,

    onClose,

    refresh,

}) {

    const [gesture, setGesture] = useState("");
    const [type, setType] = useState(TYPES[0]);
    const [mappedAction, setMappedAction] = useState("");
    const [enabled, setEnabled] = useState(true);

    useEffect(() => {

        if (!action) return;

        setGesture(action.gesture);
        setType(action.type);
        setMappedAction(action.action);
        setEnabled(action.enabled);

    }, [action]);

    async function handleSave() {

        try {

            await updateAction(gesture, {

                type,

                action: mappedAction,

                enabled,

            });

            toast.success("Mapping updated");

            refresh();

            onClose();

        }

        catch (err) {

            console.error(err);

            toast.error("Failed to update mapping");

        }

    }

    return (

        <Dialog
            open={Boolean(action)}
            onClose={onClose}
            fullWidth
            maxWidth="sm"
        >

            <DialogTitle>
                Edit Action Mapping
            </DialogTitle>

            <DialogContent>

                <Stack spacing={2} sx={{ mt: 1 }}>

                    <TextField
                        label="Gesture"
                        value={gesture}
                        disabled
                        fullWidth
                    />

                    <TextField
                        select
                        label="Action Type"
                        value={type}
                        fullWidth
                        onChange={(e) =>
                            setType(e.target.value)
                        }
                    >

                        {TYPES.map((item) => (

                            <MenuItem
                                key={item}
                                value={item}
                            >
                                {item}
                            </MenuItem>

                        ))}

                    </TextField>

                    <TextField
                        label="Assigned Action"
                        value={mappedAction}
                        fullWidth
                        onChange={(e) =>
                            setMappedAction(e.target.value)
                        }
                    />

                    <FormControlLabel
                        control={
                            <Switch
                                checked={enabled}
                                onChange={(e) =>
                                    setEnabled(e.target.checked)
                                }
                            />
                        }
                        label="Enable this mapping"
                    />

                </Stack>

            </DialogContent>

            <DialogActions>

                <Button
                    onClick={onClose}
                >
                    Cancel
                </Button>

                <Button
                    variant="contained"
                    startIcon={<SaveIcon />}
                    onClick={handleSave}
                >
                    Save Changes
                </Button>

            </DialogActions>

        </Dialog>

    );

}