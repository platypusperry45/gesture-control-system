import { Paper } from "@mui/material";

export default function GlassCard({
    children,
    sx = {},
}) {
    return (
        <Paper
            elevation={0}
            sx={{
                position: "relative",

                borderRadius: 5,

                overflow: "hidden",

                background:
                    "linear-gradient(145deg,#111827,#0B1220)",

                border:
                    "1px solid rgba(255,255,255,.06)",

                boxShadow:
                    "0 20px 60px rgba(0,0,0,.35)",

                transition: ".25s",

                "&:hover": {
                    transform: "translateY(-3px)",
                    boxShadow:
                        "0 24px 70px rgba(0,0,0,.45)",
                },

                "& *": {
                    boxSizing: "border-box",
                },

                ...sx,
            }}
        >
            {children}
        </Paper>
    );
}