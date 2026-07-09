import {
    Box,
    Stack,
    Typography,
    LinearProgress,
    Chip,
    Divider,
    CircularProgress,
} from "@mui/material";

import TrendingUpRoundedIcon from "@mui/icons-material/TrendingUpRounded";
import SpeedRoundedIcon from "@mui/icons-material/SpeedRounded";
import MemoryRoundedIcon from "@mui/icons-material/MemoryRounded";
import TimerRoundedIcon from "@mui/icons-material/TimerRounded";

import { motion } from "framer-motion";

import GlassCard from "../ui/GlassCard";

export default function TrainingProgress({

    progress = 0,

    epoch = 0,

    totalEpochs = 20,

    accuracy = 0,

    loss = 0,

    eta = "--",

    gpu = "Available",

    status = "Idle",

}) {

    const running = status === "Training";

    return (

        <motion.div

            initial={{
                opacity: 0,
                y: 20,
            }}

            animate={{
                opacity: 1,
                y: 0,
            }}

            transition={{
                duration: 0.4,
            }}

        >

            <GlassCard
                sx={{
                    p: 3,
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

                        Training Progress

                    </Typography>

                    <Chip

                        label={status}

                        color={running ? "success" : "default"}

                    />

                </Stack>

                <Divider sx={{ mb: 4 }} />

                <Stack

                    direction={{
                        xs: "column",
                        md: "row",
                    }}

                    spacing={5}

                    alignItems="center"

                >

                    <Box

                        sx={{

                            position: "relative",

                            display: "inline-flex",

                        }}

                    >

                        <CircularProgress

                            variant="determinate"

                            value={progress}

                            size={150}

                            thickness={5}

                        />

                        <Box

                            sx={{

                                position: "absolute",

                                inset: 0,

                                display: "flex",

                                justifyContent: "center",

                                alignItems: "center",

                            }}

                        >

                            <Typography

                                variant="h4"

                                fontWeight={700}

                            >

                                {Math.round(progress)}%

                            </Typography>

                        </Box>

                    </Box>

                    <Box

                        flex={1}

                        width="100%"

                    >

                        <Stack

                            direction="row"

                            justifyContent="space-between"

                            mb={1}

                        >

                            <Typography>

                                Epoch

                            </Typography>

                            <Typography

                                fontWeight={700}

                            >

                                {epoch} / {totalEpochs}

                            </Typography>

                        </Stack>

                        <LinearProgress

                            variant="determinate"

                            value={
                                totalEpochs
                                    ? (epoch / totalEpochs) * 100
                                    : 0
                            }

                            sx={{

                                height: 10,

                                borderRadius: 5,

                            }}

                        />

                        <Typography

                            mt={2}

                            color="text.secondary"

                        >

                            Live training progress updates from the backend.

                        </Typography>

                    </Box>

                </Stack>

                <Divider sx={{ my: 4 }} />

                <Stack

                    direction={{
                        xs: "column",
                        sm: "row",
                    }}

                    spacing={2}

                >

                    <Metric

                        icon={<TrendingUpRoundedIcon color="primary" />}

                        label="Accuracy"

                        value={`${Number(accuracy).toFixed(2)} %`}

                    />

                    <Metric

                        icon={<SpeedRoundedIcon color="error" />}

                        label="Loss"

                        value={Number(loss).toFixed(4)}

                    />

                    <Metric

                        icon={<TimerRoundedIcon color="warning" />}

                        label="ETA"

                        value={eta}

                    />

                    <Metric

                        icon={<MemoryRoundedIcon color="success" />}

                        label="GPU"

                        value={gpu}

                    />

                </Stack>

            </GlassCard>

        </motion.div>

    );

}

function Metric({

    icon,

    label,

    value,

}) {

    return (

        <Box

            sx={{

                flex: 1,

                p: 2,

                borderRadius: 3,

                background: "rgba(99,102,241,.08)",

                border: "1px solid rgba(255,255,255,.08)",

            }}

        >

            <Stack

                direction="row"

                spacing={1}

                alignItems="center"

                mb={1}

            >

                {icon}

                <Typography

                    variant="body2"

                    color="text.secondary"

                >

                    {label}

                </Typography>

            </Stack>

            <Typography

                variant="h6"

                fontWeight={700}

            >

                {value}

            </Typography>

        </Box>

    );

}