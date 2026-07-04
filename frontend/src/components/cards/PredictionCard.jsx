
import {
    Box,
    Chip,
    LinearProgress,
    Stack,
    Typography,
} from "@mui/material";

import PsychologyAltIcon from "@mui/icons-material/PsychologyAlt";
import BoltIcon from "@mui/icons-material/Bolt";

import DashboardCard from "./DashboardCard";

export default function PredictionCard({ status }) {

    const confidence = Math.round((status.confidence || 0) * 100);

    return (
        <DashboardCard title="">
            <Stack
                direction="row"
                justifyContent="space-between"
                alignItems="center"
                mb={3}
            >
                <Stack direction="row" spacing={1.2} alignItems="center">
                    <PsychologyAltIcon color="primary" />

                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        AI Prediction
                    </Typography>
                </Stack>

                <Chip
                    size="small"
                    color={confidence > 80 ? "success" : "warning"}
                    label={`${confidence}%`}
                />
            </Stack>

            <Typography
                variant="body2"
                color="text.secondary"
            >
                Current Gesture
            </Typography>

            <Typography
                variant="h3"
                sx={{
                    mt: 0.5,
                    mb: 3,
                    fontWeight: 700,
                    minHeight: 54,
                }}
            >
                {status.prediction ?? "--"}
            </Typography>

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

                <Typography
                    fontWeight={600}
                >
                    {confidence}%
                </Typography>
            </Stack>

            <LinearProgress
                variant="determinate"
                value={confidence}
                sx={{
                    height: 8,
                    borderRadius: 5,

                    "& .MuiLinearProgress-bar": {
                        borderRadius: 5,
                    },
                }}
            />

            <Box
                sx={{
                    mt: 4,
                    p: 2.2,
                    borderRadius: 3,
                    bgcolor: "rgba(99,102,241,.08)",
                    border: "1px solid rgba(99,102,241,.18)",
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

                <Typography
                    variant="h6"
                    fontWeight={600}
                >
                    {status.action ?? "--"}
                </Typography>
            </Box>
        </DashboardCard>
    );
}

    