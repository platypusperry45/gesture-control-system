import {
    Card,
    CardContent,
    Typography,
    Stack,
    Chip,
    IconButton,
} from "@mui/material";

import VisibilityIcon from "@mui/icons-material/Visibility";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import PanToolIcon from "@mui/icons-material/PanTool";

export default function GestureCard({
    gesture,
}) {

    return (

        <Card
            sx={{
                height: "100%",
                transition: ".25s",

                "&:hover": {
                    transform: "translateY(-6px)",
                },
            }}
        >
            <CardContent>

                <Stack
                    spacing={2}
                >

                    <PanToolIcon
                        color="primary"
                        sx={{
                            fontSize: 42,
                        }}
                    />

                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        {gesture.name}
                    </Typography>

                    <Typography
                        color="text.secondary"
                    >
                        {gesture.samples} Samples
                    </Typography>

                    <Chip
                        color="success"
                        label="Ready"
                    />

                    <Stack
                        direction="row"
                        justifyContent="space-between"
                    >

                        <IconButton>

                            <VisibilityIcon/>

                        </IconButton>

                        <IconButton>

                            <EditIcon/>

                        </IconButton>

                        <IconButton
                            color="error"
                        >

                            <DeleteIcon/>

                        </IconButton>

                    </Stack>

                </Stack>

            </CardContent>

        </Card>

    );

}