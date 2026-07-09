import {
    Box,
    Chip,
    Stack,
    Typography,
    Fade,
} from "@mui/material";

import VideocamIcon from "@mui/icons-material/Videocam";
import FiberManualRecordIcon from "@mui/icons-material/FiberManualRecord";

import { motion } from "framer-motion";

import GlassCard from "../ui/GlassCard";

export default function CameraCard() {

    return (

        <GlassCard
            sx={{
                p: 0,
                overflow: "auto",
            }}
        >

            {/* ---------------- Header ---------------- */}

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
                    color="success"
                    size="small"
                    label="LIVE"
                    icon={
                        <FiberManualRecordIcon
                            sx={{
                                fontSize: 12,
                                animation:
                                    "pulse 1.4s infinite",
                            }}
                        />
                    }
                />

            </Stack>

            {/* ---------------- Camera ---------------- */}

            <Box
                sx={{
                    p: 2,
                    bgcolor: "#05070D",
                }}
            >

                <Fade in timeout={600}>

                    <motion.div
                        whileHover={{
                            scale: 1.01,
                        }}
                        transition={{
                            duration: .25,
                        }}
                    >

                        <Box
                            component="img"
                            src="http://127.0.0.1:8000/video_feed"
                            alt="Camera Feed"
                            sx={{
                                width: "100%",
                                aspectRatio: "16/9",
                                objectFit: "cover",

                                borderRadius: 4,

                                border:
                                    "1px solid rgba(255,255,255,.08)",

                                boxShadow:
                                    "0 25px 70px rgba(0,0,0,.45)",

                                transition:
                                    ".35s",
                            }}
                        />

                    </motion.div>

                </Fade>

            </Box>

            {/* ---------------- Footer ---------------- */}

            <Stack
                direction="row"
                justifyContent="space-between"
                alignItems="center"
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
                    color="success"
                    size="small"
                    label="Connected"
                />

            </Stack>

        </GlassCard>

    );

}