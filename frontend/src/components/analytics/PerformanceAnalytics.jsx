import { useMemo } from "react";

import {
    Box,
    Stack,
    Typography,
    Chip,
} from "@mui/material";

import SpeedRoundedIcon from "@mui/icons-material/SpeedRounded";

import {
    ResponsiveContainer,
    AreaChart,
    Area,
    LineChart,
    Line,
    CartesianGrid,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";

import GlassCard from "../ui/GlassCard";

export default function PerformanceAnalytics() {

    const fpsData = useMemo(() => (

        Array.from({ length: 20 }, (_, i) => ({

            frame: i + 1,

            fps: 28 + Math.random() * 3,

        }))

    ), []);

    const latencyData = useMemo(() => (

        Array.from({ length: 20 }, (_, i) => ({

            frame: i + 1,

            latency: 18 + Math.random() * 8,

        }))

    ), []);

    return (

        <Stack spacing={3}>

            {/* FPS History */}

            <GlassCard
                sx={{
                    p:3,
                    minHeight:420,
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

                        <SpeedRoundedIcon color="primary"/>

                        <Typography
                            variant="h6"
                            fontWeight={700}
                        >
                            FPS History
                        </Typography>

                    </Stack>

                    <Chip
                        label="Realtime"
                        color="success"
                    />

                </Stack>

                <Box sx={{ height:300 }}>

                    <ResponsiveContainer
                        width="100%"
                        height="100%"
                    >

                        <AreaChart
                            data={fpsData}
                        >

                            <CartesianGrid strokeDasharray="4 4"/>

                            <XAxis dataKey="frame"/>

                            <YAxis domain={[25,32]}/>

                            <Tooltip/>

                            <Area

                                type="monotone"

                                dataKey="fps"

                                stroke="#3B82F6"

                                fill="#3B82F6"

                                fillOpacity={0.25}

                                strokeWidth={3}

                            />

                        </AreaChart>

                    </ResponsiveContainer>

                </Box>

            </GlassCard>

            {/* Inference Latency */}

            <GlassCard
                sx={{
                    p:3,
                    minHeight:420,
                }}
            >

                <Stack

                    direction="row"

                    justifyContent="space-between"

                    alignItems="center"

                    mb={3}

                >

                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        Inference Latency
                    </Typography>

                    <Chip
                        label="ms"
                        color="warning"
                    />

                </Stack>

                <Box sx={{ height:300 }}>

                    <ResponsiveContainer
                        width="100%"
                        height="100%"
                    >

                        <LineChart
                            data={latencyData}
                        >

                            <CartesianGrid strokeDasharray="4 4"/>

                            <XAxis dataKey="frame"/>

                            <YAxis/>

                            <Tooltip/>

                            <Line

                                type="monotone"

                                dataKey="latency"

                                stroke="#F59E0B"

                                strokeWidth={3}

                                dot={false}

                            />

                        </LineChart>

                    </ResponsiveContainer>

                </Box>

            </GlassCard>

        </Stack>

    );

}