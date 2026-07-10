import { useEffect, useState } from "react";

import {
    Stack,
    Typography,
    Chip,
} from "@mui/material";

import StorageRoundedIcon from "@mui/icons-material/StorageRounded";

import GlassCard from "../ui/GlassCard";

import api from "../../services/api";


export default function BackendSettings() {

    const [status, setStatus] = useState(null);


    useEffect(() => {

        const fetchStatus = async () => {

            try {

                const response = await api.get("/health");

                setStatus(response.data);

            } catch(error) {

                setStatus({
                    status:"offline"
                });

            }

        };


        fetchStatus();


        const interval = setInterval(
            fetchStatus,
            5000
        );


        return () => clearInterval(interval);


    },[]);



    return (

        <GlassCard
            sx={{
                p:3,
                height:"100%",
            }}
        >

            <Stack
                direction="row"
                spacing={1}
                alignItems="center"
                mb={3}
            >

                <StorageRoundedIcon color="primary"/>

                <Typography
                    variant="h6"
                    fontWeight={700}
                >
                    Backend Settings
                </Typography>

            </Stack>


            <Stack spacing={3}>


                <Typography>
                    API Connection
                </Typography>


                <Chip

                    label={
                        status?.status === "healthy"
                        ? "Backend Online"
                        : "Backend Offline"
                    }

                    color={
                        status?.status === "healthy"
                        ? "success"
                        : "error"
                    }

                />


                <Typography
                    color="text.secondary"
                >

                    FastAPI backend connection status.

                </Typography>


            </Stack>


        </GlassCard>

    );

}