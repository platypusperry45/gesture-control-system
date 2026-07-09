import { Box } from "@mui/material";

export default function PageContainer({ children }) {
    return (
        <Box
            sx={{
                width: "100%",
                maxWidth: "100%",

                minWidth: 0,

                overflowX: "hidden",

                display: "flex",
                flexDirection: "column",

                gap: 3,
            }}
        >
            {children}
        </Box>
    );
}