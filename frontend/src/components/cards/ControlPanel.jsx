import { Stack } from "@mui/material";

import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import StopIcon from "@mui/icons-material/Stop";
import ModelTrainingIcon from "@mui/icons-material/ModelTraining";

import DashboardCard from "./DashboardCard";
import GradientButton from "../ui/GradientButton";

export default function ControlPanel() {
    return (
        <DashboardCard
            title="Controls"
            subtitle="System operations"
        >
            <Stack spacing={2}>
                <GradientButton
                    fullWidth
                    startIcon={<PlayArrowIcon />}
                >
                    Start Inference
                </GradientButton>

                <GradientButton
                    fullWidth
                    color="inherit"
                    startIcon={<StopIcon />}
                    sx={{
                        background: "#1E293B",
                        boxShadow: "none",

                        "&:hover": {
                            background: "#334155",
                        },
                    }}
                >
                    Stop
                </GradientButton>

                <GradientButton
                    fullWidth
                    startIcon={<ModelTrainingIcon />}
                    sx={{
                        background:
                            "linear-gradient(135deg,#0EA5E9,#2563EB)",
                    }}
                >
                    Retrain Model
                </GradientButton>
            </Stack>
        </DashboardCard>
    );
}