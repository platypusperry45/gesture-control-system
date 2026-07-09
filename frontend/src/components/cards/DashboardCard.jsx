import {
    Box,
    Divider,
    Stack,
    Typography,
} from "@mui/material";

import GlassCard from "../ui/GlassCard";

export default function DashboardCard({
    title,
    subtitle,
    children,
}) {
    return (
        <GlassCard
            sx={{
                height: "100%",
            }}
        >
            <Box
                sx={{
                    px: 3,
                    py: 2.5,
                }}
            >
                <Stack spacing={0.5}>
                    <Typography
                        variant="h6"
                        fontWeight={700}
                    >
                        {title}
                    </Typography>

                    {subtitle && (
                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            {subtitle}
                        </Typography>
                    )}
                </Stack>
            </Box>

            <Divider />

            <Box
                sx={{
                    p: 3,
                }}
            >
                {children}
            </Box>
        </GlassCard>
    );
}