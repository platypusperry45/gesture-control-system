import { Stack } from "@mui/material";

import DashboardCard from "./DashboardCard";
import StatusBadge from "../ui/StatusBadge";

export default function StatusCard({ status }) {
    return (
        <DashboardCard
            title="System Status"
            subtitle="Live backend health"
        >
            <Stack spacing={2}>
                <StatusBadge
                    status={status.camera ? "online" : "offline"}
                    label={status.camera ? "Camera Online" : "Camera Offline"}
                />

                <StatusBadge
                    status={status.model_loaded ? "healthy" : "offline"}
                    label={status.model_loaded ? "Model Loaded" : "Model Missing"}
                />

                <StatusBadge
                    status={status.inference_running ? "running" : "stopped"}
                    label={status.inference_running ? "Inference Running" : "Inference Stopped"}
                />
            </Stack>
        </DashboardCard>
    );
}