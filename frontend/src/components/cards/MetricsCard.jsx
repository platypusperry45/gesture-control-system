import Grid from "@mui/material/Grid";

import SpeedIcon from "@mui/icons-material/Speed";
import TimerIcon from "@mui/icons-material/Timer";

import DashboardCard from "./DashboardCard";
import MetricTile from "../ui/MetricTile";

export default function MetricsCard({ status }) {
    return (
        <DashboardCard
            title="Performance"
            subtitle="Real-time system metrics"
        >
            <Grid container spacing={2}>
                <Grid size={6}>
                    <MetricTile
                        icon={<SpeedIcon color="primary" />}
                        label="FPS"
                        value={status.fps || "--"}
                    />
                </Grid>

                <Grid size={6}>
                    <MetricTile
                        icon={<TimerIcon color="primary" />}
                        label="Uptime"
                        value={status.uptime}
                    />
                </Grid>
            </Grid>
        </DashboardCard>
    );
}