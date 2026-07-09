import { Box } from "@mui/material";

import SideNavigation from "./SideNavigation";
import AppHeader from "./AppHeader";

export default function DashboardLayout({ children }) {
    return (
        <Box
            sx={{
                display: "flex",
                minHeight: "100vh",
                background: "#060A14",
            }}
        >
            <SideNavigation />

            <Box
                sx={{
                    flex: 1,
                    display: "flex",
                    flexDirection: "column",
                    minWidth: 0,
                    overflow: "hidden",
                }}
            >
                <AppHeader />

                <Box
                    component="main"
                    sx={{
                        flex: 1,
                        p: 6,

                        overflowY: "auto",
                        overflowX: "hidden",
                    }}
                >
                    {children}
                </Box>
            </Box>
        </Box>
    );
}