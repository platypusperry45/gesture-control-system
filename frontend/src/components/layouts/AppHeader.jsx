import {
    AppBar,
    Avatar,
    Box,
    Chip,
    Stack,
    Toolbar,
    Typography,
} from "@mui/material";

import PsychologyRoundedIcon from "@mui/icons-material/PsychologyRounded";

const drawerWidth = 270;

export default function AppHeader() {
    return (
        <AppBar
            position="fixed"
            elevation={0}
            sx={{
                /**
                 * Critical Layout Fix
                 * -------------------
                 * The AppBar must account for the permanent drawer.
                 * This eliminates the visual right-shift and keeps
                 * the header aligned with the page content.
                 */
                left: {
                    xs: 0,
                    lg: `${drawerWidth}px`,
                },

                width: {
                    xs: "100%",
                    lg: `calc(100% - ${drawerWidth}px)`,
                },

                backdropFilter: "blur(20px)",
                WebkitBackdropFilter: "blur(20px)",

                background: "rgba(8,12,20,.88)",

                borderBottom:
                    "1px solid rgba(255,255,255,.06)",

                boxShadow: "none",

                zIndex: (theme) => theme.zIndex.drawer + 1,
            }}
        >
            <Toolbar
                sx={{
                    minHeight: 72,
                    px: {
                        xs: 2,
                        sm: 3,
                        md: 4,
                    },
                }}
            >
                <Stack
                    direction="row"
                    alignItems="center"
                    justifyContent="space-between"
                    sx={{
                        width: "100%",
                        minWidth: 0,
                    }}
                >
                    {/* Left */}

                    <Stack
                        direction="row"
                        spacing={2}
                        alignItems="center"
                        sx={{
                            minWidth: 0,
                            flex: 1,
                        }}
                    >
                        <Avatar
                            sx={{
                                bgcolor: "primary.main",
                                width: 48,
                                height: 48,
                                flexShrink: 0,
                            }}
                        >
                            <PsychologyRoundedIcon />
                        </Avatar>

                        <Box
                            sx={{
                                minWidth: 0,
                            }}
                        >
                            <Typography
                                variant="h6"
                                noWrap
                                sx={{
                                    fontWeight: 700,
                                    letterSpacing: "-0.02em",
                                }}
                            >
                                Gesture Control Dashboard
                            </Typography>

                            <Typography
                                variant="body2"
                                color="text.secondary"
                                noWrap
                            >
                                AI Powered Desktop Automation
                            </Typography>
                        </Box>
                    </Stack>

                    {/* Right */}

                    <Chip
                        color="success"
                        label="System Online"
                        sx={{
                            ml: 2,
                            flexShrink: 0,
                            fontWeight: 700,
                            borderRadius: 999,
                            px: 0.5,
                        }}
                    />
                </Stack>
            </Toolbar>
        </AppBar>
    );
}