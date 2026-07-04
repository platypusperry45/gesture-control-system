import { useEffect, useState } from "react";

import { Grid } from "@mui/material";

import { motion } from "framer-motion";

import api from "../services/api";

import DashboardLayout from "../layouts/DashboardLayout.jsx";

import CameraCard from "../components/cards/CameraCard";
import PredictionCard from "../components/cards/PredictionCard";
import StatusCard from "../components/cards/StatusCard";
import MetricsCard from "../components/cards/MetricsCard";
import ControlPanel from "../components/cards/ControlPanel";
import RecentGestures from "../components/cards/RecentGestures";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

export default function Dashboard() {

    const [status, setStatus] = useState({

        camera: false,

        model_loaded: false,

        inference_running: false,

        prediction: null,

        confidence: 0,

        action: null,

        fps: 0,

        uptime: "--",

    });

    const [history, setHistory] = useState([]);

    useEffect(() => {

        async function load() {

            try {

                const { data } = await api.get("/status");

                setStatus(data);

                if (data.prediction) {

                    setHistory(previous => {

                        if (previous[0] === data.prediction)
                            return previous;

                        return [

                            data.prediction,

                            ...previous,

                        ].slice(0, 10);

                    });

                }

            }

            catch (err) {

                console.log(err);

            }

        }

        load();

        const timer = setInterval(load, 1000);

        return () => clearInterval(timer);

    }, []);

    return (

        <DashboardLayout>

            <motion.div

                initial={{ opacity: 0, y: 20 }}

                animate={{ opacity: 1, y: 0 }}

                transition={{ duration: .45 }}

            >

                <PageContainer>

                    <SectionHeader

                        title="Dashboard"

                        subtitle="Monitor real-time gesture recognition, desktop automation and AI system performance."

                    />

                    <Grid

                        container

                        spacing={3.5}

                        alignItems="stretch"

                    >

                        <Grid

                            size={{

                                xs: 12,

                                lg: 8,

                            }}

                        >

                            <CameraCard />

                        </Grid>

                        <Grid

                            size={{

                                xs: 12,

                                lg: 4,

                            }}

                        >

                            <PredictionCard status={status} />

                        </Grid>

                        <Grid

                            size={{

                                xs: 12,

                                md: 4,

                            }}

                        >

                            <StatusCard status={status} />

                        </Grid>

                        <Grid

                            size={{

                                xs: 12,

                                md: 5,

                            }}

                        >

                            <MetricsCard status={status} />

                        </Grid>

                        <Grid

                            size={{

                                xs: 12,

                                md: 3,

                            }}

                        >

                            <ControlPanel />

                        </Grid>

                        <Grid

                            size={12}

                        >

                            <RecentGestures history={history} />

                        </Grid>

                    </Grid>

                </PageContainer>

            </motion.div>

        </DashboardLayout>

    );

}