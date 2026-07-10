import {
    Grid,
    CircularProgress,
    Box,
    Typography,
} from "@mui/material";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";

import DashboardLayout from "../components/layouts/DashboardLayout";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

import AnalyticsOverview from "../components/analytics/AnalyticsOverview";
import PredictionAnalytics from "../components/analytics/PredictionAnalytics";
import PerformanceAnalytics from "../components/analytics/PerformanceAnalytics";
import SystemAnalytics from "../components/analytics/SystemAnalytics";


export default function Analytics() {


    const [analytics, setAnalytics] = useState(null);

    const [loading, setLoading] = useState(true);



    async function fetchAnalytics(){

        try{

            const response = await fetch(
                "http://127.0.0.1:8000/analytics"
            );

            const data = await response.json();

            setAnalytics(data);


        }
        catch(error){

            console.error(
                "Analytics fetch failed:",
                error
            );

        }
        finally{

            setLoading(false);

        }

    }



    useEffect(()=>{


        fetchAnalytics();


        const interval = setInterval(
            fetchAnalytics,
            2000
        );


        return ()=>clearInterval(interval);


    },[]);




    if(loading){


        return (

            <DashboardLayout>

                <Box

                    sx={{

                        height:"70vh",

                        display:"flex",

                        alignItems:"center",

                        justifyContent:"center",

                        flexDirection:"column",

                        gap:2,

                    }}

                >

                    <CircularProgress/>


                    <Typography>

                        Loading analytics...

                    </Typography>


                </Box>


            </DashboardLayout>

        );


    }




    return (

        <DashboardLayout>


            <motion.div

                initial={{

                    opacity:0,

                    y:20,

                }}

                animate={{

                    opacity:1,

                    y:0,

                }}

                transition={{

                    duration:.4,

                }}

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

                            size={{

                                xs:12,

                            }}

                        >

                            <AnalyticsOverview

                                data={analytics}

                            />

                        </Grid>




                        <Grid

                            size={{

                                xs:12,

                                lg:6,

                            }}

                        >

                            <PredictionAnalytics

                                data={analytics}

                            />


                        </Grid>





                        <Grid

                            size={{

                                xs:12,

                                lg:6,

                            }}

                        >

                            <PerformanceAnalytics

                                data={analytics}

                            />


                        </Grid>





                        <Grid

                            size={{

                                xs:12,

                            }}

                        >

                            <SystemAnalytics

                                data={analytics}

                            />


                        </Grid>



                    </Grid>


                </PageContainer>



            </motion.div>



        </DashboardLayout>


    );

}