import {
    Avatar,
    Box,
    Chip,
    Divider,
    List,
    ListItem,
    ListItemAvatar,
    ListItemText,
    Typography,
} from "@mui/material";

import PanToolIcon from "@mui/icons-material/PanTool";
import AccessTimeIcon from "@mui/icons-material/AccessTime";

import { motion, AnimatePresence } from "framer-motion";

import DashboardCard from "../cards/DashboardCard";

export default function RecentGestures({ history }) {

    return (

        <DashboardCard
            title="Recent Activity"
            subtitle="Latest recognized gestures"
        >

            {

                history.length === 0 ?

                (

                    <Box
                        sx={{
                            py: 5,
                            textAlign: "center",
                        }}
                    >

                        <PanToolIcon
                            sx={{
                                fontSize: 52,
                                color: "text.secondary",
                                mb: 1,
                            }}
                        />

                        <Typography
                            color="text.secondary"
                        >
                            Waiting for gesture predictions...
                        </Typography>

                    </Box>

                )

                :

                (

                    <List disablePadding>

                        <AnimatePresence>

                            {

                                history.map(

                                    (gesture, index) => (

                                        <motion.div

                                            key={`${gesture}-${index}`}

                                            initial={{
                                                opacity: 0,
                                                x: -30,
                                            }}

                                            animate={{
                                                opacity: 1,
                                                x: 0,
                                            }}

                                            exit={{
                                                opacity: 0,
                                                x: 30,
                                            }}

                                            transition={{
                                                duration: .3,
                                                delay: index * .05,
                                            }}

                                        >

                                            <ListItem
                                                disableGutters
                                                sx={{
                                                    py: 1.8,
                                                }}
                                            >

                                                <ListItemAvatar>

                                                    <motion.div
                                                        whileHover={{
                                                            rotate: 15,
                                                            scale: 1.1,
                                                        }}
                                                    >

                                                        <Avatar
                                                            sx={{
                                                                bgcolor:
                                                                    "primary.main",

                                                                width: 46,

                                                                height: 46,
                                                            }}
                                                        >

                                                            <PanToolIcon />

                                                        </Avatar>

                                                    </motion.div>

                                                </ListItemAvatar>

                                                <ListItemText

                                                    primary={

                                                        <Typography
                                                            fontWeight={700}
                                                            textTransform="capitalize"
                                                        >
                                                            {gesture}
                                                        </Typography>

                                                    }

                                                    secondary={

                                                        <Box
                                                            sx={{
                                                                display: "flex",
                                                                alignItems: "center",
                                                                gap: 1,
                                                                mt: .5,
                                                            }}
                                                        >

                                                            <AccessTimeIcon
                                                                sx={{
                                                                    fontSize: 14,
                                                                }}
                                                            />

                                                            <Typography
                                                                variant="caption"
                                                                color="text.secondary"
                                                            >
                                                                Just now
                                                            </Typography>

                                                            <Chip
                                                                size="small"
                                                                color="primary"
                                                                label="Detected"
                                                            />

                                                        </Box>

                                                    }

                                                />

                                            </ListItem>

                                            {

                                                index !== history.length - 1 &&

                                                <Divider
                                                    sx={{
                                                        opacity: .08,
                                                    }}
                                                />

                                            }

                                        </motion.div>

                                    )

                                )

                            }

                        </AnimatePresence>

                    </List>

                )

            }

        </DashboardCard>

    );

}