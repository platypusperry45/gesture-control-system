import { Grid } from "@mui/material";
import { motion } from "framer-motion";

import DashboardLayout from "../components/layouts/DashboardLayout";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

import AnalyticsOverview from "../components/analytics/AnalyticsOverview";
import PredictionAnalytics from "../components/analytics/PredictionAnalytics";
import PerformanceAnalytics from "../components/analytics/PerformanceAnalytics";
import SystemAnalytics from "../components/analytics/SystemAnalytics";

export default function Analytics() {

    return (

        <DashboardLayout>

            <motion.div

                initial={{ opacity: 0, y: 20 }}

                animate={{ opacity: 1, y: 0 }}

                transition={{ duration: .4 }}

            >

                <PageContainer>

                    <SectionHeader

                        title="Analytics"

                        subtitle="Monitor model performance, prediction quality and system statistics."

                    />

                    <Grid
                        container
                        spacing={3}
                    >

                        <Grid
                            size={{ xs:12 }}
                        >

                            <AnalyticsOverview/>

                        </Grid>

                        <Grid
                            size={{
                                xs:12,
                                lg:6,
                            }}
                        >

                            <PredictionAnalytics/>

                        </Grid>

                        <Grid
                            size={{
                                xs:12,
                                lg:6,
                            }}
                        >

                            <PerformanceAnalytics/>

                        </Grid>

                        <Grid
                            size={{ xs:12 }}
                        >

                            <SystemAnalytics/>

                        </Grid>

                    </Grid>

                </PageContainer>

            </motion.div>

        </DashboardLayout>

    );

}