import {
    Avatar,
    Box,
    Chip,
    Divider,
    Drawer,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Stack,
    Toolbar,
    Typography,
} from "@mui/material";

import DashboardRoundedIcon from "@mui/icons-material/DashboardRounded";
import PanToolRoundedIcon from "@mui/icons-material/PanToolRounded";
import KeyboardRoundedIcon from "@mui/icons-material/KeyboardRounded";
import ModelTrainingRoundedIcon from "@mui/icons-material/ModelTrainingRounded";
import AnalyticsRoundedIcon from "@mui/icons-material/AnalyticsRounded";
import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";
import BoltRoundedIcon from "@mui/icons-material/BoltRounded";

import {
    useLocation,
    useNavigate,
} from "react-router-dom";

const drawerWidth = 270;

const menu = [
    {
        text: "Dashboard",
        icon: <DashboardRoundedIcon />,
        path: "/",
    },
    {
        text: "Gestures",
        icon: <PanToolRoundedIcon />,
        path: "/gestures",
    },
    {
        text: "Actions",
        icon: <KeyboardRoundedIcon />,
        path: "/actions",
    },
    {
        text: "Training",
        icon: <ModelTrainingRoundedIcon />,
        path: "/training",
    },
    {
        text: "Analytics",
        icon: <AnalyticsRoundedIcon />,
        path: "/analytics",
    },
    {
        text: "Settings",
        icon: <SettingsRoundedIcon />,
        path: "/settings",
    },
];

export default function SideNavigation() {

    const navigate = useNavigate();

    const location = useLocation();

    return (

        <Drawer

            variant="permanent"

            sx={{

                width: drawerWidth,

                flexShrink: 0,

                "& .MuiDrawer-paper": {

                    width: drawerWidth,

                    bgcolor: "#0B1220",

                    color: "white",

                    borderRight:
                        "1px solid rgba(255,255,255,.05)",

                    overflowX: "hidden",

                    boxSizing: "border-box",

                },

            }}

        >

            <Toolbar />

            <Box
                sx={{
                    px: 3,
                    py: 2,
                }}
            >

                <Stack
                    direction="row"
                    spacing={2}
                    alignItems="center"
                >

                    <Avatar
                        sx={{
                            bgcolor: "primary.main",
                            width: 52,
                            height: 52,
                        }}
                    >
                        <BoltRoundedIcon />
                    </Avatar>

                    <Box>

                        <Typography
                            fontWeight={700}
                            fontSize={18}
                        >
                            Gesture AI
                        </Typography>

                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            Desktop Automation
                        </Typography>

                    </Box>

                </Stack>

                <Chip
                    label="AI Running"
                    color="success"
                    size="small"
                    sx={{
                        mt: 2,
                        borderRadius: 2,
                    }}
                />

            </Box>

            <Divider
                sx={{
                    borderColor:
                        "rgba(255,255,255,.05)",
                }}
            />

            <List
                sx={{
                    mt: 2,
                    px: 2,
                }}
            >

                {

                    menu.map((item) => {

                        const selected =
                            location.pathname === item.path;

                        return (

                            <ListItemButton

                                key={item.text}

                                selected={selected}

                                onClick={() =>
                                    navigate(item.path)
                                }

                                sx={{

                                    borderRadius: 3,

                                    py: 1.5,

                                    mb: 1,

                                    transition: ".25s",

                                    "& .MuiListItemIcon-root": {

                                        minWidth: 42,

                                    },

                                    "&.Mui-selected": {

                                        background:
                                            "linear-gradient(135deg,#2563EB,#3B82F6)",

                                        color: "white",

                                        boxShadow:
                                            "0 12px 30px rgba(37,99,235,.35)",

                                    },

                                    "&.Mui-selected:hover": {

                                        background:
                                            "linear-gradient(135deg,#2563EB,#3B82F6)",

                                    },

                                    "&:hover": {

                                        background:
                                            "rgba(255,255,255,.06)",

                                    },

                                }}

                            >

                                <ListItemIcon

                                    sx={{

                                        color:
                                            selected
                                                ? "white"
                                                : "#94A3B8",

                                    }}

                                >

                                    {item.icon}

                                </ListItemIcon>

                                <ListItemText

                                    primary={item.text}

                                    primaryTypographyProps={{

                                        fontWeight:
                                            selected
                                                ? 700
                                                : 500,

                                    }}

                                />

                            </ListItemButton>

                        );

                    })

                }

            </List>

            <Box
                flex={1}
            />

            <Divider
                sx={{
                    borderColor:
                        "rgba(255,255,255,.05)",
                }}
            />

            <Box
                p={3}
            >

                <Typography
                    variant="caption"
                    color="text.secondary"
                >
                    Gesture Control System
                </Typography>

                <Typography
                    fontWeight={700}
                >
                    Version 2.0
                </Typography>

            </Box>

        </Drawer>

    );

}