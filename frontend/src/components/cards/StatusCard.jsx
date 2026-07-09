import {
    Stack,
    Box,
    Typography,
    Chip,
} from "@mui/material";

import CameraAltIcon from "@mui/icons-material/CameraAlt";
import MemoryIcon from "@mui/icons-material/Memory";
import PsychologyAltIcon from "@mui/icons-material/PsychologyAlt";
import CircleIcon from "@mui/icons-material/Circle";

import { motion } from "framer-motion";

import DashboardCard from "../cards/DashboardCard";

function StatusRow({
    icon,
    title,
    online,
}) {
    return (
        <motion.div
            whileHover={{
                scale: 1.02,
            }}
            transition={{
                duration: .2,
            }}
        >
            <Box
                sx={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "space-between",

                    p: 2,

                    borderRadius: 3,

                    bgcolor: "rgba(255,255,255,.03)",

                    border:
                        "1px solid rgba(255,255,255,.06)",
                }}
            >
                <Stack
                    direction="row"
                    spacing={2}
                    alignItems="center"
                >
                    {icon}

                    <Typography fontWeight={600}>
                        {title}
                    </Typography>
                </Stack>

                <Chip
                    size="small"
                    color={online ? "success" : "error"}
                    icon={
                        <motion.div
                            animate={{
                                opacity: [1, .35, 1],
                                scale: [1, .8, 1],
                            }}
                            transition={{
                                repeat: Infinity,
                                duration: 1.2,
                            }}
                        >
                            <CircleIcon
                                sx={{
                                    fontSize: 10,
                                }}
                            />
                        </motion.div>
                    }
                    label={online ? "ONLINE" : "OFFLINE"}
                />
            </Box>
        </motion.div>
    );
}

export default function StatusCard({ status }) {

    return (

        <DashboardCard
            title="System Status"
            subtitle="Live backend health"
        >

            <Stack spacing={2.2}>

                <StatusRow
                    title="Camera"
                    online={status.camera}
                    icon={
                        <CameraAltIcon color="primary" />
                    }
                />

                <StatusRow
                    title="AI Model"
                    online={status.model_loaded}
                    icon={
                        <MemoryIcon color="primary" />
                    }
                />

                <StatusRow
                    title="Inference Engine"
                    online={status.inference_running}
                    icon={
                        <PsychologyAltIcon color="primary" />
                    }
                />

            </Stack>

        </DashboardCard>

    );

}