import { Box, Stack, Typography } from "@mui/material";

import GlassCard from "../ui/GlassCard";

export default function DashboardCard({
    title,
    subtitle,
    action,
    children,
    height = "100%",
    sx = {},
}) {
    return (
        <GlassCard
            sx={{
                height,
                p: 3,
                display: "flex",
                flexDirection: "column",
                ...sx,
            }}
        >
            {(title || subtitle || action) && (
                <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="flex-start"
                    sx={{
                        mb: 3,
                    }}
                >
                    <Box>
                        {title && (
                            <Typography
                                variant="h6"
                                sx={{
                                    fontWeight: 700,
                                    lineHeight: 1.2,
                                }}
                            >
                                {title}
                            </Typography>
                        )}

                        {subtitle && (
                            <Typography
                                variant="body2"
                                color="text.secondary"
                                sx={{ mt: 0.5 }}
                            >
                                {subtitle}
                            </Typography>
                        )}
                    </Box>

                    {action}
                </Stack>
            )}

            <Box
                sx={{
                    flexGrow: 1,
                    display: "flex",
                    flexDirection: "column",
                }}
            >
                {children}
            </Box>
        </GlassCard>
    );
}