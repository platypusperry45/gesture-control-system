import {

    AppBar,

    Avatar,

    Box,

    Chip,

    Toolbar,

    Typography,

} from "@mui/material";

import BoltIcon from "@mui/icons-material/Bolt";

export default function AppHeader() {

    return (

        <AppBar

            elevation={0}

            position="fixed"

            sx={{

                backdropFilter: "blur(16px)",

                bgcolor: "rgba(11,16,32,.75)",

                borderBottom:

                    "1px solid rgba(255,255,255,.05)",

            }}

        >

            <Toolbar>

                <BoltIcon
                    color="primary"
                    sx={{
                        mr:2,
                        fontSize:32,
                    }}
                />

                <Typography

                    variant="h6"

                    sx={{

                        fontWeight:700,

                        flexGrow:1,

                    }}

                >

                    Gesture AI Desktop Control

                </Typography>

                <Chip

                    color="success"

                    label="System Online"

                />

                <Avatar
                    sx={{
                        ml:3,
                    }}
                >
                    A
                </Avatar>

            </Toolbar>

        </AppBar>

    );

}