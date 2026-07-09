import {
    Grid,
    Stack,
    Typography,
} from "@mui/material";

import PsychologyRoundedIcon from "@mui/icons-material/PsychologyRounded";
import SpeedRoundedIcon from "@mui/icons-material/SpeedRounded";
import TimelineRoundedIcon from "@mui/icons-material/TimelineRounded";
import CheckCircleRoundedIcon from "@mui/icons-material/CheckCircleRounded";

import { motion } from "framer-motion";

import GlassCard from "../ui/GlassCard";

export default function AnalyticsOverview() {

    const cards = [

        {
            title: "Total Predictions",
            value: "18,426",
            subtitle: "Since startup",
            icon: <PsychologyRoundedIcon color="primary" />,
        },

        {
            title: "Average Accuracy",
            value: "97.82%",
            subtitle: "Last 500 predictions",
            icon: <CheckCircleRoundedIcon color="success" />,
        },

        {
            title: "Average FPS",
            value: "29.8",
            subtitle: "Live inference speed",
            icon: <SpeedRoundedIcon color="warning" />,
        },

        {
            title: "Average Confidence",
            value: "96.1%",
            subtitle: "Prediction confidence",
            icon: <TimelineRoundedIcon color="secondary" />,
        },

    ];

    return (

        <Grid
            container
            spacing={3}
        >

            {

                cards.map((card, index) => (

                    <Grid
                        key={index}
                        size={{
                            xs:12,
                            sm:6,
                            lg:3,
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
                                delay:index*0.08,
                            }}

                        >

                            <GlassCard

                                sx={{

                                    p:3,

                                    height:170,

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

                                    {card.icon}

                                    <Typography

                                        variant="body2"

                                        color="text.secondary"

                                    >

                                        {card.subtitle}

                                    </Typography>

                                </Stack>

                                <div>

                                    <Typography

                                        variant="body2"

                                        color="text.secondary"

                                        gutterBottom

                                    >

                                        {card.title}

                                    </Typography>

                                    <Typography

                                        variant="h3"

                                        fontWeight={800}

                                    >

                                        {card.value}

                                    </Typography>

                                </div>

                            </GlassCard>

                        </motion.div>

                    </Grid>

                ))

            }

        </Grid>

    );

}