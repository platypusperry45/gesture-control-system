import {
    Drawer,
    Toolbar,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Box,
    Typography,
} from "@mui/material";

import { NavLink } from "react-router-dom";

import DashboardIcon from "@mui/icons-material/Dashboard";
import PanToolIcon from "@mui/icons-material/PanTool";
import KeyboardIcon from "@mui/icons-material/Keyboard";
import ModelTrainingIcon from "@mui/icons-material/ModelTraining";
import AnalyticsIcon from "@mui/icons-material/Analytics";
import SettingsIcon from "@mui/icons-material/Settings";

const drawerWidth = 270;

const menu = [
    {
        name: "Dashboard",
        path: "/dashboard",
        icon: <DashboardIcon />,
    },
    {
        name: "Gestures",
        path: "/gestures",
        icon: <PanToolIcon />,
    },
    {
        name: "Actions",
        path: "/actions",
        icon: <KeyboardIcon />,
    },
    {
        name: "Training",
        path: "/training",
        icon: <ModelTrainingIcon />,
    },
    {
        name: "Analytics",
        path: "/analytics",
        icon: <AnalyticsIcon />,
    },
    {
        name: "Settings",
        path: "/settings",
        icon: <SettingsIcon />,
    },
];

export default function SideNavigation() {
    return (
        <Drawer
            variant="permanent"
            sx={{
                width: drawerWidth,
                flexShrink: 0,

                "& .MuiDrawer-paper": {
                    width: drawerWidth,
                    bgcolor: "#0B1020",
                    borderRight: "1px solid rgba(255,255,255,.06)",
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
                <Typography
                    variant="overline"
                    color="text.secondary"
                    sx={{
                        letterSpacing: 2,
                    }}
                >
                    NAVIGATION
                </Typography>
            </Box>

            <List>
                {menu.map((item) => (
                    <ListItemButton
                        key={item.name}
                        component={NavLink}
                        to={item.path}
                        sx={{
                            mx: 2,
                            my: 0.5,
                            borderRadius: 3,
                            height: 50,

                            transition: "all .25s",

                            "&:hover": {
                                bgcolor: "rgba(255,255,255,.05)",
                            },

                            "&.active": {
                                background:
                                    "linear-gradient(135deg,#4F46E5,#7C3AED)",

                                color: "#fff",

                                boxShadow:
                                    "0 10px 25px rgba(99,102,241,.35)",

                                "& .MuiListItemIcon-root": {
                                    color: "#fff",
                                },
                            },
                        }}
                    >
                        <ListItemIcon
                            sx={{
                                minWidth: 42,
                                color: "text.secondary",
                            }}
                        >
                            {item.icon}
                        </ListItemIcon>

                        <ListItemText primary={item.name} />
                    </ListItemButton>
                ))}
            </List>
        </Drawer>
    );
}