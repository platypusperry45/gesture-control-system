import { useEffect, useRef } from "react";

import {
    Box,
    Typography,
    Stack,
    Chip,
} from "@mui/material";

import TerminalRoundedIcon from "@mui/icons-material/TerminalRounded";

import GlassCard from "../ui/GlassCard";

export default function TrainingLogs({

    logs = [],

}) {

    const containerRef = useRef(null);

    useEffect(() => {

        if (containerRef.current) {

            containerRef.current.scrollTop =
                containerRef.current.scrollHeight;

        }

    }, [logs]);

    return (

        <GlassCard
            sx={{
                p: 3,
                height: 520,
                display: "flex",
                flexDirection: "column",
            }}
        >

            <Stack
                direction="row"
                justifyContent="space-between"
                alignItems="center"
                mb={3}
            >

                <Stack
                    direction="row"
                    spacing={1}
                    alignItems="center"
                >

                    <TerminalRoundedIcon color="primary" />

                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        Training Console
                    </Typography>

                </Stack>

                <Chip
                    color="success"
                    label="LIVE"
                />

            </Stack>

            <Box

                ref={containerRef}

                sx={{

                    flex: 1,

                    overflowY: "auto",

                    borderRadius: 3,

                    bgcolor: "#05070F",

                    p: 2,

                    fontFamily: "Consolas, monospace",

                    fontSize: 14,

                    border: "1px solid rgba(255,255,255,.08)",

                }}

            >

                {logs.length === 0 ? (

                    <Typography
                        color="#8b95b3"
                    >
                        Waiting for training...
                    </Typography>

                ) : (

                    logs.map((log, index) => (

                        <Typography

                            key={index}

                            sx={{

                                color: "#65ff8b",

                                mb: .7,

                                fontFamily: "Consolas",

                                wordBreak: "break-word",

                            }}

                        >

                            {log}

                        </Typography>

                    ))

                )}

            </Box>

        </GlassCard>

    );

}