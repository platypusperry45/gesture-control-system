import {
    Box,
    Chip,
    Stack,
    Typography,
} from "@mui/material";

import VideocamIcon from "@mui/icons-material/Videocam";
import FiberManualRecordIcon from "@mui/icons-material/FiberManualRecord";

import GlassCard from "../ui/GlassCard";

export default function CameraCard() {
    return (
        <GlassCard
            sx={{
                p: 0,
                overflow: "hidden",
            }}
        >
            {/* Header */}

            <Stack
                direction="row"
                justifyContent="space-between"
                alignItems="center"
                sx={{
                    px: 3,
                    py: 2.2,
                    borderBottom:
                        "1px solid rgba(255,255,255,.06)",
                }}
            >
                <Stack
                    direction="row"
                    spacing={1.5}
                    alignItems="center"
                >
                    <VideocamIcon color="primary" />

                    <Box>
                        <Typography
                            variant="h6"
                            fontWeight={700}
                        >
                            Live Camera
                        </Typography>

                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            Real-time gesture detection
                        </Typography>
                    </Box>
                </Stack>

                <Chip
                    size="small"
                    icon={
                        <FiberManualRecordIcon
                            sx={{
                                fontSize: "12px !important",
                            }}
                        />
                    }
                    label="LIVE"
                    color="success"
                />
            </Stack>

            {/* Camera Feed */}

            <Box
                sx={{
                    bgcolor: "#05070D",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    p: 2,
                }}
            >
                <Box
                    component="img"
                    src="http://127.0.0.1:8000/video_feed"
                    alt="Live Camera"

                    sx={{
                        width: "100%",
                        borderRadius: 3,

                        aspectRatio: "16 / 9",

                        objectFit: "cover",

                        border:
                            "1px solid rgba(255,255,255,.06)",
                    }}
                />
            </Box>

            {/* Footer */}

            <Stack
                direction="row"
                justifyContent="space-between"
                sx={{
                    px: 3,
                    py: 2,
                    borderTop:
                        "1px solid rgba(255,255,255,.06)",
                }}
            >
                <Typography
                    variant="body2"
                    color="text.secondary"
                >
                    Camera Status
                </Typography>

                <Chip
                    label="Connected"
                    color="success"
                    size="small"
                />
            </Stack>
        </GlassCard>
    );
}