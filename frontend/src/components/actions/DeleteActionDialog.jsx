import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Typography,
    Button,
    Stack,
} from "@mui/material";

import WarningAmberRoundedIcon from "@mui/icons-material/WarningAmberRounded";

import toast from "react-hot-toast";

import {
    deleteAction,
} from "../../services/actionService";

export default function DeleteActionDialog({

    action,

    onClose,

    refresh,

}) {

    async function remove() {

        if (!action) return;

        try {

            await deleteAction(action.gesture);

            toast.success("Mapping deleted");

            refresh();

            onClose();

        }

        catch {

            toast.error("Unable to delete mapping");

        }

    }

    return (

        <Dialog
            open={Boolean(action)}
            onClose={onClose}
            maxWidth="xs"
            fullWidth
        >

            <DialogTitle>

                <Stack
                    direction="row"
                    spacing={1.5}
                    alignItems="center"
                >

                    <WarningAmberRoundedIcon
                        color="warning"
                    />

                    Delete Mapping

                </Stack>

            </DialogTitle>

            <DialogContent>

                <Typography
                    sx={{
                        mb: 2,
                    }}
                >
                    Are you sure you want to delete this
                    gesture mapping?
                </Typography>

                {action && (

                    <Stack
                        spacing={1}
                        sx={{
                            p: 2,
                            borderRadius: 2,
                            bgcolor: "rgba(255,255,255,.03)",
                            border:
                                "1px solid rgba(255,255,255,.08)",
                        }}
                    >

                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            Gesture
                        </Typography>

                        <Typography
                            fontWeight={700}
                        >
                            {action.gesture}
                        </Typography>

                        <Typography
                            variant="body2"
                            color="text.secondary"
                            mt={1}
                        >
                            Action
                        </Typography>

                        <Typography>
                            {action.action}
                        </Typography>

                    </Stack>

                )}

            </DialogContent>

            <DialogActions>

                <Button
                    onClick={onClose}
                >
                    Cancel
                </Button>

                <Button
                    color="error"
                    variant="contained"
                    onClick={remove}
                >
                    Delete
                </Button>

            </DialogActions>

        </Dialog>

    );

}