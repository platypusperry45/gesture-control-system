import Grid from "@mui/material/Grid";

import {
    Box,
    Chip,
    Stack,
    Typography,
} from "@mui/material";

import SpeedIcon from "@mui/icons-material/Speed";
import TimerIcon from "@mui/icons-material/Timer";
import MemoryIcon from "@mui/icons-material/Memory";

import { motion } from "framer-motion";

import CountUp from "react-countup";

import DashboardCard from "./DashboardCard";

export default function MetricsCard({ status }) {

    const fps = Number(status.fps || 0);

    return (

        <DashboardCard
            title="Performance"
            subtitle="Real-time AI Engine"
        >

            <Grid
                container
                spacing={2}
            >

                {/* FPS */}

                <Grid
                    size={6}
                >

                    <motion.div
                        whileHover={{
                            scale: 1.05,
                            rotate: 2,
                        }}
                    >

                        <Box
                            sx={{

                                p:2.5,

                                borderRadius:4,

                                background:
                                    "linear-gradient(135deg,#1E293B,#0F172A)",

                                border:
                                    "1px solid rgba(255,255,255,.06)",

                                textAlign:"center",

                            }}
                        >

                            <SpeedIcon
                                color="primary"
                                sx={{
                                    fontSize:38,
                                    mb:1,
                                }}
                            />

                            <Typography
                                variant="h4"
                                fontWeight={700}
                            >

                                {fps.toFixed(1)}

                            </Typography>

                            <Typography
                                color="text.secondary"
                            >
                                FPS
                            </Typography>

                            <Chip

                                size="small"

                                color="success"

                                label="LIVE"

                                sx={{
                                    mt:1,
                                }}

                            />

                        </Box>

                    </motion.div>

                </Grid>

                {/* Uptime */}

                <Grid
                    size={6}
                >

                    <motion.div
                        whileHover={{
                            scale:1.05,
                            rotate:-2,
                        }}
                    >

                        <Box
                            sx={{

                                p:2.5,

                                borderRadius:4,

                                background:
                                    "linear-gradient(135deg,#1E293B,#0F172A)",

                                border:
                                    "1px solid rgba(255,255,255,.06)",

                                textAlign:"center",

                            }}
                        >

                            <TimerIcon

                                color="primary"

                                sx={{
                                    fontSize:38,
                                    mb:1,
                                }}

                            />

                            <Typography

                                variant="h4"

                                fontWeight={700}

                            >

                                {status.uptime}


                            </Typography>

                            <Typography
                                color="text.secondary"
                            >
                                Seconds
                            </Typography>

                            <Chip

                                size="small"

                                color="primary"

                                label="Running"

                                sx={{
                                    mt:1,
                                }}

                            />

                        </Box>

                    </motion.div>

                </Grid>

            </Grid>

            <Stack

                direction="row"

                spacing={2}

                mt={3}

            >

                <MemoryIcon color="primary"/>

                <Typography
                    color="text.secondary"
                >

                    AI inference engine is operating normally.

                </Typography>

            </Stack>

        </DashboardCard>

    );

}