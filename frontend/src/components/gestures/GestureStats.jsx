import { Grid, Stack, Typography } from "@mui/material";
import { motion } from "framer-motion";

import PanToolAltRoundedIcon from "@mui/icons-material/PanToolAltRounded";
import ImageRoundedIcon from "@mui/icons-material/ImageRounded";
import PsychologyRoundedIcon from "@mui/icons-material/PsychologyRounded";
import AutoGraphRoundedIcon from "@mui/icons-material/AutoGraphRounded";

import GlassCard from "../ui/GlassCard";

const MotionCard = motion.create(GlassCard);

function StatCard({
    icon,
    title,
    value,
    color,
    delay = 0,
}) {
    return (
        <MotionCard
            initial={{
                opacity: 0,
                y: 25,
            }}
            animate={{
                opacity: 1,
                y: 0,
            }}
            transition={{
                duration: .45,
                delay,
            }}
            sx={{
                p: 3,
                height: "100%",
                transition: ".3s",

                "&:hover": {
                    transform: "translateY(-6px)",
                    boxShadow: `0 20px 60px ${color}33`,
                },
            }}
        >
            <Stack spacing={2}>
                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                >
                    <Stack
                        sx={{
                            width: 54,
                            height: 54,
                            borderRadius: "16px",
                            bgcolor: `${color}20`,
                            color,
                            justifyContent: "center",
                            alignItems: "center",
                        }}
                    >
                        {icon}
                    </Stack>

                    <Typography
                        variant="caption"
                        color="text.secondary"
                    >
                        LIVE
                    </Typography>
                </Stack>

                <Typography
                    color="text.secondary"
                    variant="body2"
                >
                    {title}
                </Typography>

                <Typography
                    variant="h4"
                    fontWeight={700}
                >
                    {value}
                </Typography>
            </Stack>
        </MotionCard>
    );
}

export default function GestureStats({

    totalGestures,

    totalImages,

    currentGesture,

    averageAccuracy,

}) {

    return (

        <Grid
            container
            spacing={3}
            mb={4}
        >

            <Grid
                size={{
                    xs:12,
                    md:6,
                    lg:3,
                }}
            >
                <StatCard
                    delay={0}
                    color="#6366F1"
                    icon={<PanToolAltRoundedIcon />}
                    title="Total Gestures"
                    value={totalGestures}
                />
            </Grid>

            <Grid
                size={{
                    xs:12,
                    md:6,
                    lg:3,
                }}
            >
                <StatCard
                    delay={.1}
                    color="#06B6D4"
                    icon={<ImageRoundedIcon />}
                    title="Dataset Images"
                    value={totalImages}
                />
            </Grid>

            <Grid
                size={{
                    xs:12,
                    md:6,
                    lg:3,
                }}
            >
                <StatCard
                    delay={.2}
                    color="#22C55E"
                    icon={<PsychologyRoundedIcon />}
                    title="Current Prediction"
                    value={currentGesture || "--"}
                />
            </Grid>

            <Grid
                size={{
                    xs:12,
                    md:6,
                    lg:3,
                }}
            >
                <StatCard
                    delay={.3}
                    color="#F59E0B"
                    icon={<AutoGraphRoundedIcon />}
                    title="Average Accuracy"
                    value={`${averageAccuracy}%`}
                />
            </Grid>

        </Grid>

    );

}