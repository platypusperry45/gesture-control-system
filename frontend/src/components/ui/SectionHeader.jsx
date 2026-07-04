import { Box, Typography } from "@mui/material";

export default function SectionHeader({
    title,
    subtitle,
    action,
}) {
    return (
        <Box
            sx={{
                mb: 4,
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                flexWrap: "wrap",
                gap: 2,
            }}
        >
            <Box>
                <Typography
                    variant="h4"
                    sx={{
                        fontWeight: 700,
                        mb: 0.5,
                    }}
                >
                    {title}
                </Typography>

                {subtitle && (
                    <Typography
                        color="text.secondary"
                    >
                        {subtitle}
                    </Typography>
                )}
            </Box>

            {action}
        </Box>
    );
}