
import {
    Box,
    Chip,
    LinearProgress,
    Stack,
    Typography,
} from "@mui/material";

import PsychologyAltIcon from "@mui/icons-material/PsychologyAlt";
import BoltIcon from "@mui/icons-material/Bolt";

import { motion, AnimatePresence } from "framer-motion";

import DashboardCard from "./DashboardCard";

export default function PredictionCard({ status = {} }) {

    const confidence = Math.round((status?.confidence ?? 0) * 100);

    const glow =
        confidence > 90
            ? "0 0 35px rgba(34,197,94,.25)"
            : confidence > 60
            ? "0 0 30px rgba(250,204,21,.18)"
            : "none";

    return (

        <motion.div
            whileHover={{ y: -5 }}
            transition={{ duration: 0.25 }}
        >

            <DashboardCard
                title=""
                sx={{
                    boxShadow: glow,
                    transition: ".35s",
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
                        spacing={1.2}
                        alignItems="center"
                    >

                        <motion.div
                            animate={{
                                rotate: confidence > 0 ? 360 : 0,
                            }}
                            transition={{
                                duration: .6,
                            }}
                        >

                            <PsychologyAltIcon color="primary" />

                        </motion.div>

                        <Typography
                            variant="h6"
                            fontWeight={700}
                        >
                            AI Prediction
                        </Typography>

                    </Stack>

                    <Chip
                        size="small"
                        color={
                            confidence > 90
                                ? "success"
                                : confidence > 60
                                ? "warning"
                                : "default"
                        }
                        label={`${confidence}%`}
                    />

                </Stack>

                <Typography
                    variant="body2"
                    color="text.secondary"
                >
                    Current Gesture
                </Typography>

                <AnimatePresence mode="wait">

                    <motion.div
                        key={status?.prediction ?? "none"}
                        initial={{
                            opacity: 0,
                            y: 12,
                        }}
                        animate={{
                            opacity: 1,
                            y: 0,
                        }}
                        exit={{
                            opacity: 0,
                            y: -12,
                        }}
                        transition={{
                            duration: .25,
                        }}
                    >

                        <Typography
                            variant="h3"
                            sx={{
                                mt: .5,
                                mb: 3,
                                fontWeight: 800,
                                minHeight: 56,
                                textTransform: "capitalize",
                            }}
                        >

                            {status?.prediction ?? "--"}

                        </Typography>

                    </motion.div>

                </AnimatePresence>

                <Stack
                    direction="row"
                    justifyContent="space-between"
                    mb={1}
                >

                    <Typography
                        variant="body2"
                        color="text.secondary"
                    >
                        Confidence
                    </Typography>

                    <Typography fontWeight={700}>
                        {confidence}%
                    </Typography>

                </Stack>

                <motion.div
                    initial={{
                        width: 0,
                    }}
                    animate={{
                        width: "100%",
                    }}
                >

                    <LinearProgress
                        variant="determinate"
                        value={confidence}
                        sx={{
                            height: 10,
                            borderRadius: 10,

                            "& .MuiLinearProgress-bar": {
                                borderRadius: 10,
                                transition:
                                    "transform .45s ease",
                            },
                        }}
                    />

                </motion.div>

                <motion.div
                    whileHover={{
                        scale: 1.03,
                    }}
                >

                    <Box
                        sx={{
                            mt: 4,
                            p: 2.5,
                            borderRadius: 4,

                            background:
                                "linear-gradient(135deg,rgba(99,102,241,.14),rgba(79,70,229,.08))",

                            border:
                                "1px solid rgba(99,102,241,.18)",
                        }}
                    >

                        <Stack
                            direction="row"
                            spacing={1}
                            alignItems="center"
                            mb={1}
                        >

                            <BoltIcon
                                color="primary"
                                fontSize="small"
                            />

                            <Typography
                                variant="body2"
                                color="text.secondary"
                            >
                                Assigned Action
                            </Typography>

                        </Stack>

                        <AnimatePresence mode="wait">

                            <motion.div
                                key={status?.action ?? "none"}
                                initial={{
                                    opacity: 0,
                                    x: -10,
                                }}
                                animate={{
                                    opacity: 1,
                                    x: 0,
                                }}
                                exit={{
                                    opacity: 0,
                                }}
                            >

                                <Typography
                                    variant="h6"
                                    fontWeight={700}
                                >
                                    {status?.action ?? "--"}
                                </Typography>

                            </motion.div>

                        </AnimatePresence>

                    </Box>

                </motion.div>

            </DashboardCard>

        </motion.div>

    );

}