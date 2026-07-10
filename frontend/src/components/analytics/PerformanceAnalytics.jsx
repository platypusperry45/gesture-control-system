import {
    Stack,
    Typography,
} from "@mui/material";


import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
    CartesianGrid,
} from "recharts";


import GlassCard from "../ui/GlassCard";



export default function PerformanceAnalytics({ data }) {


    const runtime = data?.runtime || {};
    const training = data?.training || {};



    const fpsHistory =
        runtime.fps_history || [];


    const confidenceHistory =
        runtime.confidence_history || [];



    const length = Math.max(
        fpsHistory.length,
        confidenceHistory.length
    );



    const chartData = Array.from(
        { length },
        (_, index) => ({

            time:index + 1,

            fps:
                fpsHistory[index] || 0,


            confidence:
                confidenceHistory[index]
                    ? confidenceHistory[index] * 100
                    : 0,

        })
    );



    return (

        <GlassCard

            sx={{

                p:3,

                height:380,

            }}

        >


            <Stack

                spacing={1}

                mb={3}

            >

                <Typography

                    variant="h6"

                    fontWeight={700}

                >

                    Model Performance

                </Typography>



                <Typography

                    variant="body2"

                    color="text.secondary"

                >

                    Live inference speed and confidence tracking

                </Typography>


            </Stack>




            {

                chartData.length > 0 ?


                <ResponsiveContainer

                    width="100%"

                    height={260}

                >


                    <LineChart

                        data={chartData}

                    >


                        <CartesianGrid

                            strokeDasharray="3 3"

                        />


                        <XAxis

                            dataKey="time"

                        />


                        <YAxis/>


                        <Tooltip/>




                        <Line

                            type="monotone"

                            dataKey="fps"

                            name="FPS"

                            dot={false}

                        />



                        <Line

                            type="monotone"

                            dataKey="confidence"

                            name="Confidence %"

                            dot={false}

                        />



                    </LineChart>


                </ResponsiveContainer>



                :


                <Stack

                    height="80%"

                    justifyContent="center"

                    alignItems="center"

                >

                    <Typography

                        color="text.secondary"

                    >

                        Waiting for inference data...

                    </Typography>


                </Stack>


            }



        </GlassCard>


    );

}