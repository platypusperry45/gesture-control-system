import { useState } from "react";

import {
    Box,
    Stack,
    Typography,
    Switch,
    FormControl,
    Select,
    MenuItem,
    InputLabel,
    Divider,
    Button,
} from "@mui/material";

import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";
import DarkModeRoundedIcon from "@mui/icons-material/DarkModeRounded";
import NotificationsRoundedIcon from "@mui/icons-material/NotificationsRounded";
import SaveRoundedIcon from "@mui/icons-material/SaveRounded";

import GlassCard from "../ui/GlassCard";

export default function GeneralSettings() {

    const [theme, setTheme] = useState("Dark");

    const [notifications, setNotifications] = useState(true);

    const [autoSave, setAutoSave] = useState(true);

    return (

        <GlassCard
            sx={{
                p: 3,
                height: "100%",
            }}
        >

            <Stack
                direction="row"
                spacing={1}
                alignItems="center"
                mb={3}
            >

                <SettingsRoundedIcon color="primary" />

                <Typography
                    variant="h6"
                    fontWeight={700}
                >
                    General Settings
                </Typography>

            </Stack>

            <Stack spacing={3}>

                <Box>

                    <Typography
                        fontWeight={600}
                        mb={1}
                    >
                        Theme
                    </Typography>

                    <FormControl fullWidth>

                        <InputLabel>Theme</InputLabel>

                        <Select

                            value={theme}

                            label="Theme"

                            onChange={(e)=>setTheme(e.target.value)}

                        >

                            <MenuItem value="Dark">

                                Dark

                            </MenuItem>

                            <MenuItem value="Light">

                                Light

                            </MenuItem>

                            <MenuItem value="System">

                                System

                            </MenuItem>

                        </Select>

                    </FormControl>

                </Box>

                <Divider/>

                <Stack

                    direction="row"

                    justifyContent="space-between"

                    alignItems="center"

                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <DarkModeRoundedIcon color="primary"/>

                        <Typography>

                            Enable Dark Theme

                        </Typography>

                    </Stack>

                    <Switch
                        checked={theme==="Dark"}
                    />

                </Stack>

                <Stack

                    direction="row"

                    justifyContent="space-between"

                    alignItems="center"

                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <NotificationsRoundedIcon color="primary"/>

                        <Typography>

                            Notifications

                        </Typography>

                    </Stack>

                    <Switch

                        checked={notifications}

                        onChange={(e)=>setNotifications(e.target.checked)}

                    />

                </Stack>

                <Stack

                    direction="row"

                    justifyContent="space-between"

                    alignItems="center"

                >

                    <Stack
                        direction="row"
                        spacing={1}
                        alignItems="center"
                    >

                        <SaveRoundedIcon color="primary"/>

                        <Typography>

                            Auto Save Settings

                        </Typography>

                    </Stack>

                    <Switch

                        checked={autoSave}

                        onChange={(e)=>setAutoSave(e.target.checked)}

                    />

                </Stack>

                <Divider/>

                <Button

                    fullWidth

                    variant="contained"

                    size="large"

                >

                    Save Preferences

                </Button>

            </Stack>

        </GlassCard>

    );

}