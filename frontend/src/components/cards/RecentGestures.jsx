import {
    Avatar,
    List,
    ListItem,
    ListItemAvatar,
    ListItemText,
    Typography,
} from "@mui/material";

import PanToolIcon from "@mui/icons-material/PanTool";

import DashboardCard from "./DashboardCard";

export default function RecentGestures({ history }) {
    return (
        <DashboardCard
            title="Recent Activity"
            subtitle="Latest recognized gestures"
        >
            <List disablePadding>
                {history.length === 0 ? (
                    <Typography
                        color="text.secondary"
                    >
                        Waiting for gesture predictions...
                    </Typography>
                ) : (
                    history.map((gesture, index) => (
                        <ListItem
                            key={index}
                            divider={index !== history.length - 1}
                            disableGutters
                        >
                            <ListItemAvatar>
                                <Avatar
                                    sx={{
                                        bgcolor: "primary.main",
                                    }}
                                >
                                    <PanToolIcon />
                                </Avatar>
                            </ListItemAvatar>

                            <ListItemText
                                primary={gesture}
                                secondary="Recognized recently"
                            />
                        </ListItem>
                    ))
                )}
            </List>
        </DashboardCard>
    );
}