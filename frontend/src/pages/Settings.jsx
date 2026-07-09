import { Grid } from "@mui/material";
import { motion } from "framer-motion";

import DashboardLayout from "../components/layouts/DashboardLayout";
import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

import GeneralSettings from "../components/settings/GeneralSettings";
import CameraSettings from "../components/settings/CameraSettings";
import AISettings from "../components/settings/AISettings";
import BackendSettings from "../components/settings/BackendSettings";
import SystemSettings from "../components/settings/SystemSettings";

export default function Settings() {

    return (

        <DashboardLayout>

            <motion.div

                initial={{ opacity: 0, y: 20 }}

                animate={{ opacity: 1, y: 0 }}

                transition={{ duration: .4 }}

            >

                <PageContainer>

                    <SectionHeader

                        title="Settings"

                        subtitle="Configure camera, AI model, backend and application preferences."

                    />

                    <Grid

                        container

                        spacing={3}

                    >

                        <Grid

                            size={{

                                xs:12,

                                md:6,

                            }}

                        >

                            <GeneralSettings/>

                        </Grid>

                        <Grid

                            size={{

                                xs:12,

                                md:6,

                            }}

                        >

                            <CameraSettings/>

                        </Grid>

                        <Grid

                            size={{

                                xs:12,

                                md:6,

                            }}

                        >

                            <AISettings/>

                        </Grid>

                        <Grid

                            size={{

                                xs:12,

                                md:6,

                            }}

                        >

                            <BackendSettings/>

                        </Grid>

                        <Grid

                            size={{

                                xs:12,

                            }}

                        >

                            <SystemSettings/>

                        </Grid>

                    </Grid>

                </PageContainer>

            </motion.div>

        </DashboardLayout>

    );

}