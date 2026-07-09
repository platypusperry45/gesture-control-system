import { useEffect, useState } from "react";

import {
    Box,
    Typography,
    Stack,
    Chip,
} from "@mui/material";

import TrendingUpRoundedIcon from "@mui/icons-material/TrendingUpRounded";
import TrendingDownRoundedIcon from "@mui/icons-material/TrendingDownRounded";
import BarChartRoundedIcon from "@mui/icons-material/BarChartRounded";

import {
    ResponsiveContainer,
    LineChart,
    Line,
    CartesianGrid,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";

import GlassCard from "../ui/GlassCard";

export default function TrainingCharts({

    epoch = 0,

    accuracy = 0,

    valAccuracy = 0,

    loss = 0,

    valLoss = 0,

}) {

    const [history, setHistory] = useState([]);

    useEffect(() => {

        if (!epoch) return;

        setHistory((previous) => [

            ...previous,

            {

                epoch,

                accuracy,

                valAccuracy,

                loss,

                valLoss,

            },

        ]);

    }, [

        epoch,

        accuracy,

        valAccuracy,

        loss,

        valLoss,

    ]);

    return (

        <Box>

            <Typography
                variant="h5"
                fontWeight={700}
                mb={3}
            >
                Training Curves
            </Typography>

            <Box

                sx={{

                    display: "flex",

                    gap: 3,

                    flexWrap: "wrap",

                }}

            >

                <GlassCard

                    sx={{

                        flex: "1 1 500px",

                        p: 3,

                        minHeight: 430,

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

                            <TrendingUpRoundedIcon color="primary" />

                            <Typography
                                variant="h6"
                                fontWeight={700}
                            >
                                Accuracy
                            </Typography>

                        </Stack>

                        <Chip
                            color="success"
                            label="LIVE"
                        />

                    </Stack>

                    <Box

                        sx={{

                            width: "100%",

                            height: 320,

                        }}

                    >

                        <ResponsiveContainer
                            width="100%"
                            height="100%"
                        >

                            <LineChart
                                data={history}
                            >

                                <CartesianGrid strokeDasharray="4 4" />

                                <XAxis dataKey="epoch" />

                                <YAxis domain={[0, 100]} />

                                <Tooltip />

                                <Line

                                    dataKey="accuracy"

                                    stroke="#6366F1"

                                    strokeWidth={3}

                                    dot={false}

                                />

                                <Line

                                    dataKey="valAccuracy"

                                    stroke="#10B981"

                                    strokeWidth={3}

                                    dot={false}

                                />

                            </LineChart>

                        </ResponsiveContainer>

                    </Box>

                </GlassCard>

                <GlassCard

                    sx={{

                        flex: "1 1 500px",

                        p: 3,

                        minHeight: 430,

                    }}

                >

                    <Stack

                        direction="row"

                        spacing={1}

                        alignItems="center"

                        mb={3}

                    >

                        <TrendingDownRoundedIcon color="error" />

                        <Typography
                            variant="h6"
                            fontWeight={700}
                        >
                            Loss
                        </Typography>

                    </Stack>

                    <Box

                        sx={{

                            width: "100%",

                            height: 320,

                        }}

                    >

                        <ResponsiveContainer
                            width="100%"
                            height="100%"
                        >

                            <LineChart
                                data={history}
                            >

                                <CartesianGrid strokeDasharray="4 4" />

                                <XAxis dataKey="epoch" />

                                <YAxis />

                                <Tooltip />

                                <Line

                                    dataKey="loss"

                                    stroke="#EF4444"

                                    strokeWidth={3}

                                    dot={false}

                                />

                                <Line

                                    dataKey="valLoss"

                                    stroke="#F59E0B"

                                    strokeWidth={3}

                                    dot={false}

                                />

                            </LineChart>

                        </ResponsiveContainer>

                    </Box>

                </GlassCard>

            </Box>

            <GlassCard

                sx={{

                    mt: 3,

                    p: 3,

                }}

            >

                <Stack

                    direction="row"

                    spacing={1}

                    alignItems="center"

                    mb={3}

                >

                    <BarChartRoundedIcon color="primary" />

                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        Current Metrics
                    </Typography>

                </Stack>

                <Box

                    sx={{

                        display: "grid",

                        gridTemplateColumns:
                            "repeat(auto-fit,minmax(180px,1fr))",

                        gap: 3,

                    }}

                >

                    <Metric

                        title="Accuracy"

                        value={`${accuracy.toFixed(2)} %`}

                    />

                    <Metric

                        title="Validation Accuracy"

                        value={`${valAccuracy.toFixed(2)} %`}

                    />

                    <Metric

                        title="Loss"

                        value={loss.toFixed(4)}

                    />

                    <Metric

                        title="Epoch"

                        value={epoch}

                    />

                </Box>

            </GlassCard>

        </Box>

    );

}

function Metric({

    title,

    value,

}) {

    return (

        <Box>

            <Typography

                color="text.secondary"

                variant="body2"

            >

                {title}

            </Typography>

            <Typography

                variant="h4"

                fontWeight={700}

                mt={1}

            >

                {value}

            </Typography>

        </Box>

    );

}