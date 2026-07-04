import {
    Stack,
    Typography,
} from "@mui/material";

import GlassCard from "./GlassCard";

export default function MetricTile({
    icon,
    label,
    value,
}) {
    return (
        <GlassCard
            sx={{
                p: 2.5,
                height: "100%",
            }}
        >
            <Stack spacing={1}>
                {icon}

                <Typography
                    variant="body2"
                    color="text.secondary"
                >
                    {label}
                </Typography>

                <Typography
                    variant="h4"
                    fontWeight={700}
                >
                    {value}
                </Typography>
            </Stack>
        </GlassCard>
    );
}