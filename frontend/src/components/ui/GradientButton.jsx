import { Button } from "@mui/material";

export default function GradientButton({
    children,
    sx = {},
    ...props
}) {
    return (
        <Button
            variant="contained"
            {...props}
            sx={{
                background:
                    "linear-gradient(135deg,#6366F1,#8B5CF6)",

                color: "#fff",

                boxShadow:
                    "0 10px 30px rgba(99,102,241,.35)",

                "&:hover": {
                    background:
                        "linear-gradient(135deg,#5B5EF6,#7C3AED)",

                    boxShadow:
                        "0 14px 34px rgba(99,102,241,.45)",
                },

                ...sx,
            }}
        >
            {children}
        </Button>
    );
}