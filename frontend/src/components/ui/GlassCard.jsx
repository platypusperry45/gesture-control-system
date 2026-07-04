import { Paper } from "@mui/material";

export default function GlassCard({ children, sx = {} }) {
    return (
        <Paper
            elevation={0}
            sx={{
                background: "rgba(20, 28, 45, 0.72)",
                backdropFilter: "blur(18px)",
                WebkitBackdropFilter: "blur(18px)",

                border: "1px solid rgba(255,255,255,.08)",

                borderRadius: 4,

                boxShadow:
                    "0 12px 40px rgba(0,0,0,.35)",

                overflow: "hidden",

                transition: "all .25s ease",

                "&:hover": {
                    transform: "translateY(-3px)",
                    boxShadow:
                        "0 18px 50px rgba(0,0,0,.45)",
                    borderColor:
                        "rgba(99,102,241,.28)",
                },

                ...sx,
            }}
        >
            {children}
        </Paper>
    );
}