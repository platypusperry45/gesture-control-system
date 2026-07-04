import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";

import AppHeader from "../components/layouts/AppHeader";
import SideNavigation from "../components/layouts/SideNavigation";

export default function Layout({ children }) {

    return (

        <Box sx={{ display: "flex" }}>

            <AppHeader />

            <SideNavigation />

            <Box
                component="main"
                sx={{
                    flexGrow: 1,
                    p: 3,
                }}
            >

                <Toolbar />

                {children}

            </Box>

        </Box>

    );

}