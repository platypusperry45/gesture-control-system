import { Paper, Typography, Box } from "@mui/material";

export default function DashboardCard({
    title,
    children,
    height = "100%",
}) {

    return (

        <Paper
            elevation={0}
            sx={{

                height,

                p:3,

                borderRadius:4,

                bgcolor:"rgba(255,255,255,.04)",

                border:"1px solid rgba(255,255,255,.06)",

                backdropFilter:"blur(20px)",

            }}
        >

            <Typography
                variant="h6"
                fontWeight={700}
                mb={2}
            >
                {title}
            </Typography>

            <Box>

                {children}

            </Box>

        </Paper>

    );

}