import {
    Grid,
    Stack,
    Typography,
    Chip,
    LinearProgress,
    Box,
} from "@mui/material";

import MemoryRoundedIcon from "@mui/icons-material/MemoryRounded";
import StorageRoundedIcon from "@mui/icons-material/StorageRounded";
import VideocamRoundedIcon from "@mui/icons-material/VideocamRounded";
import PsychologyRoundedIcon from "@mui/icons-material/PsychologyRounded";
import ScheduleRoundedIcon from "@mui/icons-material/ScheduleRounded";
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded";

import { motion } from "framer-motion";

import GlassCard from "../ui/GlassCard";

export default function SystemAnalytics() {

    const stats = [

        {
            title: "CPU Usage",
            value: "32%",
            progress: 32,
            icon: <MemoryRoundedIcon color="primary" />,
            color: "#3B82F6",
        },

        {
            title: "GPU Usage",
            value: "58%",
            progress: 58,
            icon: <PsychologyRoundedIcon color="secondary" />,
            color: "#8B5CF6",
        },

        {
            title: "Memory Usage",
            value: "4.8 GB / 16 GB",
            progress: 30,
            icon: <StorageRoundedIcon color="warning" />,
            color: "#F59E0B",
        },

        {
            title: "Camera",
            value: "Connected",
            chip: "ONLINE",
            icon: <VideocamRoundedIcon color="success" />,
        },

        {
            title: "Inference Engine",
            value: "Running",
            chip: "ACTIVE",
            icon: <CheckCircleRoundedIcon color="success" />,
        },

        {
            title: "Backend Uptime",
            value: "05h 42m",
            icon: <ScheduleRoundedIcon color="primary" />,
        },

    ];

    return (

        <Grid
            container
            spacing={3}
        >

            {

                stats.map((item, index) => (

                    <Grid
                        key={index}
                        size={{
                            xs:12,
                            sm:6,
                            lg:4,
                        }}
                    >

                        <motion.div

                            initial={{
                                opacity:0,
                                y:20,
                            }}

                            animate={{
                                opacity:1,
                                y:0,
                            }}

                            transition={{
                                delay:index*0.05,
                            }}

                        >

                            <GlassCard

                                sx={{

                                    p:3,

                                    height:180,

                                    display:"flex",

                                    flexDirection:"column",

                                    justifyContent:"space-between",

                                }}

                            >

                                <Stack

                                    direction="row"

                                    justifyContent="space-between"

                                    alignItems="center"

                                >

                                    {item.icon}

                                    {

                                        item.chip &&

                                        <Chip

                                            label={item.chip}

                                            color="success"

                                            size="small"

                                        />

                                    }

                                </Stack>

                                <Box>

                                    <Typography

                                        variant="body2"

                                        color="text.secondary"

                                    >

                                        {item.title}

                                    </Typography>

                                    <Typography

                                        variant="h5"

                                        fontWeight={700}

                                        mt={1}

                                    >

                                        {item.value}

                                    </Typography>

                                </Box>

                                {

                                    item.progress !== undefined &&

                                    <LinearProgress

                                        variant="determinate"

                                        value={item.progress}

                                        sx={{

                                            mt:2,

                                            height:8,

                                            borderRadius:10,

                                            background:"rgba(255,255,255,.08)",

                                            "& .MuiLinearProgress-bar":{

                                                background:item.color,

                                            },

                                        }}

                                    />

                                }

                            </GlassCard>

                        </motion.div>

                    </Grid>

                ))

            }

        </Grid>

    );

}