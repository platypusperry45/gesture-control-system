import { useEffect, useState } from "react";

import {
    AppBar,
    Avatar,
    Box,
    Chip,
    Toolbar,
    Typography,
} from "@mui/material";

import BoltIcon from "@mui/icons-material/Bolt";

export default function AppHeader() {

    const [time, setTime] = useState(
        new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
        })
    );

    useEffect(() => {
        const timer = setInterval(() => {
            setTime(
                new Date().toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                })
            );
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    return (
        <AppBar
            position="fixed"
            elevation={0}
        >
            <Toolbar
                sx={{
                    minHeight: 72,
                    px: 4,
                }}
            >
                {/* Logo */}

                <Box
                    sx={{
                        display: "flex",
                        alignItems: "center",
                        gap: 2,
                        flexGrow: 1,
                    }}
                >
                    <Box
                        sx={{
                            width: 46,
                            height: 46,
                            borderRadius: 3,

                            display: "flex",
                            alignItems: "center",
                            justifyContent: "center",

                            background:
                                "linear-gradient(135deg,#6366F1,#8B5CF6)",

                            boxShadow:
                                "0 8px 24px rgba(99,102,241,.35)",
                        }}
                    >
                        <BoltIcon
                            sx={{
                                color: "#fff",
                                fontSize: 24,
                            }}
                        />
                    </Box>

                    <Box>
                        <Typography
                            variant="h6"
                            sx={{
                                fontWeight: 700,
                                lineHeight: 1.1,
                            }}
                        >
                            Gesture AI
                        </Typography>

                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            Real-time Desktop Control
                        </Typography>
                    </Box>
                </Box>

                {/* Status */}

                <Chip
                    label="Connected"
                    color="success"
                    size="small"
                    sx={{
                        mr: 2,
                        fontWeight: 600,
                    }}
                />

                {/* Clock */}

                <Typography
                    color="text.secondary"
                    sx={{
                        mr: 3,
                        fontWeight: 500,
                    }}
                >
                    {time}
                </Typography>

                {/* Avatar */}

                <Avatar
                    sx={{
                        bgcolor: "primary.main",
                        fontWeight: 600,
                    }}
                >
                    A
                </Avatar>
            </Toolbar>
        </AppBar>
    );
}