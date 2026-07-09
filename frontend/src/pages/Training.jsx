import { useEffect, useState } from "react";
import { Grid } from "@mui/material";
import { motion } from "framer-motion";

import DashboardLayout from "../components/layouts/DashboardLayout";

import PageContainer from "../components/ui/PageContainer";
import SectionHeader from "../components/ui/SectionHeader";

import TrainingStats from "../components/training/TrainingStats";
import TrainingProgress from "../components/training/TrainingProgress";
import TrainingControls from "../components/training/TrainingControls";
import TrainingCharts from "../components/training/TrainingCharts";
import DatasetOverview from "../components/training/DatasetOverview";
import TrainingLogs from "../components/training/TrainingLogs";
import DeployCard from "../components/training/DeployCard";

import {
    startTraining,
    stopTraining,
} from "../services/trainingService";

import { connectTrainingSocket } from "../services/trainingSocket";

export default function Training() {

    const [training, setTraining] = useState({

        running:false,
        completed:false,

        epoch:0,
        total_epochs:20,

        accuracy:0,
        val_accuracy:0,

        loss:0,
        val_loss:0,

        progress:0,

        logs:[],

    });

    useEffect(()=>{

        const socket = connectTrainingSocket((data)=>{

            setTraining(data);

        });

        return ()=>socket.close();

    },[]);

    async function handleStart(config){

        await startTraining(config);

    }

    async function handleStop(){

        await stopTraining();

    }

    return(

        <DashboardLayout>

            <motion.div

                initial={{opacity:0,y:20}}

                animate={{opacity:1,y:0}}

                transition={{duration:.4}}

            >

                <PageContainer>

                    <SectionHeader

                        title="Training Centre"

                        subtitle="Train, monitor and deploy gesture recognition models."

                    />

                    <TrainingStats

                        images={2435}

                        classes={6}

                        epochs={training.total_epochs}

                        accuracy={training.accuracy}

                    />

                    <Grid
                        container
                        spacing={3}
                        sx={{mt:2}}
                    >

                        {/* Progress */}

                        <Grid
                            size={{
                                xs:12
                            }}
                        >

                            <TrainingProgress

                                progress={training.progress}

                                epoch={training.epoch}

                                totalEpochs={training.total_epochs}

                                accuracy={training.accuracy}

                                loss={training.loss}

                                valAccuracy={training.val_accuracy}

                                status={
                                    training.running
                                        ? "Training"
                                        : training.completed
                                            ? "Completed"
                                            : "Idle"
                                }

                            />

                        </Grid>

                        {/* Controls */}

                        <Grid
                            size={{
                                xs:12
                            }}
                        >

                            <TrainingControls

                                onStart={handleStart}

                                onStop={handleStop}

                            />

                        </Grid>

                        {/* Charts */}

                        <Grid
                            size={{
                                xs:12
                            }}
                        >

                            <TrainingCharts

                                epoch={training.epoch}

                                accuracy={training.accuracy}

                                valAccuracy={training.val_accuracy}

                                loss={training.loss}

                            />

                        </Grid>

                        {/* Dataset */}

                        <Grid
                            size={{
                                xs:12,
                                md:6
                            }}
                        >

                            <DatasetOverview/>

                        </Grid>

                        {/* Logs */}

                        <Grid
                            size={{
                                xs:12,
                                md:6
                            }}
                        >

                            <TrainingLogs

                                logs={training.logs}

                            />

                        </Grid>

                        {/* Deploy */}

                        <Grid
                            size={{
                                xs:12
                            }}
                        >

                            <DeployCard/>

                        </Grid>

                    </Grid>

                </PageContainer>

            </motion.div>

        </DashboardLayout>

    );

}