import {
    Box,
    Button,
    Card,
    CardContent,
    Chip,
    Divider,
    Stack,
    Typography,
} from "@mui/material";

import KeyboardIcon from "@mui/icons-material/Keyboard";
import MusicNoteIcon from "@mui/icons-material/MusicNote";
import LanguageIcon from "@mui/icons-material/Language";
import MouseIcon from "@mui/icons-material/Mouse";
import SettingsSuggestIcon from "@mui/icons-material/SettingsSuggest";

import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import BoltIcon from "@mui/icons-material/Bolt";

import { motion } from "framer-motion";

function getType(type) {

    switch (type) {

        case "Keyboard":
        case "Keyboard Shortcut":
            return {
                icon: <KeyboardIcon sx={{ fontSize: 42 }} />,
                color: "primary",
                gradient:
                    "linear-gradient(135deg,#6366F1,#8B5CF6)",
            };

        case "Media":
            return {
                icon: <MusicNoteIcon sx={{ fontSize: 42 }} />,
                color: "success",
                gradient:
                    "linear-gradient(135deg,#10B981,#14B8A6)",
            };

        case "Browser":
            return {
                icon: <LanguageIcon sx={{ fontSize: 42 }} />,
                color: "warning",
                gradient:
                    "linear-gradient(135deg,#F59E0B,#FB923C)",
            };

        case "Mouse":
            return {
                icon: <MouseIcon sx={{ fontSize: 42 }} />,
                color: "secondary",
                gradient:
                    "linear-gradient(135deg,#EC4899,#A855F7)",
            };

        default:
            return {
                icon: <SettingsSuggestIcon sx={{ fontSize: 42 }} />,
                color: "error",
                gradient:
                    "linear-gradient(135deg,#EF4444,#F43F5E)",
            };
    }
}

export default function ActionCard({
    gesture,
    mapping,
    onEdit,
    onDelete,
    onTest,
}) {

    const theme = getType(mapping.type);

    return (

        <Card
            component={motion.div}
            whileHover={{
                y: -6,
                scale: 1.015,
            }}
            transition={{
                duration: 0.25,
            }}
            sx={{
                height: "100%",
                display: "flex",
                flexDirection: "column",

                borderRadius: 5,

                background:
                    "rgba(20,24,35,.75)",

                backdropFilter:
                    "blur(18px)",

                border:
                    "1px solid rgba(255,255,255,.06)",

                overflow: "hidden",

                transition: ".3s",

                "&:hover": {
                    boxShadow:
                        "0 25px 60px rgba(91,140,255,.25)",
                },
            }}
        >

            <Box
                sx={{
                    height: 6,
                    background: theme.gradient,
                }}
            />

            <CardContent
                sx={{
                    flex: 1,
                    display: "flex",
                    flexDirection: "column",
                    p: 3,
                }}
            >

                <Stack
                    spacing={3}
                    sx={{
                        flex: 1,
                    }}
                >

                    <Stack
                        direction="row"
                        justifyContent="space-between"
                        alignItems="center"
                    >

                        <Box color="primary.main">
                            {theme.icon}
                        </Box>

                        <Chip
                            color={theme.color}
                            label={mapping.type}
                        />

                    </Stack>

                    <Box>

                        <Typography
                            variant="h5"
                            fontWeight={700}
                            textTransform="capitalize"
                        >
                            {gesture}
                        </Typography>

                        <Typography
                            mt={1}
                            color="text.secondary"
                        >
                            {mapping.action}
                        </Typography>

                    </Box>

                    <Stack
                        direction="row"
                        justifyContent="space-between"
                        alignItems="center"
                    >

                        <Chip
                            icon={<BoltIcon />}
                            color={
                                mapping.enabled
                                    ? "success"
                                    : "error"
                            }
                            label={
                                mapping.enabled
                                    ? "Enabled"
                                    : "Disabled"
                            }
                        />

                        <Typography
                            variant="caption"
                            color="text.secondary"
                        >
                            Desktop Automation
                        </Typography>

                    </Stack>

                    <Divider />

                    <Stack
                        direction="row"
                        spacing={1}
                    >

                        <Button
                            fullWidth
                            variant="outlined"
                            startIcon={<EditIcon />}
                            onClick={() => onEdit(gesture, mapping)}
                        >
                            Edit
                        </Button>

                        <Button
                            fullWidth
                            color="error"
                            variant="outlined"
                            startIcon={<DeleteIcon />}
                            onClick={() => onDelete(gesture, mapping)}
                        >
                            Delete
                        </Button>

                    </Stack>

                    <Button
                        fullWidth
                        variant="contained"
                        size="large"
                        startIcon={<PlayArrowIcon />}
                        onClick={() => onTest(gesture)}
                        sx={{
                            py: 1.2,
                            borderRadius: 3,
                            background: theme.gradient,
                            mt: "auto",
                        }}
                    >
                        Test Automation
                    </Button>

                </Stack>

            </CardContent>

        </Card>

    );
}