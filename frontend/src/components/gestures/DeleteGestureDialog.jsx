import {

    Dialog,

    DialogTitle,

    DialogContent,

    DialogActions,

    Button,

    Typography,

} from "@mui/material";

import toast from "react-hot-toast";

import { deleteGesture } from "../../services/gestureService";

export default function DeleteGestureDialog({

    gesture,

    onClose,

    refresh,

}) {

    const loading = false;

    async function remove() {

        if (!gesture) return;

        try {

            await deleteGesture(

                gesture.name

            );

            toast.success(

                "Gesture deleted."

            );

            refresh();

            onClose();

        }

        catch (err) {

            toast.error(

                err.response?.data?.detail ||

                "Delete failed."

            );

        }

    }

    return (

        <Dialog

            open={Boolean(gesture)}

            onClose={onClose}

            fullWidth

            maxWidth="xs"

        >

            <DialogTitle>

                Delete Gesture

            </DialogTitle>

            <DialogContent>

                <Typography>

                    Are you sure you want to permanently delete

                    <strong>

                        {" "}

                        {gesture?.name}

                    </strong>

                    ?

                </Typography>

            </DialogContent>

            <DialogActions>

                <Button

                    onClick={onClose}

                    disabled={loading}

                >

                    Cancel

                </Button>

                <Button

                    color="error"

                    variant="contained"

                    onClick={remove}

                    disabled={loading}

                >

                    Delete

                </Button>

            </DialogActions>

        </Dialog>

    );

}