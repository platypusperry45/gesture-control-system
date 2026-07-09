import { useMemo } from "react";

import {
    Box,
    Stack,
    Typography,
    Chip,
} from "@mui/material";

import AnalyticsRoundedIcon from "@mui/icons-material/AnalyticsRounded";

import {
    ResponsiveContainer,
    BarChart,
    Bar,
    LineChart,
    Line,
    CartesianGrid,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";

import GlassCard from "../ui/GlassCard";

export default function PredictionAnalytics() {

    const gestureData = useMemo(() => ([
        { name: "Open", value: 624 },
        { name: "Fist", value: 548 },
        { name: "Peace", value: 493 },
        { name: "Thumb", value: 412 },
        { name: "Point", value: 331 },
        { name: "Okay", value: 287 },
    ]), []);

    const confidenceData = useMemo(() => (

        Array.from({ length: 20 }, (_, i) => ({
            frame: i + 1,
            confidence: 88 + Math.random() * 10,
        }))

    ), []);

    return (

        <Stack spacing={3}>

            {/* Prediction Distribution */}

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

                        <AnalyticsRoundedIcon color="primary"/>

                        <Typography
                            variant="h6"
                            fontWeight={700}
                        >
                            Prediction Distribution
                        </Typography>

                    </Stack>

                    <Chip
                        label="Live"
                        color="success"
                    />

                </Stack>

                <Box
                    sx={{
                        height:300,
                    }}
                >

                    <ResponsiveContainer
                        width="100%"
                        height="100%"
                    >

                        <BarChart
                            data={gestureData}
                        >

                            <CartesianGrid strokeDasharray="4 4"/>

                            <XAxis dataKey="name"/>

                            <YAxis/>

                            <Tooltip/>

                            <Bar
                                dataKey="value"
                                radius={[8,8,0,0]}
                                fill="#6366F1"
                            />

                        </BarChart>

                    </ResponsiveContainer>

                </Box>

            </GlassCard>

            {/* Confidence Trend */}

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
                        Confidence Trend
                    </Typography>

                    <Chip
                        label="Realtime"
                        color="primary"
                    />

                </Stack>

                <Box
                    sx={{
                        height:300,
                    }}
                >

                    <ResponsiveContainer
                        width="100%"
                        height="100%"
                    >

                        <LineChart
                            data={confidenceData}
                        >

                            <CartesianGrid strokeDasharray="4 4"/>

                            <XAxis dataKey="frame"/>

                            <YAxis
                                domain={[80,100]}
                            />

                            <Tooltip/>

                            <Line

                                type="monotone"

                                dataKey="confidence"

                                stroke="#22C55E"

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